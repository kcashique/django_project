from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'app'

urlpatterns = [
    path('base.html', TemplateView.as_view(template_name="app/base.html")),
    path('', TemplateView.as_view(template_name="app/index.html")),
    path('index.html', TemplateView.as_view(template_name="app/index.html")),
    path('pages/charts/charts.html/', TemplateView.as_view(template_name="app/pages/charts/charts.html")),
    path('pages/forms/basic_elements.html/', TemplateView.as_view(template_name="app/pages/forms/basic_elements.html")),
    path('pages/icons/mdi.html/', TemplateView.as_view(template_name="app/pages/icons/mdi.html")),
    path('pages/samples/blank-page.html/', TemplateView.as_view(template_name="app/pages/samples/blank-page.html")),
    path('pages/samples/error-404.html/', TemplateView.as_view(template_name="error/error-404.html")),
    path('pages/samples/error-500.html/', TemplateView.as_view(template_name="error/error-500.html")),
    path('pages/samples/login.html/', TemplateView.as_view(template_name="registration/login.html")),
    path('pages/samples/register.html/', TemplateView.as_view(template_name="registration/register.html")),
    path('pages/tables/basic-table.html/', TemplateView.as_view(template_name="app/pages/tables/basic-table.html")),
    path('pages/ui-features/buttons.html/', TemplateView.as_view(template_name="app/pages/ui-features/buttons.html")),
    path('pages/ui-features/typography.html/', TemplateView.as_view(template_name="app/pages/ui-features/typography.html")),
]
