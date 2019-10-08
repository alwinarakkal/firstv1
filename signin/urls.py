from django.urls import path,include
from . import views
urlpatterns = [
            path("register", views.register, name="register"),
            path("index", views.index, name="index"),
            path('',views.index,name="index "),

            path('update',views.edit,name="update "),
            
            
          
]
