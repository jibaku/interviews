from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.conf import settings

from interviews.models import Interview

class InterviewDetailView(DetailView):
    queryset = Interview.objects.published()

class InterviewListView(ListView):
    paginate_by = 5
    queryset = Interview.objects.published()
