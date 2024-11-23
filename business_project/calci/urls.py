from django.urls import path
from calci import views
from django.urls import include

urlpatterns = [
    path('',views.bill_info),
    path('<int:pk>',views.particular_bill_info),
    path('transactions/day/<str:pk>',views.particular_day_transactions),
    path('collections/day/<str:pk>',views.particular_day_collections),
]
