from django.db import models


class Transaction(models.Model):

    TRANSACTION_TYPES = (
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    )

    CATEGORY_CHOICES = (
        ('Food', 'Food'),
        ('Shopping', 'Shopping'),
        ('Travel', 'Travel'),
        ('Bills', 'Bills'),
        ('Salary', 'Salary'),
        ('Freelance', 'Freelance'),
    )

    title = models.CharField(max_length=200)

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPES
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title