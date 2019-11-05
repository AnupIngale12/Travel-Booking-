from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib import messages
from Dest.models import Destination
from Dest.models import Booking
# Create your views here.

def dest(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        price= request.POST.get('price')
        img = request.FILES.get('img')
        offer = request.POST.get('offer')
        if offer == 'on':
            offer = True
        dest1 = Destination.objects.create(name= name,desc = desc, price = price, img = img, offer = offer)
        return render(request,'dest.html',{'dest1':dest1 })

def login(request):
     if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = auth.authenticate(username = username ,password = password ) 
         
          if user is not None:
              if user.is_superuser:
                auth.login(request,user)
                #alert('User login Successfully')
                return render(request,'dest.html')
              else:
                auth.login(request,user)
                return redirect('/')
          else:
              messages.info(request,'Invalid Credentials.')
              return redirect('Register:login')
     else:
         return render(request,'login.html')   

def register(request):
     if request.method == 'POST':
         first_name = request.POST['first_name']
         email = request.POST['email']
         password1= request.POST['password1']
         password2= request.POST['password2']
         username = request.POST['username']

         if password1 == password2:
                 if User.objects.filter(username = username).exists():
                      messages.info(request,'UserName Taken')
                      return redirect('register')
                 elif User.objects.filter(email = email).exists():
                      messages.info(request,'Email Taken')
                      return redirect('Register:register')
                 else:
                     user = User.objects.create_user(username = username ,first_name = first_name , email = email , password = password1)
                     user.save();
                     print('User Created')
                    # alert("User Register Succesfully")
                     return redirect('Register:login')
         else:
            messages.info(request,'Password Not Matching')
            return redirect('register')
         return redirect('/')
     else:
        return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

def visit(request):
     return render(request,'login.html')

def booking(request):
     if request.user.is_authenticated:
         return render(request,'booking.html')
     else:
         messages.info(request,'Login First')
         return redirect('Register:login')

def booked(request):
    Travel=''
    if request.method == 'POST':
        variable = request.POST.get('hiddenVal')
        if int(variable) >= 1:
            for i in range(1, int(variable)+1):
                firstname = request.POST.get('firstname-'+str(i))
                lastname = request.POST.get('lastname-'+str(i))
                email = request.POST.get('email-'+str(i))
                destination = request.POST.get('destination-'+str(i))
                date = request.POST.get('date-'+str(i))
                Travel = Booking.objects.create(firstname = firstname, lastname = lastname, email = email , destination= destination, date=date)
        return render(request, 'booked.html', {'Travel': Travel})


def sub(request):
    return redirect('/')

def home(request):
    return redirect('/')