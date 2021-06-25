from django.contrib import admin
from .models import User, manager, hadmin, buser, Invoice_Model, Invoice

# Register your models here.
admin.site.register(User)
admin.site.register(buser)
admin.site.register(manager)
admin.site.register(hadmin)
admin.site.register(Invoice_Model)
admin.site.register(Invoice)