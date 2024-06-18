from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UpdateUserForm
from authentication.models import CustomUser


# TODO: Change returns
# TODO: Add go back button
# TODO: Add reset button
# Create your views here.
@login_required(login_url='login')
def account(request):
    if request.method == "POST":
        form = UpdateUserForm(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return render(request, 'account.html', {'form': form})
    else:
        form = UpdateUserForm(instance=request.user)

        return render(request, 'account.html', {'form': form})
