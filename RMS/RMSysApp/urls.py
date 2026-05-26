from django.urls import path
from .views import menu_list, create_order,daily_sales_report,low_stock_alert,reserve_table

urlpatterns = [
    path('menu/', menu_list),
    path('orders/', create_order),
    path('reports/daily-sales/', daily_sales_report),
    path('reports/low-stock/', low_stock_alert),
    path('reservations/', reserve_table),
]