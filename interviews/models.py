# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.conf import settings

from django.contrib.sites.models import Site

from interviews.managers import InterviewManager

class Interview(models.Model):
    site = models.ForeignKey(Site, default=settings.SITE_ID)
    
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

class Answer(models.Model):
    interview = models.ForeignKey(Interview)
    order = models.IntegerField()
    question = models.TextField(blank=True)
    response = models.TextField(blank=True)
    
    class Meta:
        unique_together = (
            ('interview', 'order'),
        )
