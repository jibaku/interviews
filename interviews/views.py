from django.views.generic.list_detail import object_detail, object_list
from interviews.models import Interview
from django.conf import settings

def interview_detail(request, interview_slug):
    queryset = Interview.objects.published()
    return object_detail(request, queryset=queryset, slug=interview_slug, slug_field='slug')

def interview_list(request):
    queryset = Interview.objects.published()
    return object_list(request, queryset=queryset)