# Virtual Environment setup open command prompt:
1) Go to the directory and create the folders, Use mkdir for the same
2) Then to install vm --> pip install virtualenv
3) Virtualenv venv--> ([Response]created virtual environment CPython3.8.8.final.0-64 in 3391ms) and venv folder will be created 
4) To Activate virtual env-->cd venv-->cd scripts-->activate ([Response](venv) ...\Desktop\Courses\Course-Lib\venv\Scripts>)
5) Come back to the Course-lib Folder
6) To install Django--> pip install django
7) To confirm if the installation is successfull type-->django-admin ([Response] Available subcommands)
8) To create start project-->django-admin startproject course_library .
9) To run the vm-->python manage.py runserver
10) django-admin startapp <app name>
11) To open VS code type--> code .
12) Now to register the app--> open project course_library-->open settings.py--> go to Install apps-->type your app name
13) In course_lib file -->urls.py--> import include--> we need to mention the path of urls that we will include--> path('',include("app.urls"))
14) After working urls.py we will write logic on app --> views.py
15) [V 10]Convert folder into package type __init__.py in app folder, this is like a shortcut folder to find new urls
16) [V 11]To access admin http://127.0.0.1:8000/admin If not able to access add path('admin/', admin.site.urls), in urls.py
17) on terminal type--> manage.py createsuperuser  
