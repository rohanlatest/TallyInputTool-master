from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from . import models
from .models import Invoice_Model, Invoice
from .form import InvoiceFormset, InvoiceModelForm
# Create your views here.


def dashboard(request):
    return render(request, 'dashboard.html')



def invoice_entry(request):

    user = request.user
    template_name = 'ainvoice_entry.html'

    if request.method == 'GET':
        purchaseform = InvoiceModelForm(request.GET or None)
        formset = InvoiceFormset(queryset=Invoice.objects.none())
    elif request.method == 'POST':
        purchaseform = InvoiceModelForm(request.POST, request.FILES)
        formset = InvoiceFormset(request.POST, request.FILES)
        if purchaseform.is_valid() and formset.is_valid():
            invo = purchaseform.save(commit=False)
            invo.user = request.user
            invo.status = 'Pending'
            invo.save()
            for form in formset:
                # so that `purchase` instance can be attached.
                particular = form.save(commit=False)
                particular.invoice = invo
                particular.save()
            return redirect('view_unapprove_invoice')
    return render(request, template_name, {'bookform': purchaseform, 'formset': formset})


def view_unapprove_invoice(request):
    info = models.Invoice_Model.objects.all()
    return render(request, 'view_unapprove_invoice.html',{'info':info})


def edit_unapprove_invoice(request):
    return render(request, 'edit_unapprove_invoice.html')


def invoice_entry_approve(request):
    info = models.Invoice_Model.objects.all()
    return render(request, 'invoice_entry_approve.html',{'info':info})


def cash_entry(request):
    return render(request, 'cash_entry.html')


def cash_entry_approve(request):
    return render(request, 'cash_entry_approve.html')


def syn_supplier(request):
    return render(request, 'syn_supplier.html')


def add_user(request):
    return render(request, 'add_user.html')


def modify_user(request):
    return render(request, 'modify_user.html')

def approve(request, id):
    form1 = Invoice_Model.objects.get(pk=id)
    form1.status = 'Approve'
    form1.save()
    return redirect('invoice_entry_approve')