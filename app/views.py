from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum

from .models import Transaction


def home(request):

    search = request.GET.get('search')

    transactions = Transaction.objects.all().order_by('-id')

    if search:
        transactions = transactions.filter(
            title__icontains=search
        )

    total_income = Transaction.objects.filter(
        type='Income'
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    total_expense = Transaction.objects.filter(
        type='Expense'
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    balance = total_income - total_expense

    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
    }

    return render(
        request,
        'app/home.html',
        context
    )


def add_transaction(request):

    if request.method == 'POST':

        title = request.POST.get('title')

        amount = request.POST.get('amount')

        type = request.POST.get('type')

        category = request.POST.get('category')

        if title and amount:

            Transaction.objects.create(

                title=title,
                amount=amount,
                type=type,
                category=category,

            )

        return redirect('home')

    return render(
        request,
        'app/add_transaction.html'
    )


def delete_transaction(request, id):

    transaction = get_object_or_404(
        Transaction,
        id=id
    )

    transaction.delete()

    return redirect('home')


def update_transaction(request, id):

    transaction = get_object_or_404(
        Transaction,
        id=id
    )

    if request.method == 'POST':

        transaction.title = request.POST.get('title')

        transaction.amount = request.POST.get('amount')

        transaction.type = request.POST.get('type')

        transaction.category = request.POST.get('category')

        transaction.save()

        return redirect('home')

    context = {
        'transaction': transaction
    }

    return render(
        request,
        'app/update_transaction.html',
        context
    )