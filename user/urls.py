from django.urls import path
from.import views

urlpatterns = [
    path('udashboard/', views.udashboard, name='udashboard'),
    path('uinvoice_entry/', views.uinvoice_entry, name='uinvoice_entry'),
    path('uview_unapprove_invoice/', views.uview_unapprove_invoice, name='uview_unapprove_invoice'),
    path('uedit_unapprove_invoice/', views.uedit_unapprove_invoice, name='uedit_unapprove_invoice'),
    path('ucash_entry/', views.ucash_entry, name='ucash_entry'),
    path('usyn_supplier/', views.usyn_supplier, name='usyn_supplier'),
]

