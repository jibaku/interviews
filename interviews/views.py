from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.conf import settings
from django.http import Http404
from interviews.models import Interview, Person

class InterviewDetailView(DetailView):
    def get_queryset(self):
        queryset = Interview.objects.published()
        return queryset
    

class InterviewListView(ListView):
    paginate_by = 5
    
    def get_queryset(self):
        queryset = Interview.objects.published()
        if 'filter_key' in self.kwargs:
            if self.kwargs['filter_key'] in ['sexe']:
                if self.kwargs['filter_value'] == 'homme':
                    queryset = queryset.filter(person__sex=1)
                elif self.kwargs['filter_value'] == 'femme':
                    queryset = queryset.filter(person__sex=2)
                else:
                    raise Http404()
            else:
                raise Http404()
        return queryset

    def get_current_filter(self):
        current_filter = None
        queryset = self.get_queryset()
        if 'filter_key' in self.kwargs:
            if self.kwargs['filter_key'] in ['sexe']:
                if self.kwargs['filter_value'] == 'homme':
                    queryset = queryset.filter(person__sex=1)
                    current_filter = 'sexe'
                elif self.kwargs['filter_value'] == 'femme':
                    queryset = queryset.filter(person__sex=2)
                    current_filter = 'sexe'
        return current_filter

    def get_context_data(self, **kwargs):
        context = super(InterviewListView, self).get_context_data(**kwargs)
        context['filter'] = self.get_current_filter()
        context['total_interviews'] = Interview.objects.published().count()
        return context