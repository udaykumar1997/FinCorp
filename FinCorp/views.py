from django.shortcuts import render
from .models import Transaction
from .forms import TransactionForm

# You can create your views here
def transaction_form(request):
    form = TransactionForm()
    return render(request, 'transaction_form.html', {'form': form})