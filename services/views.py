from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from services.models import Service, Category


class CategoryListView(ListView):
	queryset = Category.objects.filter(is_active=True)
	template_name = "app/pages/category_list.html"

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['new_link'] = reverse_lazy('services:category_new')
		return context


class CategoryDetailView(DetailView):
	queryset = Category.objects.filter(is_active=True)
	template_name = "app/common/object_detail.html"


class CategoryCreateView(CreateView):
	model = Category
	template_name = "app/common/object_form.html"
	fields = "__all__"


class CategoryUpdateView(UpdateView):
	model = Category
	template_name = "app/common/object_form.html"
	fields = "__all__"


class CategoryDeleteView(DeleteView):
	model = Category
	template_name = 'app/common/confirm_delete.html'
	success_url = reverse_lazy('services:category_list')


class ServiceListView(ListView):
	queryset = Service.objects.filter(is_active=True)
	template_name = "app/pages/service_list.html"

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['new_link'] = reverse_lazy('services:service_new')
		return context


class ServiceDetailView(DetailView):
	queryset = Service.objects.filter(is_active=True)
	template_name = "app/common/object_detail.html"


class ServiceCreateView(CreateView):
	model = Service
	template_name = "app/common/object_form.html"
	fields = "__all__"


class ServiceUpdateView(UpdateView):
	model = Service
	template_name = "app/common/object_form.html"
	fields = "__all__"


class ServiceDeleteView(DeleteView):
	model = Service
	template_name = 'app/common/confirm_delete.html'
	success_url = reverse_lazy('services:service_list')
