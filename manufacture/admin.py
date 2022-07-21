from django.contrib import admin

# Register your models here.

from .models import Sales, SalaryTotal, Occupation, Employee, Working_out, Prof


admin.site.register(Sales)
admin.site.register(SalaryTotal)
admin.site.register(Occupation)
admin.site.register(Employee)
admin.site.register(Working_out)
admin.site.register(Prof)