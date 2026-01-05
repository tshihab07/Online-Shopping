from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name


# Record Items
class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Items"

    def __str__(self):
        return self.name