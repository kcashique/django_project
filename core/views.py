from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.http.response import HttpResponse
import json


class Index(TemplateView):
    template_name = "app/index.html"
