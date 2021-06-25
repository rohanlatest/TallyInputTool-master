from django.urls import path
from.import views

urlpatterns = [
    path('mdashboard/', views.mdashboard, name='mdashboard'),
    path('minvoice_entry/', views.minvoice_entry, name='minvoice_entry'),
    path('mview_unapprove_invoice/', views.mview_unapprove_invoice, name='mview_unapprove_invoice'),
    path('medit_unapprove_invoice/', views.medit_unapprove_invoice, name='medit_unapprove_invoice'),
    path('minvoice_entry_approve/', views.minvoice_entry_approve, name='minvoice_entry_approve'),
    path('mcash_entry/', views.mcash_entry, name='mcash_entry'),
    path('mcash_entry_approve/', views.mcash_entry_approve, name='mcash_entry_approve'),
    path('msyn_supplier/', views.msyn_supplier, name='msyn_supplier'),
]

