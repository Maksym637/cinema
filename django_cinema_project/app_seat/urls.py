from django.urls import path
from . import views

urlpatterns = [
    path('seats/', views.get_post_seat),
    path('seats/<int:pk>', views.delete_seat_by_id)
]
