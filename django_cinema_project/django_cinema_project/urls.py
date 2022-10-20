from django.contrib import admin
from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns
from app_hall.views import HallView
from app_seat.views import SeatView
from app_film.views import FilmView
from app_schedule.views import ScheduleView
from app_user.views import UserView
from app_booking.views import BookingView

urlpatterns = [
    path('admin/', admin.site.urls),

    # users :
    path('user/', UserView.as_view()),
    path('user/<str:username>/', UserView.as_view()),

    # seats :
    path('seat/', SeatView.as_view()),
    path('seat/<int:id>/', SeatView.as_view()),

    # halls :
    path('hall/', HallView.as_view()),
    path('hall/<int:id>/', HallView.as_view()),

    # films :
    path('film/', FilmView.as_view()),
    path('film/<int:id>/', FilmView.as_view()),

    # schedules :
    path('schedule/', ScheduleView.as_view()),
    path('schedule/<int:id>/', ScheduleView.as_view()),

    # bookings :
    path('booking/', BookingView.as_view()),
    path('booking/<int:id>/', BookingView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)