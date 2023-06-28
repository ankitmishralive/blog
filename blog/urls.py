from django.contrib import admin

from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from .views import home,post,category

urlpatterns = [  
    path('',home),
    path('blog/<slug:url>',post),
    path('category/<slug:url>',category)
    # path()
]