from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import CurrentBalanceForm
from .models import Current_Balance

@login_required
def home(request):
    cur_balance = Current_Balance.objects.filter(user=request.user).first()
    add_balance_form = CurrentBalanceForm
    return render(request, 'home.html', {'cur_balance':cur_balance, 'add_balance_form':add_balance_form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('/accounts/login/')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


@login_required
def add_current_balance(request, user_id):
    form = CurrentBalanceForm(request.POST)
    if form.is_valid():
        new_current_balance = form.save(commit=False)
        new_current_balance.user_id = user_id
        new_current_balance.save()
    return redirect('home')