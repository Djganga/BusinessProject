from django.urls import path

from django.urls import include

from api import views

urlpatterns = [
    path('',views.ProductList.as_view()),
    path('<int:pk>',views.ParticularProduct.as_view())

]
