from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('jobs/', views.JobsList.as_view()),
    path('jobs/<int:pk>/', views.JobsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
