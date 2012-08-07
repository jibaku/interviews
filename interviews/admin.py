# -*- coding: utf-8 -*-
from django.contrib import admin

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
    pass

admin.site.register(Person, PersonAdmin)

class InterviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_on', 'is_published')
    list_filter = ('site', 'published_on', 'is_published')
    prepopulated_fields = {"slug": ("title",)}
    inlines = (AnswerInline, InterviewPictureInline)

admin.site.register(Interview, InterviewAdmin)


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('author', 'quote')

admin.site.register(Quote, QuoteAdmin)

class PictureAdmin(admin.ModelAdmin):
    pass

admin.site.register(Picture, PictureAdmin)

class ProductAdmin(admin.ModelAdmin):
	pass

admin.site.register(Product, ProductAdmin)

class InterviewProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(InterviewProduct, InterviewProductAdmin)

