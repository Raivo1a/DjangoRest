from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()


class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('lesson', 'course', 'payment_type',)
    ordering_fields = ['payment_date',]


class PaymentCreateAPIView(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
