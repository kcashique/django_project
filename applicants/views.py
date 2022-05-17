from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from applicants.models import JobApplication, Applicant


class JobApplicationListView(ListView):
	queryset = JobApplication.objects.filter(is_active=True)
	template_name = "app/pages/jobapplication_list.html"

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['new_link'] = reverse_lazy('applicants:jobapplication_new')
		return context


class JobApplicationDetailView(DetailView):
	queryset = JobApplication.objects.filter(is_active=True)
	template_name = "app/common/object_detail.html"


class JobApplicationCreateView(CreateView):
	model = JobApplication
	template_name = "app/common/object_form.html"
	fields = "__all__"


class JobApplicationUpdateView(UpdateView):
	model = JobApplication
	template_name = "app/common/object_form.html"
	fields = "__all__"


class JobApplicationDeleteView(DeleteView):
	model = JobApplication
	template_name = 'app/common/confirm_delete.html'
	success_url = reverse_lazy('applicants:jobapplication_list')


class ApplicantListView(ListView):
	queryset = Applicant.objects.filter(is_active=True)
	template_name = "app/pages/applicant_list.html"

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['new_link'] = reverse_lazy('applicants:applicant_new')
		return context


class ApplicantDetailView(DetailView):
	queryset = Applicant.objects.filter(is_active=True)
	template_name = "app/common/object_detail.html"


class ApplicantCreateView(CreateView):
	model = Applicant
	template_name = "app/common/object_form.html"
	fields = "__all__"


class ApplicantUpdateView(UpdateView):
	model = Applicant
	template_name = "app/common/object_form.html"
	fields = "__all__"


class ApplicantDeleteView(DeleteView):
	model = Applicant
	template_name = 'app/common/confirm_delete.html'
	success_url = reverse_lazy('applicants:applicant_list')
