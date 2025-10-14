from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=50, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=100, unique=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='prices')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='ZAR')
    date_checked = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        # Save price
        super().save(*args, **kwargs)
        # Auto-log to PriceHistory
        PriceHistory.objects.create(
            product=self.product,
            store=self.store,
            amount=self.amount,
            currency=self.currency,
            date_checked=self.date_checked
        )

    def __str__(self):
        return f"{self.product.name} - {self.amount} {self.currency}"

class PriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='price_history')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='price_history')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    date_checked = models.DateTimeField()

    def __str__(self):
        return f"{self.product.name} at {self.store.name} - {self.amount} {self.currency}"

