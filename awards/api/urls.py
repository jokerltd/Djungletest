from django.urls import include, path
from rest_framework.routers import DefaultRouter
from awards.api import views

router=DefaultRouter()

urlpatterns = [
  path("awards/AwardsDetail/<int:pk>/", views.AwardsDetailView.as_view(), name="awards-details"),
  path("awards/AwardsDetail/", views.AwardsDetailView.as_view(), name="awards-details"),
  path("awards/AwardsList/", views.AwardsList.as_view(), name="awards-list"),
]