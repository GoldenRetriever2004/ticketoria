from django.contrib import admin

from .models import Category, Item, Ticket

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Ticket)