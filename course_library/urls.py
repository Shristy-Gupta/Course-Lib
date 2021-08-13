"""course_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import HttpResponse
from app.views import home,verify_payment,coursePage,LoginView,SignupView,signout,checkout,mycourses
from django.conf import settings
from django.conf.urls.static import static
from course_library.settings import MEDIA_ROOT, MEDIA_URL

# Moved to HomePage.py 
# def home(request):
#     return HttpResponse("Home Page")

#Shristy-Define Home Function
urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout', signout, name='logout'),
    path('my-course', mycourses, name='my-course'),
    path('signup', SignupView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('', home, name='home'),
    path('courses/<str:slug>', coursePage, name='coursepage'),
    path('check-out/<str:slug>', checkout, name='check-out'),
    path('verify_payment', verify_payment, name='verify_payment'),
    #path('',include("app.urls"))
]
urlpatterns +=static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
