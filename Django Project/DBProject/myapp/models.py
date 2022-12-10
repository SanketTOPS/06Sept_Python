from django.db import models

# Create your models here.

class studinfo(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    dob=models.DateField()
    address=models.TextField()

    def __str__(self) -> str:
        return self.name