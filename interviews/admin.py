# -*- coding: utf-8 -*-
from django.contrib import admin

from interviews.models import Interview, Answer

# Inline
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3

class InterviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_on', 'is_published')
    list_filter = ('site', 'published_on', 'is_published')
    prepopulated_fields = {"slug": ("title",)}
    inlines = (AnswerInline,)

admin.site.register(Interview, InterviewAdmin)
