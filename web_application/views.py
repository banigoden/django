from django.shortcuts import get_object_or_404, render
from .models import Employee


def index(request):

    employees = Employee.objects.all()
    num_employee = employees.count() # aggregate method
    return render(request, "web_application/index.html", {
        "employees": employees,
        "total_employees": num_employee,
    })


def employee_detail(request, id):

    employee = get_object_or_404(Employee, pk=id)
    
    return render(request, 'web_application/employee_detail.html', {
              "first_name": employee.first_name,
              "second_name": employee.second_name,
              "department": employee.department,
              "email": employee.email,
              "date": employee.date,
              "level": employee.level
              }) 

def filtered_employees_criteria(request, criteria):
    filtered_employees = Employee.objects.filter(department=criteria)
    return render(request, "web_application/filtered_employees.html",{
        "filtered_employees": filtered_employees,
        "filter_criteria": f"Employees criteria is {criteria} :"
    })

def filtered_employees_field_value(request, field , value):
    # Validate field parameter to prevent arbitrary queries
    allowed_fields = ["first_name", "second_name", "email", "department", "level", "date"]
    if field not in allowed_fields:
        # Handle invalid field, return an error page
        return render(request, "web_application/error_page.html", {"error_message": "Invalid field"})
    
     # Create a dictionary to map field names to actual model fields
    field_mapping = {
        "first_name": "first_name",
        "second_name": "second_name",
        "department": "department",
        "email": "email",
        "level": "level",
        "date": "date"  
    }

    # Use the field_mapping dictionary to get the actual field name
    actual_field = field_mapping.get(field)

    # Perform filtering based on the field and value
    filtered_employees = Employee.objects.filter(**{f"{actual_field}__icontains": value})

    context = {
        "filtered_employees": filtered_employees,
        "filter_criteria": f"Employees with {field} containing '{value}'",
    }

    return render(request, "web_application/filtered_employees.html", context=context)


 