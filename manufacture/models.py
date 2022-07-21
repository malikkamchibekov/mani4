from django.db import models

STATUSES = [
        ('Новый', 'Новый'),
        ('В процессе', 'В процессе'),
        ('Собран', 'Собран'),
        ('Отгружен', 'Отгружен'),
        ('Оплачен', 'Оплачен'),
    ]


class Sale(models.Model):
    vendor_code = models.CharField(max_length=40, verbose_name='Артикул')
    title = models.CharField(max_length=40, verbose_name="Наименование")
    type = models.CharField(max_length=40, verbose_name="Модель")
    size = models.CharField(max_length=40, verbose_name="Размер")
    quantity = models.IntegerField(default=0, verbose_name="Кол-во")
    price = models.DecimalField(max_digits=40, decimal_places=2, default=0, verbose_name="Цена сом")
    status = models.CharField(max_length=40, choices=STATUSES)
    total = models.DecimalField(max_digits=40, decimal_places=2, verbose_name="Сумма сом")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    def __str__(self):
        return f'{self.vendor_code}'


class Catalogue(models.Model):
    vendor_code = models.CharField(max_length=40)  # Артикул модели
    image = models.ImageField(upload_to='media/products/%Y/%m/%d', blank=True)  # Фото товара
    title = models.CharField(max_length=40, blank=True, null=True) # Название модели
    type = models.CharField(max_length=40)  # Тип модели обуви(цвета, отделка, и т.д.)
    size = models.CharField(max_length=40)  # Размерная сетка
    rest_quantity = models.PositiveIntegerField()  # Остаток на складе

    def __str__(self):
        return f'{self.vendor_code}, {self.type}'


class SalaryTotal(models.Model):  # общая зарплата
    employee = models.OneToOneField('Employee', on_delete=models.CASCADE, primary_key=True)
#    occupation = models.ForeignKey('Occupation', null=True, blank=True, on_delete=models.CASCADE,
                              #     related_name='salary_occupation')
    sales = models.ForeignKey('Sale', on_delete=models.CASCADE, null=True, blank=True, related_name='salary_sales')
    working_out = models.OneToOneField('Production', on_delete=models.CASCADE, null=True, blank=True)
    month = models.DateTimeField(auto_now=True)
    working_days = models.IntegerField(null=True)
    fact_work_days = models.IntegerField(null=True)
    oklad_social_fund = models.IntegerField(null=True)
    oklad_fact = models.IntegerField(null=True)
    social_fund = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    firm_social_fund = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    oklad_nachislen = models.IntegerField(null=True)
    viplata = models.IntegerField(null=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.viplata}'

    # def social_fund(self):  # оц фонд отчисления работника 18%
    #
    #     return self.oklad_social_fund * 0.18
    #
    # def firm_social_fund(self):  # соц фонд отчисления работодателя 17,25%
    #
    #     return self.oklad_social_fund * 0.1725

    # def accrued_salary(self):#Начисленная зарплата=Сдельная станок ПУ (карусель(Выплата))+ Сдельная ЭВА(Расчет по ЭВА(Сдельная зарплата))
    #     return (self.calc_pu + self.calc_eva)
    #
    #
    # def calc_pu(self): #Сдельная станок ПУ (карусель(Выплата)):
    #     pass
    #
    #
    # def calc_eva(self): #Сдельная ЭВА(Расчет по ЭВА(Сдельная зарплата)
    #     pass
    #


class Occupation(models.Model):
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=64)
    objects = models.Manager()

    def __str__(self):
        return self.title


class Employee(models.Model):
    active = models.BooleanField(default=True)
    date_start = models.DateTimeField(auto_now_add=True)
    fio = models.CharField(max_length=64, unique=True)  # имя фамилия отчество сотрудника
    phone = models.CharField(max_length=20, blank=True)
    phone1 = models.CharField(max_length=20, blank=True)
    occupation = models.ForeignKey('Occupation', null=True, blank=True, on_delete=models.CASCADE,
                                   related_name='employer_ocupation')
    monthly_salary = models.IntegerField(default=0)
    objects = models.Manager()

    def __str__(self):
        return self.fio


class Production(models.Model):  # Выробатка
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    model = models.ForeignKey('Catalogue', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, verbose_name='Кол-во')
    defect_worker = models.IntegerField(default=0)


    # workers_defect = models.IntegerField(default=0)  # Брак рабочих
    # machines_defect = models.IntegerField(default=0)  # Брак станков
    # say_marriage = models.IntegerField(default=0)  # Брак Сая
    #
    # def __str__(self):
    #     return f'{self.quantity}'

class Client(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, verbose_name='Клиент')
    phone = models.CharField(max_length=100, verbose_name='Номер телефона')
    address = models.CharField(max_length=100, blank=True)
    file = models.FileField(upload_to='media/clients/%Y/%m/%d', blank=True)

    def __str__(self):
        return f'{self.name}, {self.phone}'
