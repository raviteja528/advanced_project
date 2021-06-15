from django.shortcuts import render
# from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,UpdateView,
                                DeleteView)
# from django.http import HttpResponse
from . import models


# Create your views here.
# def index(request):
#     return render(request,'index.html')

# class CBView(View):
#     def get(self,request):
#         return HttpResponse("CLASS BASED VIEWS ARE COOL!")

class IndexView(TemplateView):
    template_name = 'index.html'
#
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = 'BASIC INJECTION'
#         return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    # school_list

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    #school
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
