from django.contrib import admin
from django.urls import path
from app_user.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='homepage')
]
