from django.urls import path
from . import views

urlpatterns = [
    path("", views.workshop_list, name="workshop_list"),
    path("detail/<int:id>", views.workshop_detail, name="workshop_detail"),
    path("member", views.member_list, name="member_list"),
    
]