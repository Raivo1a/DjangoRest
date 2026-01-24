from django.contrib.auth.models import AbstractUser
from django.db import models

from course.models import Course


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")

    phone = models.CharField(
        max_length=35, verbose_name="Телефон", blank=True, null=True, help_text="Введите номер телефона"
    )
    tg_name = models.CharField(
        max_length=50, verbose_name="Ник телеграм", blank=True, null=True, help_text="Введите ник в телеграмме"
    )
    avatar = models.ImageField(
        upload_to="users/avatars/", verbose_name="Аватар", blank=True, null=True, help_text="Загрузите свой аватар"
    )
    country = models.CharField(
        max_length=30, verbose_name="Страна", blank=True, null=True, help_text="Введите вашу страну"
    )
    city = models.CharField(max_length=30, verbose_name="Город", blank=True, null=True, help_text="Введите ваш город")

    token = models.CharField(max_length=100, verbose_name="Токен", blank=True, null=True)
    last_login = models.DateField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    payment_methods = [("transfer", "Перевод на счет"), ("cash", "Наличные"), ("card", "Карта")]
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, verbose_name="Пользователь", related_name="payments", blank=True, null=True
    )
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата оплаты")
    course = models.ForeignKey(
        "course.Course", on_delete=models.SET_NULL, verbose_name="Оплаченный курс", blank=True, null=True
    )
    lesson = models.ForeignKey(
        "course.Lesson", on_delete=models.SET_NULL, verbose_name="Оплаченный урок", blank=True, null=True
    )
    total_sum = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Сумма оплаты"
    )
    payment_type = models.CharField(choices=payment_methods, blank=True, null=True, verbose_name="Способ оплаты")
    session_id = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Id сессии", help_text="Укажите Id сессии"
    )
    link = models.URLField(
        max_length=1000, blank=True, null=True, verbose_name="Ссылка на оплату", help_text="Укажите ссылку на оплату"
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return self.user


class Subscription(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name="Курс", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

    def __str__(self):
        return self.user
