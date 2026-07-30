from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/",views.dashboard,name='dashboard'),
    path("employees/",views.employee_list,name='employee_list'),
    path("employee/add/",views.add_employee,name='add_employee'),
    path( "employee/edit/<int:id>/",views.edit_employee,name='edit_employee'),
    path("employee/delete/<int:id>/", views.delete_employee, name="delete_employee"),
    path("profile/", views.profile, name="profile"),
    path(
    "change-password/",
    views.change_password,
    name="change_password"
),
    ]