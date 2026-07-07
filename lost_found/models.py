from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

from django.conf import settings
# Create your models here.

ctg = [('Dev', 'DEVICES (Phone, Laptop, Tablet, Headphones)'),
              ('Doc', 'DOCUMENTS (IDs, Student Cards, Passports, Notebooks)'),
              ('Acc', 'ACCESSORIES (Keys, Wallets, Bags, Umbrellas)'),
              ('Clo', 'CLOTHING (Jackets, Hats, Gloves, Footwear)'),
              ('Sta', 'STATIONERY (Pens, Calculators, Art Supplies)'),
              ('Oth', 'OTHER (Water Bottles, Sports Gear, Miscellaneous)')]

stat = [('L', 'LOST ITEM'),
          ('F', 'FOUND ITEM'),
          ('C', 'CLAIMED')]


class Item(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()

    catagories = models.CharField(
        max_length=3,
        choices=ctg,
        default='Oth'
    )

    status= models.CharField(
        max_length=3,
        choices=stat,
        default="L"
    )

    image = models.ImageField(upload_to="lostitems/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    claimed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='claimed_items')
