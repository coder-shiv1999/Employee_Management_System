from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department
from datetime import datetime
# Create your views here.

def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render(request,'view_all_emp.html',context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = request.POST['role']
        phone = int(request.POST['phone'])
        new_emp = Employee(first_name=first_name,last_name=last_name,salary=salary,dept_id=dept,bonus=bonus,role_id=role,phone=phone,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added succsessfully")
    elif request.method=='GET':
        return render(request,'add_emp.html')
    else:
        return HttpResponse("Error")

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee removed")
        except:
            return HttpResponse("error")
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request,'remove_emp.html',context)