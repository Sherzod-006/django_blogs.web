from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog
# Create your views here.


class BlogListView(ListView):
    model = Blog
    template_name = 'home.html'  # Specify your template name here
    context_object_name = 'blogs'
