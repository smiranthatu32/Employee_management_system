from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context  ={
    'emps' : emps}
    return render(request, 'all_emp.html',context)


def add_emp(request):
        if request.method == "POST":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            salary = request.POST['salary']
            role = request.POST['role']
            phone = request.POST['phone']
            dept = request.POST['dept']
            email_name = request.POST['email_name']
            new_emp = Employee(first_name=first_name,last_name=last_name,salary=salary,role_id=role,phone=phone,dept_id=dept,email_name=email_name)
            new_emp.save()
            return  HttpResponse('employee created and added sucessfully')
        elif request.method == "GET":
            return render(request, 'add_emp.html')
        else:
            return HttpResponse('employee is not created')




def del_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_deleted = Employee.objects.get(id=emp_id)
            emp_to_be_deleted.delete()
            return HttpResponse("employee has been deleted")
        except:
            return HttpResponse("plss enter valid employee")

    emps = Employee.objects.all()
    context = {
        'emps': emps}
    return render(request, 'del_emp.html', context)



def filter_emp(request):
    if request.method == "POST":
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name= dept)
         if role:
            emps = emps.filter(role__name= role)

        context = {
            'emps' : emps
        }
        return render(request,'all_emp.html',context)

    elif request.method == "GET":
        return  render(request,'filter_emp.html')

    else:
        HttpResponse("Erorr!")



