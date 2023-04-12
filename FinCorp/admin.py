from django.contrib import admin
from .models import Currency, TransactionGroup, ModeOfPayment, Folio, Transaction

admin.site.register(Currency)
admin.site.register(TransactionGroup)
admin.site.register(ModeOfPayment)
admin.site.register(Folio)
admin.site.register(Transaction)
