# -*- coding: utf-8 -*-

from django.contrib import admin
from interviews.models import Question, InterviewTemplate, Interview
from interviews.models import QuestionOrder, Answer

# Inline
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 2

class QuestionOrderInline(admin.TabularInline):
    model = QuestionOrder
    extra = 2

# Admin
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'site')
    list_filter = ('site',)

class InterviewTemplateAdmin(admin.ModelAdmin):
    list_filter = ('site',)
    prepopulated_fields = {"slug": ("title",)}
    inlines = (QuestionOrderInline,)

class InterviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_on', 'is_published')
    list_filter = ('site', 'published_on', 'is_published')
    prepopulated_fields = {"slug": ("title",)}
    inlines = (AnswerInline,)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Interview, InterviewAdmin)
admin.site.register(InterviewTemplate, InterviewTemplateAdmin)

