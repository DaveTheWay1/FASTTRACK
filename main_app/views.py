from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .forms import CurrentBalanceForm, MonthlyCostsForm, MonthlyPaymentsForm, AdditionalPurchasesForm
from .models import Current_Balance, Monthly_Costs, Monthly_Payments, Additional_Purchases

@login_required
def home(request):
    cur_balance = Current_Balance.objects.filter(user=request.user).first()
    monthly_costs = Monthly_Costs.objects.filter(user=request.user)
    monthly_payments = Monthly_Payments.objects.filter(user=request.user)
    additional_purchases = Additional_Purchases.objects.filter(user=request.user)
    add_balance_form = CurrentBalanceForm
    add_monthly_costs_form = MonthlyCostsForm
    add_monthly_payments_form = MonthlyPaymentsForm
    add_additional_purchases_form = AdditionalPurchasesForm
    return render(request, 'home.html', {
        'cur_balance':cur_balance, 
        'monthly_costs':monthly_costs,
        'add_balance_form':add_balance_form,
        'add_monthly_costs_form':add_monthly_costs_form,
        'monthly_payments':monthly_payments,
        'add_monthly_payments_form':add_monthly_payments_form,
        'additional_purchases':additional_purchases,
        'add_additional_purchases_form':add_additional_purchases_form
    })

@login_required
def user_logout(request):
    logout(request)
    return redirect('/accounts/login/')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # supers are not required in function based views 
        # because they dont inherit form_valid from a parent class
        # rather form_valid is a built object method
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
        new_current_balance.original_amount = new_current_balance.amount
        new_current_balance.save()
    return redirect('home')

@login_required
def reset(request, current_balance):
    cur_balance = Current_Balance.objects.get(id=current_balance)
    cur_balance.amount = cur_balance.original_amount
    cur_balance.save()
    return redirect('home')

@login_required
def add_monthly_costs(request, user_id):
    form = MonthlyCostsForm(request.POST)
    if form.is_valid():
        new_monthly_cost = form.save(commit=False)
        new_monthly_cost.user_id = user_id
        new_monthly_cost.save()
        return JsonResponse({'monthly_cost_name': new_monthly_cost.name, 'monthly_cost_amount':new_monthly_cost.amount})
    return redirect('home')


def apply_monthly_costs(request, current_balance, monthly_cost):
    cb = Current_Balance.objects.get(id=current_balance)
    mc = Monthly_Costs.objects.get(id=monthly_cost)
    applied = cb.amount - mc.amount
    cb.amount = applied
    cb.save()
    return redirect('home')

@login_required
def add_monthly_payments(request, user_id):
    form = MonthlyPaymentsForm(request.POST)
    if form.is_valid():
        new_monthly_payment = form.save(commit=False)
        new_monthly_payment.user_id = user_id
        new_monthly_payment.save()
    return redirect('home')

def apply_monthly_payment(request, current_balance, monthly_payment):
    cb = Current_Balance.objects.get(id=current_balance)
    mp = Monthly_Payments.objects.get(id=monthly_payment)
    cb.amount = cb.amount + mp.amount
    cb.save()
    return redirect('home')

@login_required
def add_additional_purchases(request, user_id):
    form = AdditionalPurchasesForm(request.POST)
    if form.is_valid():
        new_additional_purchase = form.save(commit=False)
        new_additional_purchase.user_id = user_id
        new_additional_purchase.save()
    return redirect('home')

def apply_additional_purchase(request, current_balance, additional_purchase):
    cb = Current_Balance.objects.get(id=current_balance)
    ap = Additional_Purchases.objects.get(id=additional_purchase)
    cb.amount = cb.amount - ap.amount
    cb.save()
    return redirect('home')

class CurrentBalanceUpdate(LoginRequiredMixin, UpdateView):
    model = Current_Balance
    fields = ['amount']

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.original_amount = instance.amount  # Set the updated amount as the new original amount
        instance.save()
        # * form is valid here requires a super bc it is a 
        # * class based view that inheritas the form_valid from 
        # * the parent class ModelFormMixin
        # supers are not required in function based views 
        # because they dont inherit form_valid from a parent class
        # rather form_valid is a built object method
        return super().form_valid(form)

class MonthlyCostUpdate(LoginRequiredMixin, UpdateView):
    model = Monthly_Costs
    fields = ['name','amount']

class MonthlyCostDelete(LoginRequiredMixin, DeleteView):
    model = Monthly_Costs
    success_url = '/'

class MonthlyPaymentUpdate(LoginRequiredMixin, UpdateView):
    model = Monthly_Payments
    fields = ['name','amount']

class MonthlyPaymentDelete(LoginRequiredMixin, DeleteView):
    model = Monthly_Payments
    success_url = '/'

class AdditionalPurchaseUpdate(LoginRequiredMixin, UpdateView):
    model = Additional_Purchases
    fields = ['name','amount']

class AdditionalPurchaseDelete(LoginRequiredMixin, DeleteView):
    model = Additional_Purchases
    success_url = '/'