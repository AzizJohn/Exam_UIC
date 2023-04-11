from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedModel
from apps.users.models import CustomUser


# Create your models here.



class Company(TimeStampedModel):
    name = models.CharField(max_length=100)
    about = models.TextField()


    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name

class Vacancy(TimeStampedModel):
    title = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"

    def __str__(self):
        return self.title



class Resume(TimeStampedModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="resume")
    file = models.FileField(verbose_name=_("file"), upload_to="resumes/%Y/%m/%d/")

    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resume"

    def __str__(self):
        return f"{self.user}'s file"