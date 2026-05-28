from rest_framework import serializers
from .models import MenuItem, Order, OrderItem, Inventory,Table,Reservation


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['menu_item', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, write_only=True)

    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'items', 'created_at', 'total_amount']

    def create(self, validated_data):
        items_data = validated_data.pop('items')

        order = Order.objects.create(**validated_data)

        total = 0

        for item_data in items_data:
            order_item = OrderItem.objects.create(
                order=order,
                **item_data
            )

            total += order_item.menu_item.price * order_item.quantity

            # Inventory Auto Update
            inventory_item = Inventory.objects.filter(
                item_name=order_item.menu_item.name
            ).first()

            if inventory_item:
                inventory_item.quantity -= order_item.quantity
                inventory_item.save()

        order.total_amount = total
        order.save()

        return order
    
class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = '__all__'

    def validate(self, data):

        table = data['table']

        if not table.is_available:
            raise serializers.ValidationError(
                "This table is not available."
            )

        return data