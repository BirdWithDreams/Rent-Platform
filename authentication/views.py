from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm
from .models import Wallet, CustomUser

FORM_FIELDS = ["Логін", "Електронна пошта", "Пароль (має містити хоча б 8 символів та 1 літеру)", "Повторити пароль"]


# Create your views here.
def register_page(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            wallet = Wallet.objects.create(
                user_id=user,
                balance=0
            )
            user = form.cleaned_data.get('username')

            return redirect('main')
    form = list(zip(FORM_FIELDS, form))
    return render(request, 'register.html', {'form': form})


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return render(request, 'login.html', {})

    return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    return redirect('login')
