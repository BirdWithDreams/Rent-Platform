from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UpdateUserForm
from authentication.models import CustomUser

# TODO: Change return
# TODO: Add go back button
FORM_FIELDS = ["Ім'я", "Прізвище", "Електронна пошта", "Номер карти", "Адреса", "Місто"]



# TODO: Change returns
# TODO: Add go back button
# TODO: Add reset button
# Create your views here.
@login_required(login_url='login')
def account(request):
    form = UpdateUserForm(instance=request.user)
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

        return render(request, 'account.html', {'form': form})

    return render(request, 'account.html', {'form': form})