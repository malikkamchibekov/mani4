from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('salary_total', salary_total,name='salary_total'),
    path('salary', salary, name='salary'),
    path('exp', exp, name='exp'),
    path('emp_form', emp_form, name='emp_form'),
    path('emp_report', emp_report, name='emp_report'),
    path('raschet_eva', raschet_eva, name='raschet_eva'),
    path('raschet_pu', raschet_pu, name='raschet_pu'),
]