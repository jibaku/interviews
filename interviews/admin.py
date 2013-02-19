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


class InterviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'published_on', 'is_published', 'preview_link')
    list_filter = ('site', 'published_on', 'is_published')
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = 'published_on'
    ordering = ('is_published', '-published_on')
    search_fields = ['title', 'description']
    inlines = (AnswerInline, InterviewPictureInline)

    def preview_link(self, obj):
        preview_url = reverse('interviews-preview', args=[obj.preview_hash, obj.slug])
        return '<a href="%s">Preview</a>' % (preview_url,)
    preview_link.short_description = 'Preview'
    preview_link.allow_tags = True


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('author', 'quote')


class PictureAdmin(admin.ModelAdmin):
    list_display = ('image', 'interview', 'legend')
    list_filter = ('interview',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'count', 'preview_link')
    prepopulated_fields = {"slug": ("title",)}

    def count(self, obj):
        return obj.interviewproduct_set.count()
    count.short_description = 'Interviews'

    def preview_link(self, obj):
        product_preview_url = reverse('product-detail', args=[obj.slug])
        return '<a href="%s">Preview</a>' % (product_preview_url,)
    preview_link.short_description = 'Preview'
    preview_link.allow_tags = True


class InterviewProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'interview')
    list_filter = ('product', 'interview')

admin.site.register(Person, PersonAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Interview, InterviewAdmin)
admin.site.register(InterviewProduct, InterviewProductAdmin)
admin.site.register(Product, ProductAdmin)
