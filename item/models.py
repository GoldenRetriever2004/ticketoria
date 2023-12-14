from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_items')
    created_at = models.DateTimeField(auto_now_add=True)
    venue = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    item = models.ForeignKey(Item, related_name='tickets', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='tickets', on_delete=models.CASCADE, default=None, null=True)
    def __str__(self):
        return self.item.name

class Payment(models.Model):
    number = models.CharField(max_length=16)
    sec = models.CharField(max_length=3)
    valid = models.CharField(max_length=5)