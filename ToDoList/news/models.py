from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ---> {self.is_archived}"

