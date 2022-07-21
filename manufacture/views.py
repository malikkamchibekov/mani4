from django.shortcuts import render

from .models import Employee, Working_out, Occupation, SalaryTotal


def index(request):
    return render(request, 'manufacture/index.html')


def salary(request):
    return render(request, 'manufacture/salary.html')

def emp_report(request):
    employers = Employee.objects.all()
    context = {
        'employers': employers,
           }
    return render(request, 'manufacture/emp_report.html', context)

def emp_form(request):
    return render(request, 'manufacture/emp_form.html')

def exp(request):
    return render(request, 'manufacture/exp.html')

def salary_total(request):
    payroll = SalaryTotal.objects.all()
    context = {
        'payroll': payroll,
    }
    return render(request, 'manufacture/salary_total.html', context)

def raschet_eva(request):
    return render(request, 'manufacture/raschet_eva.html')

def raschet_pu(request):
    return render(request, 'manufacture/raschet_pu.html')

