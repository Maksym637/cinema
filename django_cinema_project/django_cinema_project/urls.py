from django.contrib import admin
from django.urls import path
from app_user.views import index

from rest_framework.urlpatterns import format_suffix_patterns
from app_hall.views import HallView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='homepage'),

    # halls :
    path('hall/', HallView.as_view()),
    path('hall/<int:id>/', HallView.as_view())

    # films :

    # schedules :
]

urlpatterns = format_suffix_patterns(urlpatterns)