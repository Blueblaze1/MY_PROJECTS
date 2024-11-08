from django.contrib import admin
from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('text_to_decx/', text_to_decx),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)