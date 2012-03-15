# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.conf import settings

class InterviewManager(models.Manager):
    def published(self):
        queryset = self.filter(site__id=settings.SITE_ID)
        queryset = queryset.filter(published_on__lte=datetime.datetime.now())
        queryset = queryset.filter(is_published=True)
        return queryset
