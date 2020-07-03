from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from . import models
from django.urls import reverse_lazy
# Create your views here.

"""
TemplateView Example:
"""


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['admin_input'] = "Admin wants to say Hello"
        return context


"""
ListView Example:
"""


class SchoolListView(ListView):
    # You can manually return a context like this:
    context_object_name = "schools"
    # Or this will covert the School model to become a tag named school_list
    model = models.School


"""
DetailView Example:
"""


class SchoolDetailView(DetailView):
    # You can manually return a context like this:
    context_object_name = "schools"
    id = "pk"
    # Or this will covert the School model to become a tag named school
    model = models.School
    template_name = 'cbv_app/school_detail.html'


"""
Schools creation
"""


class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'address')
    model = models.School


"""
Schools update
"""


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School


"""
School deletion
"""


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('cbv_app:list')