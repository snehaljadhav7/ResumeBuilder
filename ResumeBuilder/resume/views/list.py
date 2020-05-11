from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from resume.models import ResumeItem
from resume.utils import Render
from django.shortcuts import render
from django.shortcuts import render_to_response
import django.template.loader

class ListPageView(ListView):
    template_name = 'list.html'

    def get_queryset(self):
        # return ResumeItem.objects.all()
        return ResumeItem.objects.order_by('First_Name', 'Last_Name')

    def pdf(self, resume_id):
        resumeItem= ResumeItem.objects.get(id=resume_id)
        info = { 'resumeItem':resumeItem}
        return Render.render_to_response('pdf.html', info)
