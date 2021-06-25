import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.models import PermissionsMixin, BaseUserManager

# Create your models here.
class Invoice_Model(models.Model):
    invoice_id = models.IntegerField(default=0)
    supplier_invoice_no = models.CharField(max_length=255, default='')
    supplier_invoice_date = models.DateTimeField(default=datetime.datetime.now())
    supplier_name = models.CharField(max_length=100, default='')
    supplier_state = models.CharField(max_length=100, default='')
    user = models.CharField(max_length=100, default='')
    total_amount = models.IntegerField(default=0)
    total_igst = models.IntegerField(default=0)
    total_sgst = models.IntegerField(default=0)
    total_cgst = models.IntegerField(default=0)
    grand_total = models.IntegerField(default=0)
    naration = models.CharField(max_length=1000, default='')
    status = models.CharField(max_length=20, default='Pending')
    total_gst = models.IntegerField(default=0)

    class Meta:
        db_table = 'Invoice_Model'

    def __str__(self):
        return self.supplier_invoice_no


class Invoice(models.Model):

    invoice = models.ForeignKey(Invoice_Model, related_name='invoice', on_delete=models.CASCADE,)
    description = models.CharField(max_length=100, default='')
    amount = models.IntegerField(default=0)
    igst = models.IntegerField(default=0)
    cgst = models.IntegerField(default=0)
    sgst = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    gst = models.IntegerField(default=0)
    total = models.IntegerField(default=0)


    class Meta:
        db_table = 'Invoice'

    def __str__(self):
        return self.description


class User(AbstractUser):
    role = models.CharField(max_length=100, default='')
    is_manager = models.BooleanField(default=False)
    is_hadmin = models.BooleanField(default=False)
    is_buser = models.BooleanField(default=False)

class manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)



class hadmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class buser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
