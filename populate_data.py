from django.core.management.base import BaseCommand
from django.db import transaction
from .web_application.models import Employee

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Create some employees
        employee1 = Employee.create('John', 'Doe', 'IT', 1)
        employee1.save(update_fields=('email', 'level'))
        employee1.email = 'johndoe@example.com'
        employee1.level = 3
        employee1.save()

        employee2 = Employee.create('Jane', 'Doe', 'Marketing', 2)
        employee2.save(update_fields=('email', 'level'))
        employee2.email = 'janedoe@example.com'
        employee2.level = 4
        employee2.save()

        # Create some telephone numbers for each employee
        with transaction.atomic():
            employee1.telephonenumbers.create(number='+1 202-555-1212')
            employee1.telephonenumbers.create(number='+1 929-888-4321')

            employee2.telephonenumbers.create(number='+1 404-777-9876')
            employee2.telephonenumbers.create(number='+1 678-555-3456') 