from django.urls import path
from . import views

urlpatterns = [
    path('', views.insertdata, name='insertdata'),
    path('data/', views.displaydata, name='displaydata'),
    path('data/deletedata/<int:id>/', views.deletedata, name='deletedata'),
    path('data/updatedata/<int:id>', views.updatedata, name='updatedata'),
    path('data/updatedata/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('data/export/', views.export, name='export')
]