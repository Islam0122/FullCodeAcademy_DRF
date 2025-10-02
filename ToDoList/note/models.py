from django.db import models

class Note(models.Model):
     title = models.CharField(max_length=100)
     note = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)

     class Meta:
         ordering = ['-created_at']


