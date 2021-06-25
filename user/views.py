from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.



def udashboard(request):
    return render(request, 'udashboard.html')


def uinvoice_entry(request):
    return render(request, 'uinvoice_entry.html')


def uview_unapprove_invoice(request):
    return render(request, 'uview_unapprove_invoice.html')


def uedit_unapprove_invoice(request):
    return render(request, 'uedit_unapprove_invoice.html')


def ucash_entry(request):
    return render(request, 'ucash_entry.html')


def usyn_supplier(request):
    return render(request, 'usyn_supplier.html')