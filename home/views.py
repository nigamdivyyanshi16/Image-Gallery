from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def add_category(request):
    pass

def add_tag(request):
    pass

def upload_image(request):
    pass

def view_categories(request):
    categories= Category.objects.all()
    return render(request,"index.html",{"categories": categories})
    #jab categories mile toh index ko dena
    #ab isko return krna zrruri hai taaki ye function urls m kuch return krre


def view_tags(request):
    tags=Tag.objects.all()
    return render(request, 'tags.html', {'tags' : tags})

def view_images(request):
    images=Image.objects.all()
    return render(
        request, 'index.html',
        {'images':images}
        # index pr bhejdho  , kiss name se? images se .kisko?images ko
    )