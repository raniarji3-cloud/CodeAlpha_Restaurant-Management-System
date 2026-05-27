from django.db import models
from django.core.exceptions import ValidationError

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=50)
    image = models.URLField(blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
      
class Order(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Preparing', 'Preparing'),
        ('Ready', 'Ready'),
        ('Delivered', 'Delivered'),
    ]

    customer_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def __str__(self):
        return self.customer_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.menu_item.price * self.quantity

class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.item_name

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number}"

class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)

    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE
    )

    reservation_time = models.DateTimeField()

    def clean(self):
        if not self.table.is_available:
            raise ValidationError(
                "This table is not available."
            )

        existing_reservation = Reservation.objects.filter(
            table=self.table,
            reservation_time=self.reservation_time
        ).exclude(id=self.id)

        if existing_reservation.exists():
            raise ValidationError(
                "This table is already reserved for this time."
            )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer_name} - Table {self.table.table_number}"