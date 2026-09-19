from django.shortcuts import render
from .models import Khata
from django.db.models import Sum

def home(request):
    income = Khata.objects.filter(transaction_type='INCOME').aggregate(Sum('amount'))['amount__sum'] or 0
    expense = Khata.objects.filter(transaction_type='EXPENSE').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = income - expense
    all_data = Khata.objects.all().order_by('-id')
    return render(request, 'home.html', {'income': income, 'expense': expense, 'balance': balance, 'datas': all_data})