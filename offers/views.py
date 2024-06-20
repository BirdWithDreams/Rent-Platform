from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from authentication.models import Wallet
from .forms import OfferCreateForm
from .models import Offers, Contract
from django.contrib import messages

FORM_FIELDS = ["Назва", "Категорія", "Опис", "Ціна", "Теги", "Зображення"]


# Create your views here.
@login_required(login_url='login')
def my_offers(request):
    offers = Offers.objects.filter(user_id=request.user)

    return render(request, 'user-offers.html', {'offers': offers, 'user': request.user})


@login_required(login_url='login')
def add_offer(request):
    form = OfferCreateForm()
    if request.method == 'POST':
        form = OfferCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user_id = request.user
            form.save()

            return redirect('account')
    form = list(zip(FORM_FIELDS, form))
    return render(
        request,
        'offer-add-edit.html',
        {
            'form': form,
            'title': 'Створення пропозиції',
            'btn': 'Змінити'
        }
    )


@login_required(login_url='login')
def edit_offer(request, offer):
    if request.method == "POST":
        form = OfferCreateForm(request.POST, request.FILES, instance=Offers.objects.get(id=offer))
        if form.is_valid():
            offer = form.save(commit=False)
            offer.save()
            return redirect('account')

    form = OfferCreateForm(instance=Offers.objects.get(id=offer))
    form = list(zip(FORM_FIELDS, form))
    return render(
        request,
        'offer-add-edit.html',
        {
            'form': form,
            'title': 'Редагування пропозиції',
            'btn': 'Змінити'
        }
    )


# TODO: fix None in form
# TODO: Add form handling
@login_required(login_url='login')
def make_offer(request, offer):
    if request.method == 'POST':
        offer = Offers.objects.get(id=offer)
        seller = offer.user_id
        buyer = request.user
        seller_wallet = Wallet.objects.get(user_id=seller)
        buyer_wallet = Wallet.objects.get(user_id=buyer)
        buyer_first_name = request.POST.get('buyer_first_name')
        buyer_last_name = request.POST.get('buyer_last_name')
        buyer_email = request.POST.get('buyer_email')
        buyer_city = request.POST.get('buyer_city')
        buyer_location = request.POST.get('buyer_location')
        balance = Wallet.objects.get(user_id=request.user).balance

        if offer.price > balance:
            return render(request, 'transaction-status.html', {'status': 0})

        contract = Contract.objects.create(
            seller=seller,
            buyer=buyer,
            offer=offer,
            buyer_first_name=buyer_first_name,
            buyer_last_name=buyer_last_name,
            buyer_email=buyer_email,
            buyer_city=buyer_city,
            buyer_location=buyer_location,
        )

        seller_wallet.balance += offer.price
        seller_wallet.save()
        buyer_wallet.balance -= offer.price
        buyer_wallet.save()

        return render(request, 'transaction-status.html', {'status': 1})

    return render(
        request,
        'make-offer.html',
        {
            'offer': Offers.objects.get(id=offer),
            'seller': request.user,
            'btn': 'Створити'
        }
    )
