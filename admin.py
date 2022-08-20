from django.contrib import admin
from .models import Employer, Contact, Subscribe, Pay, Paypal
# Register your models here
admin.site.register(Employer)
admin.site.register(Contact)
admin.site.register(Subscribe)
admin.site.register(Pay)
admin.site.register(Paypal)
