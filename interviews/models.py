# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.conf import settings

from interviews.managers import InterviewManager

import datetime

class Question(models.Model):
    site = models.ForeignKey(Site, default=settings.SITE_ID)
    question = models.TextField()

    def __unicode__(self):
        return self.question

class InterviewTemplate(models.Model):
    site = models.ForeignKey(Site, default=settings.SITE_ID)
    
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    questions = models.ManyToManyField(Question, through='QuestionOrder')

    def __unicode__(self):
        return self.title

class QuestionOrder(models.Model):
    interview = models.ForeignKey(InterviewTemplate)
    question = models.ForeignKey(Question)
    order = models.IntegerField()

class Interview(models.Model):
    site = models.ForeignKey(Site, default=settings.SITE_ID)
    template = models.ForeignKey(InterviewTemplate)
    
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    
    is_published = models.BooleanField(default=False)
    published_on = models.DateTimeField(default=datetime.datetime.now)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)
    
    introduction = models.TextField(blank=True, null=True)
    footnotes = models.TextField(blank=True, null=True)

    objects = InterviewManager()

    class Meta:
        ordering = ["-published_on"]

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('interviews-detail', [self.slug])

    @property
    def answers(self):
        return Answer.objects.for_interview(self)

class AnswerManager(models.Manager):
    def for_interview(self, interview):
        return self.filter(interview=interview).filter(answered=True).order_by('order')

class Answer(models.Model):
    interview = models.ForeignKey(Interview)
    question = models.ForeignKey(Question)
    order = models.IntegerField()
    answered = models.BooleanField(default=False)
    response = models.TextField(blank=True)
    
    objects = AnswerManager()
    
    class Meta:
        unique_together = (
            ('interview', 'order'),
            ('interview', 'question'),
        )