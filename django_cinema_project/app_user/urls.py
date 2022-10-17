from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.post_user),
    path('user/<str:username>', views.user_details)
]