from django.db import models

# Create your models here.

class employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name