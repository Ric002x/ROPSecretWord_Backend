from django.urls import path

from words import views

urlpatterns = [
    path('validate/<str:word>', views.VerifyWord.as_view()),
    path('', views.TodaysWord.as_view()),
]
