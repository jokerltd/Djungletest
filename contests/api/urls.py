from django.urls import include, path
from rest_framework.routers import DefaultRouter
from contests.api import views

router=DefaultRouter()

urlpatterns = [
  path('play/', views.PlayView.as_view(), name='play'),
  path("contests/ContestsDetail/<int:pk>/", views.ContestsDetailView.as_view(), name="contests-details"),
  path("contests/ContestsDetail/", views.ContestsDetailView.as_view(), name="contests-details"),
  path("contests/ContestsList/", views.ContestsList.as_view(), name="contests-list"),
]