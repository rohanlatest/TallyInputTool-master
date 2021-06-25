from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import modelformset_factory
from .models import Invoice_Model, Invoice



gst_choices = [('0', 0),('5', 5), ('6', 6), ('14', 14), ('18', 18), ('28', 28)]
state = [('Maharashtra','Maharashtra'),('Gujrat','Gujrat'),('Madhya Pradesh','Madhya Pradesh'),('New Delhi','New Delhi')]
invoice_choices = [('Production Purchase', 'Production Purchase'), ('Office/OH Purchase ', 'Office/OH Purchase'), ('Asset Purchase', 'Asset Purchase'), ('Other', 'Other')]
vendor_choices = [('Production Purchase', 'Production Purchase'), ('Office/OH Purchase ', 'Office/OH Purchase'), ('Asset Purchase', 'Asset Purchase'), ('Other', 'Other')]
pro_choices = [('Production Purchase', 'Production Purchase'), ('Office/OH Purchase ', 'Office/OH Purchase'), ('Asset Purchase', 'Asset Purchase'), ('Other', 'Other')]
po_choices = [('1', '1'),('2','2'),('3','3'),('4','4')]


class InvoiceModelForm(forms.ModelForm):

    class Meta:
        model = Invoice_Model
        fields = ('supplier_invoice_no','total_gst','supplier_name','invoice_id','supplier_state','supplier_invoice_date','total_amount','total_igst','grand_total','total_sgst','total_cgst','naration',)
        widgets = {
            'supplier_invoice_no': forms.TextInput(attrs={
                'class': 'form-control round-form',
                'placeholder': 'Enter Supplier Invoice No here',
            }),
            'supplier_name': forms.TextInput(attrs={
                'class': 'form-control round-form',
                'placeholder': 'Enter Supplier Name here'
            }),
            'invoice_id': forms.NumberInput(attrs={
                'class': 'form-control round-form',
                'placeholder': 'Enter Invoice Id here'
            }),
            'supplier_state': forms.Select(choices=state,attrs={
                'class': 'form-control round-form',
                'placeholder': 'Enter Supplier State here'
            }),

            'total_amount': forms.NumberInput(attrs={
                'class': 'form-control round-form',
                'placeholder': '  Total Amount ',
                'readonly': True
            }),
            'total_igst': forms.NumberInput(attrs={
                'class': 'form-control round-form',
                'placeholder': ' Total IGST ',
                'readonly': True
            }),
            'total_sgst': forms.NumberInput(attrs={
                'class': 'form-control round-form',
                'placeholder': ' Total SGST ',
                'readonly': True
            }),
            'total_cgst': forms.NumberInput(attrs={
                'class': 'form-control round-form',
                'placeholder': ' Total CGST ',
                'readonly': True
            }),
            'naration': forms.TextInput(attrs={
                'class': 'form-control round-form',
                'placeholder': 'Your naration'
            }),

            'total_gst': forms.NumberInput(attrs={
                'class': 'form-control round-form',
                'placeholder': 'Enter GST here',
                'readonly': True

            }),
            'grand_total': forms.NumberInput(attrs={
                'class': 'form-control round-form',
                'placeholder': 'Grand Total',
                'readonly': True
            }),
            'supplier_invoice_date': forms.DateTimeInput(format='%d-%m-%Y', attrs={
                'class': 'form-control round-form',
                'placeholder': 'Enter Supplier Invoice Date here',
                'type': 'date'

            }),

        }


InvoiceFormset = modelformset_factory(
    Invoice,
    fields=('description','amount','igst','sgst','cgst','quantity','total','gst'),
    extra=1,
    widgets={'description': forms.TextInput(attrs={
        'class': 'form-control round-form',
        'placeholder': 'Enter Description here'
    }),
        'amount': forms.NumberInput(attrs={
            'class': 'form-control round-form',
            'placeholder': 'Enter Amount here',
        }),
        'igst': forms.NumberInput(attrs={
            'class': 'form-control round-form',
            'placeholder': 'Enter IGST Rate here'
        }),
        'sgst': forms.NumberInput(attrs={
            'class': 'form-control round-form',
            'placeholder': 'Enter SGST Rate here'
        }),
        'cgst': forms.NumberInput(attrs={
            'class': 'form-control round-form',
            'placeholder': 'Enter CGST Rate here'
        }),
        'quantity': forms.NumberInput(attrs={
            'class': 'form-control round-form',
            'placeholder': 'Enter Quantity here'
        }),
        'gst': forms.Select(choices=gst_choices,attrs={
            'class': 'form-control round-form',
            'placeholder': 'Choose GST',
        }),
        'total': forms.NumberInput(attrs={
            'class': 'form-control round-form',
            'placeholder': 'Total',
            'readonly': True
        }),
    }
)
