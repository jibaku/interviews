# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone 
class InterviewManager(models.Manager):
    def published(self):
    	yougner_than = timezone.now()
        queryset = self.filter(site__id=settings.SITE_ID)
        queryset = queryset.filter(published_on__lte=yougner_than)
        queryset = queryset.filter(is_published=True)
        return queryset
