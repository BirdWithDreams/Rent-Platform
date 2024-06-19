from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UpdateUserForm, ReviewCreateForm
from authentication.models import CustomUser
from .models import Feedbacks

# TODO: Add go back button
FORM_FIELDS = ["Ім'я", "Прізвище", "Електронна пошта", "Номер карти", "Адреса", "Місто"]


# TODO: Add messages
# Create your views here.
@login_required(login_url='login')
def account(request):
    if request.method == "POST":
        form = UpdateUserForm(data=request.POST, instance=request.user)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            form = list(zip(FORM_FIELDS, form))
            return render(request, 'account.html', {'form': form})

    form = UpdateUserForm(instance=request.user)
    form = list(zip(FORM_FIELDS, form))
    return render(request, 'account.html', {'form': form})


def user(request, username):
    target = CustomUser.objects.get(username=username)
    reviews = Feedbacks.objects.filter(target=target)
    return render(request, 'user_page.html', {'target': target, 'reviews': reviews})


@login_required(login_url='login')
def add_review(request, username):
    form = ReviewCreateForm()
    if request.method == 'POST':
        target = CustomUser.objects.get(username=username)
        reviews = Feedbacks.objects.filter(target=target)

        form = ReviewCreateForm(request.POST)

        if form.is_valid():
            form.save()

            return render(request, 'user_page.html',
                          {'target': target, 'reviews': reviews})

    return render(request, 'add-review.html', {'form': form})
