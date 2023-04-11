from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from sorl.thumbnail import ImageField

from apps.common.models import TimeStampedModel
from apps.users.models import CustomUser


class Service(TimeStampedModel):
    name = models.CharField(max_length=100)
    icon = ImageField(upload_to="services", null=True, blank=True, verbose_name=_("Icon"))
    avg_rating = models.FloatField(default=0)
    number_review = models.IntegerField(default=0)

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=100)
    icon = ImageField(upload_to="products", null=True, blank=True, verbose_name=_("Icon"))
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.PositiveIntegerField([MaxValueValidator(100)])

    @property
    def final_price(self):
        return self.original_price * (100 - self.discount) / 100

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("products")

    def __str__(self):
        return self.name


class Review(TimeStampedModel):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_text = models.CharField(max_length=200, null=True)
    review_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")

    def __str__(self):
        return str(self.rating) + " | " + self.service.name + " | " + str(self.review_user)
