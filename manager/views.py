from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


def mdashboard(request):
    return render(request, 'mdashboard.html')


def minvoice_entry(request):
    return render(request, 'minvoice_entry.html')


def mview_unapprove_invoice(request):
    return render(request, 'mview_unapprove_invoice.html')


def medit_unapprove_invoice(request):
    return render(request, 'medit_unapprove_invoice.html')


def minvoice_entry_approve(request):
    return render(request, 'minvoice_entry_approve.html')


def mcash_entry(request):
    return render(request, 'mcash_entry.html')


def mcash_entry_approve(request):
    return render(request, 'mcash_entry_approve.html')


def msyn_supplier(request):
    return render(request, 'msyn_supplier.html')