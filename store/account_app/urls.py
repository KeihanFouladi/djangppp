from django.urls import path
from . import views

urlpatterns = [
    #path('',views.user_register)
    path('register/',views.user_register)
]
