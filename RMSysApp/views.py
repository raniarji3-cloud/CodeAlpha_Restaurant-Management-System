from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Sum
from django.utils.timezone import now
from django.shortcuts import render, get_object_or_404, redirect

from .models import MenuItem, Order, OrderItem, Inventory, Reservation
from .serializers import MenuItemSerializer, OrderSerializer, ReservationSerializer

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# =========================
# 🔵 API: MENU LIST
# =========================
@api_view(['GET'])
def menu_list(request):
    items = MenuItem.objects.all()
    serializer = MenuItemSerializer(items, many=True)
    return Response(serializer.data)


# =========================
# 🔵 API: CREATE ORDER (POSTMAN / DRF)
# =========================
@api_view(['GET', 'POST'])
def create_order(request):
    if request.method == 'GET':
        return Response({"message": "Use POST request to create orders"})

    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# =========================
# 🔵 API: DAILY SALES REPORT
# =========================
@api_view(['GET'])
def daily_sales_report(request):
    today = now().date()

    orders = Order.objects.filter(created_at__date=today)

    total_sales = orders.aggregate(
        Sum('total_amount')
    )['total_amount__sum'] or 0

    return Response({
        "date": today,
        "total_orders": orders.count(),
        "total_sales": total_sales
    })


# =========================
# 🔵 API: LOW STOCK
# =========================
@api_view(['GET'])
def low_stock_alert(request):
    items = Inventory.objects.filter(quantity__lt=5)

    data = [
        {
            "item_name": i.item_name,
            "quantity": i.quantity,
            "alert": "Low Stock"
        }
        for i in items
    ]

    return Response(data)


# =========================
# 🔵 API: RESERVATION
# =========================
@api_view(['GET', 'POST'])
def reserve_table(request):

    if request.method == 'GET':
        return Response({"message": "Use POST request to reserve table"})

    serializer = ReservationSerializer(data=request.data)

    if serializer.is_valid():
        try:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# =========================
# 🟡 HTML: CREATE ORDER FROM MENU (LOGIN REQUIRED)
# =========================
@login_required(login_url='/login/')
def create_order_from_menu(request, item_id):

    item = get_object_or_404(MenuItem, id=item_id)

    quantity = int(request.POST.get('quantity', 1))

    order = Order.objects.create(
        customer_name=request.user.username,
        total_amount=0
    )

    order_item = OrderItem.objects.create(
        order=order,
        menu_item=item,
        quantity=quantity
    )

    total = order_item.menu_item.price * quantity

    order.total_amount = total

    order.save()

    return redirect(f'/orders/{order.id}/')

# =========================
# 🟡 HTML: HOME PAGE
# =========================
@login_required(login_url='/login/')
def home(request):
    return render(request, 'RMSysApp/home.html')


# =========================
# 🟡 HTML: MENU PAGE
# =========================
@login_required(login_url='/login/')
def menu_page(request):
    items = MenuItem.objects.all()
    return render(request, 'RMSysApp/menu.html', {'items': items})


# =========================
# 🟡 HTML: RESERVATION PAGE
# =========================
@login_required(login_url='/login/')
def reservation_page(request):
    return render(request, 'RMSysApp/reservation.html')


# =========================
# 🟡 HTML: ORDER DETAIL PAGE
# =========================
@login_required(login_url='/login/')
def order_detail(request, order_id):

    order = get_object_or_404(Order, id=order_id)
    items = order.orderitem_set.all()

    return render(request, 'RMSysApp/order.html', {
        'order': order,
        'items': items
    })
# =========================
# 🛒 ADD TO CART
# =========================
@login_required(login_url='/login/')
def add_to_cart(request, item_id):

    item = get_object_or_404(MenuItem, id=item_id)

    cart = request.session.get('cart', {})

    item_id_str = str(item_id)

    if item_id_str in cart:
        cart[item_id_str] += 1
    else:
        cart[item_id_str] = 1

    request.session['cart'] = cart

    return redirect('/cart/')

# =========================
# 🛒 VIEW CART
# =========================
@login_required(login_url='/login/')
def cart_view(request):

    cart = request.session.get('cart', {})

    items = []
    total = 0

    for item_id, qty in cart.items():
        item = MenuItem.objects.get(id=item_id)

        item_total = item.price * qty
        total += item_total

        items.append({
            'item': item,
            'qty': qty,
            'total': item_total
        })

    return render(request, 'RMSysApp/cart.html', {
        'items': items,
        'total': total
    })
    
# =========================
# 🧹 CLEAR CART
# =========================
@login_required(login_url='/login/')
def clear_cart(request):
    request.session['cart'] = {}
    return redirect('/cart/')

# =========================
# ✅ CHECKOUT CART → CREATE ORDER
# =========================
@login_required(login_url='/login/')
def checkout_cart(request):

    cart = request.session.get('cart', {})

    if not cart:
        return redirect('/cart/')

    order = Order.objects.create(
        customer_name=request.user.username,
        total_amount=0
    )

    total = 0

    for item_id, qty in cart.items():
        item = MenuItem.objects.get(id=item_id)

        OrderItem.objects.create(
            order=order,
            menu_item=item,
            quantity=qty
        )

        total += item.price * qty

    order.total_amount = total
    order.save()

    request.session['cart'] = {}

    return redirect(f'/orders/{order.id}/')


# =========================
# SIGNUP
# =========================
def signup_view(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'RMSysApp/signup.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)
        return redirect('/home/')

    return render(request, 'RMSysApp/signup.html')

# =========================
# LOGIN
# =========================
def login_view(request):

    if request.user.is_authenticated:
        return redirect('/home/')

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('/home/')

        else:

            return render(
                request,
                'RMSysApp/login.html',
                {
                    'error': 'Invalid username or password'
                }
            )

    return render(request, 'RMSysApp/login.html')
# =========================
# LOGOUT
# =========================
def logout_view(request):
    logout(request)
    return redirect('/login/')
