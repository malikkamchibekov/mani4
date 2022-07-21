from django.db import models
from django.db.models import Sum

class Sales(models.Model):
    vendor_code = models.CharField(max_length=40)
    # image = models.ImageField()
    type = models.CharField(max_length=40)
    size = models.CharField(max_length=40)
    pair = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=40, decimal_places=2, default=0)
    STATUSES = [
        ('Новый', 'Новый'),
        ('В процессе', 'В процессе'),
        ('Собран', 'Собран'),
        ('Отгружен', 'Отгружен'),
        ('Оплачен', 'Оплачен'),
    ]
    status = models.CharField(max_length=40, choices=STATUSES)
    total = models.DecimalField(max_digits=40, decimal_places=2, default=0)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    def __str__(self):
        return f'{self.vendor_code}'

CURRENCY = 'Som'
days = range(6)

class SalaryTotal(models.Model): #общая зарплата
    employee = models.ForeignKey(
        'Employee',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='salary_employee'
    )
    # occupation = models.ForeignKey('Occupation', null=True, blank=True, on_delete=models.CASCADE, related_name='salary_ocupation')
    # month = models.DateTimeField(auto_now=True)
    # working_days = models.IntegerField(null=True)
    # fact_work_days = models.IntegerField( null=True)
    oklad_social_fund = models.IntegerField(null=True)
    oklad_fact = models.IntegerField(null=True)
    # social_fund = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    # firm_social_fund = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    # oklad_nachislen = models.IntegerField(null=True)
    viplata = models.IntegerField(null=True)

    objects = models.Manager()


    def __str__(self):
        return f'{self.viplata}'

    def __str__(self):
        return f'{self.employee}'

class Occupation(models.Model):
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=64)

    objects = models.Manager()

    def __str__(self):
        return self.title

class Employee(models.Model):
    active = models.BooleanField(default=True)
    date_start = models.DateTimeField(auto_now_add=True)
    fio = models.CharField(max_length=64, unique=True) #имя фамилия отчество сотрудника
    phone = models.CharField(max_length=20, blank=True)
    #phone1 = models.CharField(max_length=20, blank=True)
    occupation = models.ForeignKey('Occupation', null=True, blank=True, on_delete=models.CASCADE, related_name='employer_ocupation')

    monthly_salary = models.IntegerField(default=0)

    objects = models.Manager()

    def __str__(self):
        return self.fio

class Working_out(models.Model): #Выробатка
    data = models.CharField(max_length=10)
    kol_vo = models.IntegerField(default=0)
    workers_defect = models.IntegerField(default=0) #Брак рабочих
    machines_defect = models.IntegerField(default=0) #Брак станков
    Say_marriage = models.IntegerField(default=0)#Брак Сая

    def __str__(self):
        return self.kol_vo

class Prof(models.Model):
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=64)

    objects = models.Manager()

    def __str__(self):
        return self.title