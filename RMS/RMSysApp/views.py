from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from django.utils.timezone import now

from .models import MenuItem,Order,Inventory,Reservation
from .serializers import MenuItemSerializer, OrderSerializer

@api_view(['GET'])
def menu_list(request):
    items = MenuItem.objects.all()
    serializer = MenuItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def create_order(request):
    if request.method == 'GET':
        return Response({
            "message": "Use POST request to create orders"
        })

    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def daily_sales_report(request):

    today = now().date()

    orders = Order.objects.filter(
        created_at__date=today
    )

    total_sales = orders.aggregate(
        Sum('total_amount')
    )['total_amount__sum'] or 0

    total_orders = orders.count()

    return Response({
        "date": today,
        "total_orders": total_orders,
        "total_sales": total_sales
    })

@api_view(['GET'])
def low_stock_alert(request):

    low_stock_items = Inventory.objects.filter(
        quantity__lt=5
    )

    data = []

    for item in low_stock_items:
        data.append({
            "item_name": item.item_name,
            "quantity": item.quantity,
            "alert": "Low Stock"
        })

    return Response(data)

@api_view(['GET', 'POST'])
def reserve_table(request):

    if request.method == 'GET':
        return Response({
            "message": "Use POST request to reserve table"
        })

    serializer = ReservationSerializer(
        data=request.data
    )

    if serializer.is_valid():

        try:
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        except Exception as e:

            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )