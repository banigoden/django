from django.urls import path
from . import views
from .views import index, employee_detail

urlpatterns = [
    path("", views.index, name='employees'),
    path("employee/<int:id>", views.employee_detail , name='employee-detail'),
    path("filtered/<str:criteria>", views.filtered_employees, name='filtered-employees'),
    path("filtered/<str:field>/<str:value>", views.filtered_employees, name='filtered-employees')
]
