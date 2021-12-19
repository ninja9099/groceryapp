import uuid
import datetime

from django.contrib.auth import get_user_model
from django.db import models

from apps.common.base_model import BaseModel
from apps.grocery.constants import GroceryListStatus, ReminderInterval, GroceryItemStatus
from apps.grocery.functions import get_seven_days_from_now

User = get_user_model()


class GroceryList(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    user = models.ForeignKey(User, related_name='grocery_lists', on_delete=models.CASCADE)
    status= models.CharField(choices=GroceryListStatus.get_choices(),max_length=20)
    # field for the friendly reminder of completing it in 7 days after being created or on provided date
    due_date = models.DateTimeField(default=get_seven_days_from_now())
    reminder_interval = models.CharField(choices=ReminderInterval.get_choices(), max_length=10, default=ReminderInterval.Daily)

    class Meta:
        db_table = "ga_grocery_list"
        verbose_name = "Grocery List"
        order_with_respect_to = 'created_ts'

    def __str__(self):
        return f"{self.id}"


class GroceryItems(BaseModel):
    """
    Model for storing single item on grocery list
    """
    grocery_list = models.ForeignKey(GroceryList, on_delete=models.CASCADE, related_name="grocery_items")
    name = models.CharField(max_length=255)
    quantity = models.FloatField(default=1.)
    unit_of_measure = models.CharField(max_length=255)
    status = models.CharField(choices=GroceryItemStatus.get_choices(), default=GroceryItemStatus.Pending, max_length=20)

    class Meta:
        db_table = "ga_grocery_items"
        verbose_name = "Grocery Item"
        order_with_respect_to = 'created_ts'
        unique_together = ("grocery_list", "name")

    def __str__(self):
        return f"{self.name}"
