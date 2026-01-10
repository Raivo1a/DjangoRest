from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Course
from users.models import User, Subscription


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
        self.course = Course.objects.create(name="Test Course", owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscribe(self):
        url = reverse("users:manage_subscription")
        data = {
            "course_id": self.course.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(response.data.get("message"), "Подписка добавлена")

    def test_unsubscribe(self):
        Subscription.objects.create(user=self.user, course=self.course)
        url = reverse("users:manage_subscription")
        data = {
            "course_id": self.course.pk
        }
        self.assertTrue(
            Subscription.objects.filter(user=self.user, course=self.course).exists()
        )
        response = self.client.post(url, data)
        self.assertFalse(
            Subscription.objects.filter(user=self.user, course=self.course).exists()
        )
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(response.data.get("message"), "Подписка удалена")
