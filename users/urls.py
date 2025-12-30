from django.urls import path

from users.views import UserListAPIView, PaymentListAPIView

app_name = "users"

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-list'),
    path('payments/', PaymentListAPIView.as_view(), name='payments_list'),
]
