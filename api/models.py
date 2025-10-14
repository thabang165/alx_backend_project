from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(unique=True)
    rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="current_prices")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="store_prices")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    date_checked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.amount} {self.currency}"


class PriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="price_history")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="store_price_history")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    date_checked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.amount} {self.currency}"
