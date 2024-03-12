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
    ![Create Timesheet at 'timesheet_create/'.](/media/Screenshot%20from%202024-02-14%2010-19-30.png)
    - This in base saved
        - customuser
        ![customuser](/media/Screenshot%20from%202024-02-14%2010-35-00.png)
        - employer
        ![employer](/media/Screenshot%20from%202024-02-14%2010-35-13.png)
        - emloyee
        ![employee](/media/Screenshot%20from%202024-02-13%2022-08-49.png)
        - timesheet
        ![worktime](/media/Screenshot%20from%202024-02-14%2010-19-55.png)
        - worktime
        ![worktime](/media/Screenshot%20from%202024-02-14%2010-20-40.png)

        - I created another private repository. From which:
        ![worktime](/media/Screenshot%20from%202024-03-04%2009-08-24.png)
        ![worktime](/media/Screenshot%20from%202024-03-05%2000-56-00.png)
        
        custom prodaction calendar: Day, Day of week, Year and month. Later - national holidays and some more things? dont know what are yet.
        nationality can be taken from django country lib, but i guess better way to take it without additional lib, without models, just copy file from 'https://public.opendatasoft.com/explore/embed/dataset/countries-codes/table/' and use form choice field
        All info what we can can gather without base and django instruments we must gather (in the left top corner), and I think its the moment when we can start to use models. Lets gather holidays concerned the employer and will save only these holidays in base. списки работодателей и работников, по работодателю переходим в его интерфейс, вылезают только его работники
        Eployer add holidays to his employee. Two forms working indepedantly (more or less). Employer can add holidays and calculate something, thus see changings he made. Later will convert all this in money.
        ![worktime](/media/Screenshot%20from%202024-03-06%2012-04-37.png)
        ![worktime](/media/Screenshot%20from%202024-03-06%2012-03-49.png)

        добавляем праздики, сохраняем в базу, выводим в табличку слева на темплейте.
        ![worktime](/media/Screenshot%20from%202024-03-06%2014-27-05.png)

        добавляем CounterAgent, UpLoadFilesModel грузим файлы каждая модель (Employer, Employee, CounterAgent) в свою папку
        ![worktime](/media/Screenshot%20from%202024-03-08%2010-45-33.png)
        ![worktime](/media/Screenshot%20from%202024-03-08%2010-46-11.png)

        немного кода 
        ![worktime](/media/Screenshot%20from%202024-03-11%2001-03-05.png)
        ![worktime](/media/Screenshot%20from%202024-03-11%2001-03-57.png)
        ![worktime](/media/Screenshot%20from%202024-03-11%2001-04-43.png)
        ![worktime](/media/Screenshot%20from%202024-03-11%2001-17-52.png)

        we have much space for manouvering. in code commented we locate file depending on request, in uncomment we locate exact where we show to locate
        Next step lets create oportunity to Employer to organize employee's notifications. For that we'll have to read some docs and variants of organization. Useing of admin panel to handle this task is not the best idea, all must be done on client side in browser.
        - Create message box, chek if notification, who is request.user (Employer, Employee, Counteragent), show mssg if for him and accept mmsg from him, generate back bttn from mssg box. Little video:
        ![worktime](/media/Screencast from 13.03.2024 00:08:09.webm)
      




        
    

Andrey Mazo (+79219507391, andreymazo@mail.ru)