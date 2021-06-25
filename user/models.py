from django.db import models

# Create your models here.
class invoice(models.Model):
    supplier_invoice_number = models.CharField(max_length=100)
    supplier_invoice_date = models.DateField(default='')
    supplier_name = models.CharField(max_length=100)
    supplier_state = models.CharField(max_length=100)
    total_amount = models.IntegerField(default=0)
    narration = models.CharField(max_length=100, default='')
    user_user_id = models.CharField(max_length=100, default='')
    manager_user_id = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.supplier_invoice_number

class invoice_detail(models.Model):
    invoice_id = models.CharField(max_length=100)
    basic_amount = models.IntegerField(default=0)
    gst_rate = models.IntegerField(default=0)
    cgst = models.IntegerField(default=0)
    sgst = models.IntegerField(default=0)
    igst = models.IntegerField(default=0)

    def __str__(self):
        return self.invoice_id