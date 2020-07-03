from django.db import models
from django.urls import reverse

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    address = models.CharField(max_length=256)

    def get_absolute_url(self):
        return reverse("cbv_app:detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    major = models.CharField(max_length=256)
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
