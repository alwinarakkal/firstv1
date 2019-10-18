from django.urls import path,include
from django.conf.urls import include, url   
from . import views

urlpatterns = [
            path("register", views.register, name="register"),
            path("index", views.index, name="index"),
            path('',views.index,name="index "),

            path('update',views.edit,name="update"),
            path('profile',views.profile,name="profile "),

            url('', include('django.contrib.auth.urls')),
]
              
          

