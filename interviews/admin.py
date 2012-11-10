# -*- coding: utf-8 -*-
from django.contrib import admin
from django.core.urlresolvers import reverse

from interviews.models import Interview, Answer, Quote, Person
from interviews.models import Picture, Product, InterviewProduct, InterviewPicture

# Inline
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3

class InterviewPictureInline(admin.TabularInline):
    model = InterviewPicture
    extra = 4

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex')
    list_filter = ('sex',)

admin.site.register(Person, PersonAdmin)

class InterviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_on', 'is_published', 'preview_link')
    list_filter = ('site', 'published_on', 'is_published')
    prepopulated_fields = {"slug": ("title",)}
    inlines = (AnswerInline, InterviewPictureInline)

    def preview_link(self, obj):
      return '<a href="%s">Preview</a>' % (reverse('interviews-preview', args=[obj.preview_hash, obj.slug]),)
    preview_link.short_description = 'Preview'
    preview_link.allow_tags = True

admin.site.register(Interview, InterviewAdmin)


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('author', 'quote')

admin.site.register(Quote, QuoteAdmin)

class PictureAdmin(admin.ModelAdmin):
    list_display = ('image', 'interview', 'legend')
    list_filter = ('interview',)

admin.site.register(Picture, PictureAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'count', 'preview_link')

    def count(self, obj):
        return obj.interviewproduct_set.count()
    count.short_description = 'Interviews'

    def preview_link(self, obj):
      return '<a href="%s">Preview</a>' % (reverse('product-detail', args=[obj.slug]),)
    preview_link.short_description = 'Preview'
    preview_link.allow_tags = True

admin.site.register(Product, ProductAdmin)

class InterviewProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'interview')
    list_filter = ('product', 'interview')

admin.site.register(InterviewProduct, InterviewProductAdmin)

