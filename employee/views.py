from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import Employee
from .forms import EmployeeForm,ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.

@login_required
def dashboard(request):   
    context = {
        "employee_count":Employee.objects.count(),
        "user_count":User.objects.count()
    }

    return render(request,"dashboard/dashboard.html",context)

@login_required
def employee_list(request):
    search = request.GET.get("search")
    employee = Employee.objects.all()
    if search:
        employee = employee.filter(
            Q(name__icontains=search)|Q(email__icontains=search)|Q(department__icontains=search)
        )
    paginator = Paginator(employee,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':page_obj,
        'employees':employee
    }
    return render(request,"employee/employee_list.html",context)

@login_required
def add_employee(request):
   


    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request,"Employee added successfully.")
            return redirect("employee_list")

    else:
        form = EmployeeForm()

    context = {
        "form": form
    }

    return render(request, "employee/add_employee.html", context)

@login_required
def edit_employee(request,id):
    employee = get_object_or_404(Employee, id = id)
    if request.method == "POST":
        form  = EmployeeForm(
            request.POST,
            request.FILES,
            instance = employee
        )

        if form.is_valid():
            form.save()
            messages.success(request,"Employee updated successfully.")
            return redirect("employee_list")

    else:
        form = EmployeeForm(instance=employee)

    return render(request,"employee/edit_employee.html",{"form":form,"employee":employee})

@login_required
def delete_employee(request,id):
    employee = get_object_or_404(Employee,id=id)
    if request.method == "POST":
        if employee.image:
            if os.path.isfile(employee.image.path):
                os.remove(employee.image.path)

        employee.delete()
        messages.success(request, "Employee deleted successfully.")
        return redirect("employee_list")

    return render(request,"employee/delete_employee.html",{"employee":employee})

@login_required
def profile(request):

    if request.method == "POST":

        form = ProfileForm(
            request.POST,
            instance=request.user
        )

        if form.is_valid():
            form.save()
            messages.success(request,"Profile updated successfully.")
            return redirect("profile")

    else:
        form = ProfileForm(instance=request.user)

    return render(
        request,
        "accounts/profile.html",
        {
            "form": form
        }
    )

@login_required
def change_password(request):

    if request.method == "POST":

        form = PasswordChangeForm(
            request.user,
            request.POST
        )

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(
                request,
                user
            )

            messages.success(
                request,
                "Password changed successfully."
            )

            return redirect("profile")

    else:

        form = PasswordChangeForm(request.user)

    return render(
        request,
        "accounts/change_password.html",
        {
            "form": form
        }
    )