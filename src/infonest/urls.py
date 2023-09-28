from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', admin.site.urls),
    path('index/', include('main.urls')),
    path('accounts/', include('allauth.urls')),
]
