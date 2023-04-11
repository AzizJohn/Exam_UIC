from django.db import models

from apps.common.models import TimeStampedModel
from apps.users.models import CustomUser


class Company(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Mark(TimeStampedModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="mark")
    mark_name = models.CharField(max_length=100)

    def __str__(self):
        return self.mark_name


class Car(TimeStampedModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company")
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, related_name="mark")
    price = models.DecimalField(max_digits=9, decimal_places=2)
    user = models.ForeignKey(
        CustomUser, models.CASCADE, related_name='cars'
    )

    def __str__(self):
        return self.price