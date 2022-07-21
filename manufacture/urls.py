from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('salary_total', salary_total, name='salary_total'),
    path('raschet_eva', raschet_eva, name='raschet_eva'),
    path('raschet_pu', raschet_pu, name='raschet_pu'),
    path('new_sale', new_sale, name='new_sale'),
    path('employers', employers, name='employers'),
    path('catalogue', view_catalogue, name='catalogue'),
    path('edit_sale/<int:id>', edit_sale, name='edit_sale'),
    path('delete_sale/<int:id>', delete_sale, name='delete_sale'),
    path('new_client', new_client, name='new_client'),
    path('clients', view_client, name='clients'),
    path('catalogue', view_catalogue, name='catalogue'),
    path('daily_production', daily_production, name='daily_production'),
]