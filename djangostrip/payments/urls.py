from django.contrib import admin
from django.urls import include, path

from payments.views import CancelPageView, SuccessPageView, home

urlpatterns = [
    # path('', HomePageView.as_view(), name='home'),
    path('', home, name='home'),
    path('success/', SuccessPageView.as_view(), name='success'),
    path('cancel/', CancelPageView.as_view(), name='cancel'),
]