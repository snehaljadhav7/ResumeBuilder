from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from resume.models import ResumeItem
from resume.utils import Render
from django.shortcuts import render
from django.shortcuts import render_to_response
import django.template.loader

class HomePageView(TemplateView):
    template_name = 'home.html'
