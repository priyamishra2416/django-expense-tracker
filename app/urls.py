from django.urls import path

from .views import (
    home,
    add_transaction,
    delete_transaction,
    update_transaction,
)


urlpatterns = [

    path('', home, name='home'),

    path(
        'add/',
        add_transaction,
        name='add_transaction'
    ),

    path(
        'delete/<int:id>/',
        delete_transaction,
        name='delete_transaction'
    ),

    path(
        'update/<int:id>/',
        update_transaction,
        name='update_transaction'
    ),

]