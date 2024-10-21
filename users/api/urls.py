from django.urls import path
from rest_framework.routers import DefaultRouter
from users.api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import CustomAuthToken

router=DefaultRouter()

urlpatterns = [
  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path("users/UsersDetail/<int:pk>/", views.UsersDetailView.as_view(), name="users-details"),
  path("users/UsersDetail/", views.UsersDetailView.as_view(), name="users-details"),
  path("users/UsersList/", views.UsersList.as_view(), name="users-list"),
  path("users/UserAwardsDetail/<int:pk>/", views.UserAwardsDetailView.as_view(), name="userawards-details"),
  path("users/UserAwardsDetail/", views.UserAwardsDetailView.as_view(), name="userawards-details"),
  path("users/UserAwardsList/", views.UserAwardsList.as_view(), name="userawards-list"),
  path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('users/api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
]
