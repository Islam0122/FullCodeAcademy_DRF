from django.db import models

class Task(models.Model):
    class Status(models.TextChoices):
        CREATED = 'created',"Создано"
        IN_PROGRESS = "in_progress", "В работе"
        COMPLETED = "completed", "Завершено"
    title = models.CharField(
        max_length=255,
        verbose_name="Название задачи",
        help_text="Краткое название задачи (до 255 символов)"
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.CREATED,
        verbose_name="Статус задачи",
        help_text="Текущий статус задачи"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Время, когда задача была создана"
    )
    def __str__(self):
        return f"{self.title} ---> {self.status}"

