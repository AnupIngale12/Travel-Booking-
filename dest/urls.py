from django.urls import path
from .import views
app_name = "dest"
urlpatterns = [
    path('',views.index,name='index')
]
