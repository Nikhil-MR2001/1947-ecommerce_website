from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from item.models import Item, Category


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    # type_of =  models.ForeignKey(Category, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product.name