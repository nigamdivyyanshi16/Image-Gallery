"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import view_categories, view_tags , view_images
#home.views ek folder hai jismein views_categories krke ek function hai
from django.conf import settings
from django.conf.urls.static import static
# the above two commands are used only when we deal with loading of images
urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories',view_categories,name="categories"),
    path('tags', view_tags, name="tags"),
    path('', view_images, name="images"),
    # url parameters name act as links in base.html
]
# in django we are enabling a permission in our website, so django block randoms urls(like here of images) so we import predefined functions or variables to 
# to import and then urls are valid django displays it
urlpatterns+=static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
