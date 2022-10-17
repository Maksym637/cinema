from django.contrib import admin
from django.urls import path
from app_user.views import index

from rest_framework.urlpatterns import format_suffix_patterns
from app_hall.views import HallView
from app_film.views import FilmView
from app_schedule.views import ScheduleView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='homepage'),

    # halls :
    path('hall/', HallView.as_view()),
    path('hall/<int:id>/', HallView.as_view()),

    # films :
    path('film/', FilmView.as_view()),
    path('film/<int:id>/', FilmView.as_view()),
    
    # schedules :
    path('schedule/', ScheduleView.as_view()),
    path('schedule/<int:id>/', ScheduleView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)