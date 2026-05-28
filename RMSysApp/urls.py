from django.urls import path
from .views import (
    home,
    signup_view,
    login_view,
    logout_view,
    menu_page,
    reservation_page,
    reserve_table,
    cart_view,
    add_to_cart,
    clear_cart,
    checkout_cart,
    create_order_from_menu,
    order_detail,
    daily_sales_report,
    low_stock_alert,
)

urlpatterns = [

    # AUTH
    path('', login_view, name='root'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),

    # HOME
    path('home/', home, name='home'),

    # MENU
    path('menu-page/', menu_page, name='menu_page'),

    # RESERVATION
    path('reservation-page/', reservation_page, name='reservation_page'),
    path('reservations/', reserve_table, name='reserve_table'),

    # CART
    path('cart/', cart_view, name='cart'),
    path('add-to-cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('clear-cart/', clear_cart, name='clear_cart'),
    path('checkout/', checkout_cart, name='checkout_cart'),

    # ORDER
    path('create-order/<int:item_id>/', create_order_from_menu, name='create_order'),
    path('orders/<int:order_id>/', order_detail, name='order_detail'),

    # REPORTS
    path('reports/daily-sales/', daily_sales_report, name='daily_sales'),
    path('reports/low-stock/', low_stock_alert, name='low_stock'),
]