from django.urls import path
from calci import views
from django.urls import include

urlpatterns = [
    path('',views.bill_info),
    path('<int:pk>',views.particular_bill_info)
]