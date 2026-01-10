from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from course.models import Course
from users.models import Payment, User, Subscription


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class SubscriptionSerializer(ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        course = obj.course
        return Subscription.objects.filter(user=user, course=course).exists()
