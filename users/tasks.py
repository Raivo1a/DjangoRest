from datetime import timezone, timedelta

from celery import shared_task

from users.models import User


@shared_task
def deactivate_users():
    """Отключение неактивных пользователей"""
    user = User.objects.all()
    for u in user:
        if timezone.now() - u.last_login > timedelta(days=30):
            u.is_active = False
            u.save()
