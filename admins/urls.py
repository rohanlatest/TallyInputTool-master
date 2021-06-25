from django.urls import path
from.import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('invoice_entry/', views.invoice_entry, name='invoice_entry'),
    path('view_unapprove_invoice/', views.view_unapprove_invoice, name='view_unapprove_invoice'),
    path('edit_unapprove_invoice/', views.edit_unapprove_invoice, name='edit_unapprove_invoice'),
    path('invoice_entry_approve/', views.invoice_entry_approve, name='invoice_entry_approve'),
    path('cash_entry/', views.cash_entry, name='cash_entry'),
    path('cash_entry_approve/', views.cash_entry_approve, name='cash_entry_approve'),
    path('syn_supplier/', views.syn_supplier, name='syn_supplier'),
    path('add_user/', views.add_user, name='add_user'),
    path('modify_user/', views.modify_user, name='modify_user'),
    path('approve/<int:id>/', views.approve, name='approve'),
]

