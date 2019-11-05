from django.urls import path
from .import views

app_name = "Register"

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('dest',views.dest,name='dest'),
    path('visit',views.visit,name ='visit'),
    path('booking',views.booking,name='booking'),
    path('booked',views.booked,name='booked'),
    path('sub',views.sub,name='sub'),
    path('home',views.home,name='home')

]
