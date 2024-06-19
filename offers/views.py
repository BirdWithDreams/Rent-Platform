from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OfferCreateForm
from .models import Offers
from django.contrib import messages

FORM_FIELDS = ["Назва", "Категорія", "Опис", "Ціна", "Теги", "Зображення"]


# Create your views here.
@login_required(login_url='login')
def my_offers(request):
    offers = Offers.objects.filter(user_id=request.user)

    return render(request, 'user_offers.html', {'offers': offers, 'user': request.user})


@login_required(login_url='login')
def add_offer(request):
    form = OfferCreateForm()
    if request.method == 'POST':
        form = OfferCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user_id = request.user
            form.save()
            messages.success(request, 'Offer was created for ')

            return redirect('account')
    form = list(zip(FORM_FIELDS, form))
    return render(request, 'offer-add-edit.html', {'form': form, 'title': 'Створення пропозиції'})


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
    return render(request, 'offer-add-edit.html', {'form': form, 'title': 'Редагування пропозиції'})

# TODO: fix None in form
# TODO: Add form handling
@login_required(login_url='login')
def make_offer(request, offer):
    if request.method == 'POST':



        return redirect('search')


    return render(request, 'make_offer.html', {'offer': Offers.objects.get(id=offer), 'user': request.user})

