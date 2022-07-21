from django import forms
from .models import *


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ('vendor_code', 'title', 'type', 'size', 'quantity', 'price', 'total')


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
