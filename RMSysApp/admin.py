from django.contrib import admin
from .models import MenuItem, Order, OrderItem,Inventory,Table,Reservation

admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Inventory)
admin.site.register(Table)
admin.site.register(Reservation)