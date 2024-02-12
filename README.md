# WorktimeRecovered
- **Учет рабочего времени.**
Пользователи: Работники и Менеджеры.
Работник приходит на работу нажимает на кнопку - начало рабочего дня, нажимает на кнопку - приостановка, нажимает на кнопку - продолжение, в конце нажимает на кнопку - конец рабочего дня. В базу заносится рабочее время.
Users: Emploers and Emploees. Emploee starts work day - push the bttn, stop work day - push the bttn, resumes to work - push the bttn, end day work - push the bttn. Worktime --> Base.
- Django project with forms. 
Install deps:

```cmd
pip install -r requirements.txt
```

Start dev server:

```cmd
python3 manage.py runserver
```


1. Create Eployer at employer_create_with_double_form/ (with 2 forms), employer_create/ (with formset), 
2. Create Eployee at employee_create_with_doubleform/ (with 2 forms).
To keep everything in order for each creating end point to make self form. For ex. employer_create_with_double_form/ uses CustomUserDoubleform, EmployerDoubleformWithourCustomuser. Thus we have clear fields at every end point

Andrey Mazo (+79219507391)