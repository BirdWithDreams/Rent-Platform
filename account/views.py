from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from offers.models import Offers
from .forms import UpdateUserForm
from authentication.models import CustomUser

# TODO: Change return
# TODO: Add go back button
FORM_FIELDS = ["Ім'я", "Прізвище", "Електронна пошта", "Номер карти", "Адреса", "Місто"]


# Create your views here.
@login_required(login_url='login')
def account(request):
    offers = Offers.objects.filter(user_id=request.user)
    if request.method == "POST":
        form = UpdateUserForm(data=request.POST, instance=request.user)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            form = list(zip(FORM_FIELDS, form))
            return render(request, 'account.html', {'form': form, 'offers': offers})

    form = UpdateUserForm(instance=request.user)
    form = list(zip(FORM_FIELDS, form))
    return render(request, 'account.html', {'form': form, 'offers': offers})
