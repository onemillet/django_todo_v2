from django.db import models

# Create your models here.
class Todo(models.Model):
    status = models.BooleanField(default=False)
    content = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)