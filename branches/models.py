from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    restaurant = models.ForeignKey(
        Restaurant,
        related_name="employees",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    avatar = models.ImageField(upload_to="employees", null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
