
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.http import HttpResponse

from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from datetime import datetime
from django.contrib.auth.decorators import user_passes_test


def index(request):
    print('das')
    if str(request.user) == 'AnonymousUser':
        return redirect('login')
    else:
        return render(request, 'manufacture/index.html')


#
# @receiver(post_save, sender=SalaryTotal)
# def my_handler(sender, instance, **kwargs):
#     obj = Employee.objects.get(id(**kwargs))
#     obj.monthly_salary = instance.oklad_fact
#     obj.save()


def salary_total(request):
    sales = Sale.objects.all().order_by('-pk')
    return render(request, 'manufacture/salary_total.html', {'sales': sales})


def edit_sale(request, id):
    try:
        edited_sale = Sale.objects.get(id=id)

        if request.method == "POST":
            edited_sale.vendor_code = request.POST.get("vendor_code")
            edited_sale.title = request.POST.get("title")
            edited_sale.type = request.POST.get("type")
            edited_sale.size = request.POST.get("size")
            edited_sale.quantity = request.POST.get("quantity")
            edited_sale.price = request.POST.get("price")
            edited_sale.total = request.POST.get("total")
            edited_sale.save()
            return redirect('salary_total')
        else:
            return render(request, "manufacture/edit_sale.html", {"edited_sale": edited_sale})
    except Sale.DoesNotExist:
        return HttpResponseNotFound("<h2>Продажа не найдена</h2>")


# удаление данных из бд
def delete_sale(request, id):
    try:
        deleted_sale = Sale.objects.get(id=id)
        deleted_sale.delete()
        return redirect('salary_total')
    except Sale.DoesNotExist:
        return HttpResponseNotFound("<h2>Продажа не найдена</h2>")


def raschet_eva(request):
    return render(request, 'manufacture/raschet_eva.html')


def raschet_pu(request):
    return render(request, 'manufacture/raschet_pu.html')


def new_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            try:
                sale = form.save()
                sale.save()
                return redirect('salary_total')
            except:
                form.add_error(None, "Что-то пошло не так, попробуйте снова")
        else:
            form = SaleForm()
    else:
        form = SaleForm()
    return render(request, 'manufacture/new_sale.html', {'form': form})


def employers(request):
    employer = Employee.objects.all()
    return render(request, 'manufacture/employers.html', {'employers': employer})

def view_catalogue(request):
    catalogue = Catalogue.objects.all()
    return render(request, 'manufacture/catalogue.html', {'catalogue': catalogue})


def new_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            try:
                client = form.save()
                client.save()
                return redirect('clients')
            except:
                form.add_error(None, "Что-то пошло не так, попробуйте снова")
        else:
            form = ClientForm()
    else:
        form = ClientForm()
    return render(request, 'manufacture/new_client.html', {'form': form})


def view_client(request):
    clients = Client.objects.all()
    return render(request, 'manufacture/clients.html', {'clients': clients})

def new_employee(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            try:
                client = form.save()
                client.save()
                return redirect('clients')
            except:
                form.add_error(None, "Что-то пошло не так, попробуйте снова")
        else:
            form = ClientForm()
    else:
        form = ClientForm()
    return render(request, 'manufacture/new_client.html', {'form': form})


def daily_production(request):
    productions = DailyProduction.objects.all()
    context = {
        'production': productions,

    }
    return render(request, 'manufacture/daily_production.html', context)


def home(request):
    if request.user == 'AnonymousUser':
        return redirect('login')
    else:
    # new_user = UserRegistrationForm
        return render(request, 'index.html', {'new_user': new_user, 'old_user': AuthenticationForm})


def register_new(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():

            new_user = user_form.save(commit=False)

            new_user.set_password(user_form.cleaned_data['password'])

            new_user.save()
            return redirect('home')
        else:
            print('not ok')
            return redirect('home')
    else:
        user_form = UserRegistrationForm()

    return render(request, 'manufacture/register.html', {'register_form': user_form})


def user_login(request):
    if request.method == 'POST':
        print('das')
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'manufacture/login.html', {'form': form})