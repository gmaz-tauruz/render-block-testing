from django.urls import path

from . import views

app_name = __package__

urlpatterns = [
    path('', views.voucher_list, name='voucher_list'),
     path('', views.voucher_list_viaTemplateResponse, name='voucher_list_viaTemplateResponse')
]