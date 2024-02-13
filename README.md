# WorktimeRecovered
- **Учет рабочего времени.**
Пользователи: Работники и Менеджеры.
Работник приходит на работу нажимает на кнопку - начало рабочего дня, нажимает на кнопку - приостановка, нажимает на кнопку - продолжение, в конце нажимает на кнопку - конец рабочего дня. В базу заносится рабочее время.
____________________________
This project was done in 10 day about a half a year ago. Then .env was lost, and the project was layed on a shelve. Now I deside to recover it with no hurry, step by step.

Users: Emploers and Emploees. Emploee starts work day - push the bttn, stop work day - push the bttn, resumes to work - push the bttn, end day work - push the bttn. Worktime --> Base. Postgres is here. If you dont have PyCharm (proffesional) then try dbeaver - best choice.

- Django project with forms. 
    - Install deps:

    ```cmd
    pip install -r requirements.txt
    ```

    - Start dev server:
    (Permissions (models.py line 17) must be commented before first makemigrations, then add them and try: python3 manage.py makinigrations)

    ```cmd
    python3 manage.py makemigrations 
    ```

     ```cmd
    python3 manage.py migrate
    ```

    ```cmd
    python3 manage.py runserver
    ```



1. Use command files to initial base filling: For ex. _python3 manage.py create_super_user_ will be enough to start.
2. Create Eployer at employer_create_with_double_form/ (with 2 forms), employer_create/ (with formset), 
3. Create Eployee at employee_create_with_doubleform/ (with 2 forms).
To keep everything in order for each creating endpoint to make self form. For ex. endpoint: "employer_create_with_double_form/" uses _CustomUserDoubleform_, _EmployerDoubleformWithourCustomuser_. Thus we have clear fields at every end point
4.  - Create Timesheet at 'timesheet_create/'
    ![Create Timesheet at 'timesheet_create/'.](/media/Screenshot%20from%202024-02-13%2022-08-49.png)
    - This in base saved
    ![This in base saved.](/media/Screenshot%20from%202024-02-13%2022-09-50.png)

Andrey Mazo (+79219507391, andreymazo@mail.ru)