from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accounts.models import Account


def add_account(request):
    account = Account()
    account.name = 'sss'
    account.photo_url = 'jiw' #'https://www.fooish.com/sql/insert-into.html'
    account.age = 10

    account.save()



    return HttpResponse("Hello World!")



def mary_account(request):
    # account = Account.objects.filter(name='mary').first()
    #
    # print(account.name)
    # print(account.age)

    account = Account.objects.raw('SELECT "user"."id", "user"."name", "user"."photo_url", "user"."age" FROM "user" WHERE "user"."name" = "mary"')

    return HttpResponse("Hello!")