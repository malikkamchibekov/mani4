from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
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

