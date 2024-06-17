from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OfferCreateForm
from .models import Offers
from django.contrib import messages


# Create your views here.
#TODO: Add edit button and logic
@login_required(login_url='login')
def my_offers(request):
    offers = Offers.objects.filter(user_id=request.user)
    return render(request, 'myoffers.html', {'myoffers': offers})

@login_required(login_url='login')
def add_offer(request):
    form = OfferCreateForm()
    if request.method == 'POST':
        form = OfferCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user_id = request.user
            form.save()
            messages.success(request, 'Offer was created for ')

            return redirect('my_offers')

    return render(request, 'add_offer.html', {'form': form})
