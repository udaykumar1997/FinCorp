from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class TransactionGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ModeOfPayment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Folio(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    TRANSACTION_CLASSES = [
        ('WMBU', 'White, mbu'),
        ('BMBU', 'Black, mbu'),
        ('WMMA', 'White, mma'),
    ]

    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    transaction_group = models.ForeignKey(TransactionGroup, on_delete=models.CASCADE)
    mode_of_payment = models.ForeignKey(ModeOfPayment, on_delete=models.CASCADE)
    transaction_class = models.CharField(max_length=4, choices=TRANSACTION_CLASSES)
    folio = models.ForeignKey(Folio, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} {self.description}"
