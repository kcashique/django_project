from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from jobs.models import Job, Skill

class JobListView(ListView):
	queryset = Job.objects.filter(is_active=True)
	template_name = "app/pages/job_list.html"

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['new_link'] = reverse_lazy('jobs:job_new')
		return context


class JobDetailView(DetailView):
	queryset = Job.objects.filter(is_active=True)
	template_name = "app/common/object_detail.html"


class JobCreateView(CreateView):
	model = Job
	template_name = "app/common/object_form.html"
	fields = "__all__"


class JobUpdateView(UpdateView):
	model = Job
	template_name = "app/common/object_form.html"
	fields = "__all__"


class JobDeleteView(DeleteView):
	model = Job
	template_name = 'app/common/confirm_delete.html'
	success_url = reverse_lazy('services:job_list')


class SkillListView(ListView):
	queryset = Skill.objects.filter(is_active=True)
	template_name = "app/pages/skill_list.html"

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['new_link'] = reverse_lazy('jobs:skill_new')
		return context


class SkillDetailView(DetailView):
	queryset = Skill.objects.filter(is_active=True)
	template_name = "app/common/object_detail.html"


class SkillCreateView(CreateView):
	model = Skill
	template_name = "app/common/object_form.html"
	fields = "__all__"


class SkillUpdateView(UpdateView):
	model = Skill
	template_name = "app/common/object_form.html"
	fields = "__all__"


class SkillDeleteView(DeleteView):
	model = Skill
	template_name = 'app/common/confirm_delete.html'
	success_url = reverse_lazy('jobs:skill_list')
