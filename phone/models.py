from django.db import models
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from shared.models import BaseModel

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'phone_category'


class Phones(BaseModel):
    BRAND_CHOICES = (
        ('APPLE', 'Apple'),
        ('SAMSUNG', 'Samsung'),
        ('XIAOMI', 'Xiaomi'),
        ('OPPO', 'Oppo'),
        ('REALME', 'Realme'),
    )

    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES, default='APPLE')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to='phones/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'JPG', 'PNG'])]
    )
    year = models.PositiveIntegerField(
        validators=[MinValueValidator(2000), MaxValueValidator(2026)]
    )
    desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        db_table = 'phones'
        ordering = ['-id']


class PhoneOrder(BaseModel):
    user = models.CharField(max_length=50)
    phone = models.ForeignKey(Phones, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.total_price = self.count * self.phone.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} | {self.phone.brand} {self.phone.model}"

    class Meta:
        db_table = 'phone_order'
        ordering = ['-id']
