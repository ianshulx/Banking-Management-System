from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('transfer/',views.transfer, name='transfer'), 
    path('viewcustomers/',views.viewcustomers, name='viewcustomers'), 
    path('transhistory/',views.transhistory, name='transhistory'),
    path('customerdetails/<str:pk>/',views.customerdetails, name='customerdetails')
]
