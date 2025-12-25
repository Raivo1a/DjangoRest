from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название курса", help_text="Введите название курса")
    description = models.TextField(
        max_length=100, blank=True, null=True, verbose_name="Описание", help_text="Введите описание"
    )
    image = models.ImageField(upload_to="products/photo", blank=True, null=True, help_text="Загрузите фото")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название урока", help_text="Введите название урока")
    description = models.TextField(
        max_length=100, blank=True, null=True, verbose_name="Описание", help_text="Введите описание"
    )
    image = models.ImageField(upload_to="course/photo", blank=True, null=True, help_text="Загрузите фото")
    link = models.URLField(blank=True, null=True, verbose_name="Ссылка на видео", help_text="Вставьте ссылку на видео")
    course = models.ForeignKey(
        Course, on_delete=models.SET_NULL, verbose_name="Курс", help_text="Выберите курс", blank=True, null=True
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.name
