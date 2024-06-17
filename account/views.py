from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UpdateUserForm
from authentication.models import CustomUser


# Create your views here.

def account(request):
    form = UpdateUserForm(instance=request.user)
    if request.method == "POST":
        form = UpdateUserForm(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return render(request, 'account.html', {'form': form})
    else:
        form = UpdateUserForm(instance=request.user)

        return render(request, 'account.html', {'form': form})

    return render(request, 'account.html', {'form': form})

# def account(request):
#
#
#     form = UpdateUserForm(instance=request.user)
#     if request.method == 'POST':
#         form = UpdateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             messages.success(request, 'Account was created for ' + user)
#
#             return redirect('index')
#
#     return render(request, 'register.html', {'form': form})
