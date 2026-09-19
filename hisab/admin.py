from django.contrib import admin
from .models import Khata

@admin.register(Khata)
class KhataAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'reason', 'amount', 'transaction_type', 'date')