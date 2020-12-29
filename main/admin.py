from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Beneficiary)
admin.site.register(Donor)
admin.site.register(Partner)
admin.site.register(Product)
admin.site.register(Donation)
