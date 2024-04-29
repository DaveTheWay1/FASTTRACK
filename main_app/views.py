from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .forms import CurrentBalanceForm, MonthlyCostsForm, MonthlyPaymentsForm
from .models import Current_Balance, Monthly_Costs, Monthly_Payments

@login_required
def home(request):
    cur_balance = Current_Balance.objects.filter(user=request.user).first()
    monthly_costs = Monthly_Costs.objects.filter(user=request.user)
    monthly_payments = Monthly_Payments.objects.filter(user=request.user)
    add_balance_form = CurrentBalanceForm
    add_monthly_costs_form = MonthlyCostsForm
    add_monthly_payment_form = MonthlyPaymentsForm
    return render(request, 'home.html', {
        'cur_balance':cur_balance, 
        'monthly_costs':monthly_costs,
        'add_balance_form':add_balance_form,
        'add_monthly_costs_form':add_monthly_costs_form,
        'monthly_payments':monthly_payments,
        'add_monthly_payments_form':add_monthly_payment_form
    })

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

@login_required
def add_monthly_costs(request, user_id):
    form = MonthlyCostsForm(request.POST)
    if form.is_valid():
        new_monthly_cost = form.save(commit=False)
        new_monthly_cost.user_id = user_id
        new_monthly_cost.save()
    return redirect('home')

@login_required
def add_monthly_payments(request, user_id):
    form = MonthlyPaymentsForm(request.POST)
    if form.is_valid():
        new_monthly_payment = form.save(commit=False)
        new_monthly_payment.user_id = user_id
        new_monthly_payment.save()
    return redirect('home')

class CurrentBalanceUpdate(LoginRequiredMixin, UpdateView):
    model = Current_Balance
    fields = ['amount']

class MonthlyCostUpdate(LoginRequiredMixin, UpdateView):
    model = Monthly_Costs
    fields = ['name','amount']