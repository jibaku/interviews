# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone 

from django.contrib.sites.models import Site

from interviews.managers import InterviewManager

class Person(models.Model):
    SEX_CHOICES = (
        (1, 'Homme'),
        (2, 'Femme'),
    )
    name = models.CharField(max_length=255)
    birthdate = models.DateField(blank=True, null=True)
    sex = models.IntegerField(choices=SEX_CHOICES)

    def __unicode__(self):
        return self.name

    @property
    def age(self):
        if self.birthdate:
            today = datetime.date.today()
            return (today.year - self.birthdate.year) - int((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        else:
            return None


class Interview(models.Model):
    """
    """
    person = models.ForeignKey(Person)
    site = models.ForeignKey(Site, default=settings.SITE_ID)
    
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    
    is_published = models.BooleanField(default=False)
    published_on = models.DateTimeField(default=timezone.now)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)
    
    introduction = models.TextField(blank=True, null=True)
    footnotes = models.TextField(blank=True, null=True)
    
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    #place = models.TextField(blank=True, null=True)
    
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

    @property
    def selected_picture(self):
        return Picture.objects.filter(interviewpicture__is_selected=True).get(interview=self)

class Picture(models.Model):
    interview = models.ForeignKey(Interview)
    image = models.ImageField(upload_to='pictures')
    legend = models.TextField(blank=True)

    def __unicode__(self):
        return "%s - %s (%s)" % (self.interview, self.image, self.legend)

class Answer(models.Model):
    interview = models.ForeignKey(Interview)
    order = models.IntegerField()
    question = models.TextField(blank=True)
    response = models.TextField(blank=True)
    related_pictures = models.ManyToManyField(Picture, blank=True)

    class Meta:
        unique_together = (
            ('interview', 'order'),
        )


class Quote(models.Model):
    related_to = models.ForeignKey(Answer)
    author = models.CharField(max_length=255)
    quote = models.TextField()


class InterviewPicture(models.Model):
    interview = models.ForeignKey(Interview)
    picture = models.ForeignKey(Picture)
    is_selected = models.BooleanField()


# Product related
class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    amazon_url = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('product-detail', [self.slug])


class InterviewProduct(models.Model):
    interview = models.ForeignKey(Interview, related_name='products')
    product = models.ForeignKey(Product)
