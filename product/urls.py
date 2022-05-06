# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
from django.urls import path, include

from product import views

urlpatterns = [
    path('lastest-products/', views.LatestProductsList.as_view()),
]