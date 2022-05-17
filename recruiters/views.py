from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from recruiters.models import Recruiter

# Create your views here.
class RecruiterListView(ListView):
	queryset = Recruiter.objects.filter(is_active=True)
	template_name = "app/pages/recruiter_list.html"

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['new_link'] = reverse_lazy('recruiters:recruiter_new')
		return context


class RecruiterDetailView(DetailView):
	queryset = Recruiter.objects.filter(is_active=True)
	template_name = "app/common/object_detail.html"


class RecruiterCreateView(CreateView):
	model = Recruiter
	template_name = "app/common/object_form.html"
	fields = "__all__"


class RecruiterUpdateView(UpdateView):
	model = Recruiter
	template_name = "app/common/object_form.html"
	fields = "__all__"


class RecruiterDeleteView(DeleteView):
	model = Recruiter
	template_name = 'app/common/confirm_delete.html'
	success_url = reverse_lazy('recruiters:recruiter_list')
