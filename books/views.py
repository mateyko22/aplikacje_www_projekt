from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):  # noqa: D101
    template_name = 'index.html'
