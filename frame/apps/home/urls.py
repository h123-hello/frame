from django.urls import path

from frame.apps.home import views

urlpatterns = [
    path("banner/", views.BannerListAPIView.as_view()),
]
