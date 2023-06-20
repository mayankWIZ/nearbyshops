from django.urls import path
from .views import home_view, shop_list, detail_view, update_view, delete_view

urlpatterns = [
    # Other URL patterns...
    path('shop_list/', shop_list),
    path('detail/<int:pk>', detail_view),
    path('update/<int:pk>', update_view),
    path('delete/<int:pk>', delete_view),
    path('', home_view),
]