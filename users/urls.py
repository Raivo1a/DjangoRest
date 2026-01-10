from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import PaymentListAPIView, UserCreateAPIView, UserListAPIView, ManageSubscriptionAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user-list"),
    path("payments/", PaymentListAPIView.as_view(), name="payments_list"),
    path("login/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh"),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path('subscription/', ManageSubscriptionAPIView.as_view(), name='manage_subscription'),
]
