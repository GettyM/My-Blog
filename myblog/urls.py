
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('registration.urls')),
]
