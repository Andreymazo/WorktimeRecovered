from django.urls import include, path, re_path
from worktime.apps import WorktimeConfig
from worktime.filters import  FilteredEmployeeListView
from worktime.formset import CustomuserCreateWithEmployee, CustomuserCreateWithEmployer, CustomuserUpdateWithEmployee
# from worktime.models import CustomUser, CustomUserTable
from worktime.views import CustomUserList, CustomLoginView, CustomuserCreateWithDoubleForm, EmployeeCreateWithDoublform, EmployeeDetail, EmployerDetail, EmployerFilteredListView,FilteredCustomUserListView, EmploeeTableView,  TimesheetsFilteredFilterView, TimesheetLst, EmployeeDelete
#, EmployerCreate,
# # \
#     EmployeeDetail, EmployeeUpdate, EmployeeCreate, \
#     , CustomUserLst, TimesheetsCreateView, TimesheetsUpdateView, TimesheetsDetailView, \
#     TimesheetsDeleteView, WorkTimeListView, WorkTimeCreateView, WorkTimeUpdateView, WorkTimeDetailView, \
#     WorktimeDeleteView, , EmployeeTableView

app_name = WorktimeConfig.name

urlpatterns = [

    path('', CustomLoginView.as_view(template_name='registration/login.html'), name='login'),

    path('customuser_lst2/', CustomUserList.as_view(), name='customuser_lst2'),
    path('customuser_lst/', FilteredCustomUserListView.as_view(), name='customuser_lst'),
    # path('customuser_lst/', CustomUserLst.as_view(table_class = CustomUserTable, model=CustomUser, template_name ='workingtime/customuser_list.html', table_pagination={ "per_page":5 } ) , name='filtered_customuser_lst'),
    path('customuser_create/', CustomuserCreateWithEmployee.as_view(), name='customuser_create'),
    path('customuser_update/<int:pk>', CustomuserUpdateWithEmployee.as_view(), name='customuser_update'),

    path('employer_filtered_list/', EmployerFilteredListView.as_view(), name='employer_filtered_list'),
    path('employer_create/', CustomuserCreateWithEmployer.as_view(template_name="worktime/employer_form.html"), name='employer_create'),
    # https://www.joshuakehn.com/2013/7/18/multiple-django-forms-in-one-form.html
    path('employer_create_with_double_form/', CustomuserCreateWithDoubleForm, name='employer_create_with_double_form'),#.as_view(template_name="worktime/employer_form.html"), name='employer_create_with_include'
    path('employer_detail/<int:pk>', EmployerDetail.as_view(template_name="workingtime/employer_detail.html"), name='employer_detail'),

    path('employee_self/', EmploeeTableView.as_view(template_name="worktime/employee_list.html"), name='employee_self'),

    path('employee_create_with_doubleform/', EmployeeCreateWithDoublform, name='employee_create_with_doubleform'),
    

    # #то же самое, что и выше, только нет фильтрации на селфюзера-работка, будет виден список всем пользователям
    # # path('employee_lst/', EmployeeTableView.as_view(template_name="workingtime/employee_list2.html"), name='employee_lst'),
    path('employee_lst_filtered/', FilteredEmployeeListView.as_view(template_name="worktime/employee_lst_filtered.html"), name='employee_lst_filtered'),
    # ##Либо кастомюзер create с Емплоии, либо просто Емплоии create. Одно комментируем.
    # # path('employee_create/', EmployeeCreate.as_view(template_name="workingtime/employee_form.html"), name='employee_create'),
    path('employee_detail/<int:pk>', EmployeeDetail.as_view(template_name="worktime/employee_detail.html"), name='employee_detail'),
    # #Либо кастомюзер апдейт с Емплоии, либо просто Емплоии апдейт. Одно комментируем.
    # # path('employee_update/<int:pk>', EmployeeUpdate.as_view(template_name="workingtime/employee_form.html"), name='employee_update'),
    path('employee_delete/<int:pk>', EmployeeDelete.as_view(template_name='workingtime/employee_confirm_delete.html'), name='employee_delete'),

    path('timesheet_get_self_time/', TimesheetLst.as_view(), name='timesheet_lst_self_time'),
    path('timesheet/', TimesheetsFilteredFilterView.as_view(template_name="workingtime/timesheet.html"), name='timesheet'),
    # path('timesheet_create/', TimesheetsCreateView.as_view(template_name="workingtime/timesheet_form.html"), name='timesheet_create'),
    # path('timesheet_update/<int:pk>', TimesheetsUpdateView.as_view(template_name="workingtime/timesheet_form.html"), name='timesheet_update'),
    # path('timesheet_detail/<int:pk>', TimesheetsDetailView.as_view(template_name="workingtime/timesheet_form.html"), name='timesheet_detail'),
    # path('timesheet_delete/<int:pk>', TimesheetsDeleteView.as_view(template_name="workingtime/timesheet_confirm_delete.html"), name='timesheet_delete'),

    # path('worktime_lst/', WorkTimeListView.as_view(template_name="workingtime/worktime_lst.html"), name='worktime_lst'),
    # path('worktime_create/', WorkTimeCreateView.as_view(template_name="workingtime/worktime_form.html"), name='worktime_create'),
    # path('worktime_update/<int:pk>', WorkTimeUpdateView.as_view(template_name="workingtime/worktime_update.html"), name='worktime_update'),
    # path('worktime_detail/<int:pk>', WorkTimeDetailView.as_view(template_name="workingtime/worktime_detail.html"), name='worktime_detail'),
    # path('worktime_delete/<int:pk>', WorktimeDeleteView.as_view(template_name="workingtime/worktime_confirm_delete.html"), name='worktime_delete'),

]
