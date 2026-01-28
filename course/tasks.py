from celery import shared_task
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from course.models import Course
from users.models import User, Subscription


@shared_task
def send_update_notification(course_pk):
    """Подписка на обновления курсов"""
    course = Course.objects.filter(pk=course_pk).first()
    users = User.objects.all()
    for user in users:
        subscription = Subscription.objects.filter(course=course_pk, user=user.pk).first()
        if subscription:
            send_mail(
                subject=f'Обновление курса "{course}"',
                message=f'Kypc "{course}", на который вы подписаны, обновлен',
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email],
            )
