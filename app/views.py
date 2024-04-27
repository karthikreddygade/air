from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, HttpResponse ,redirect
from .models import *
from django.contrib.auth.decorators import login_required



def intro(request):
    return render(request,"intro.html")

def homepage(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def termsofuse(request):
    return render(request, "termsofuse.html")

def ticket(request):
    tickets = Tickets.objects.all()  # Fetch all Ticket objects from the database
    return render(request, 'ticket.html', {'tickets': tickets})

def payment(request):
    return render(request,'Payment.html')

def Register(request):
    return render(request,'register.html')

def admin_Register(request):
    return render(request,'admin/admin_register.html')


def Logout(request):
    return  render(request,'home.html')


def admin_adduser(request):
    if request.method == "POST":
        name=request.POST.get('nm')
        email = request.POST.get('em')
        pswd = request.POST.get('pswd')
        Admin.objects.create( name=name,email=email, pswd=pswd)
        return redirect('Register')
    return render(request, 'register.html')
def adduser(request):
    if request.method == "POST":
        name=request.POST.get('nm')
        email = request.POST.get('em')
        pswd = request.POST.get('pswd')
        Passenger.objects.create( name=name,email=email, pswd=pswd)
        return redirect('Register')
    return render(request, 'register.html')



def checkuser(request):
    if request.method == 'POST':
        username = request.POST.get('un')
        password = request.POST.get('pswd')

        # Check if a user with the provided email exists (assuming email is used for login)
        users = Passenger.objects.filter(email=username)
        if users.exists():
            user = users.first()  # Assuming unique emails
            if password == user.pswd:

                request.session['user_id'] = user.id
                return redirect('user_page')
            else:

                return HttpResponse("Invalid Credentials")
        else:

            return HttpResponse("User does not exist")
    else:

        return render(request, 'register.html')  # Assuming you have a login form template


@login_required
def user_page(request):
    username = request.user.username
    user_logged_in = True
    return render(request, 'user.html', {'username': username, 'user_logged_in': user_logged_in})


@login_required
def user_about(request):
    username = request.user.username
    user_logged_in = True
    return render(request, 'user_about.html', {'username': username, 'user_logged_in': user_logged_in})


@login_required
def user_contact(request):
    username = request.user.username
    user_logged_in = True
    return render(request, 'user_contact.html', {'username': username, 'user_logged_in': user_logged_in})


@login_required
def user_termsofuse(request):
    username = request.user.username
    user_logged_in = True
    return render(request, 'user_termsofuse.html', {'username': username, 'user_logged_in': user_logged_in})



def admin_checkuser(request):
    if request.method == 'POST':
        username = request.POST.get('un')
        password = request.POST.get('pswd')

        # Check if a user with the provided email exists (assuming email is used for login)
        users = Admin.objects.filter(email=username)
        if users.exists():
            user = users.first()  # Assuming unique emails
            if password == user.pswd:

                request.session['user_id'] = user.id
                return redirect('admin_user_page')
            else:

                return HttpResponse("Invalid Credentials")
        else:

            return HttpResponse("User does not exist")
    else:

        return render(request, 'register.html')  # Assuming you have a login form template


@login_required
def admin_user_page(request):
    username = request.user.username
    user_logged_in = True
    return render(request, 'admin/admin_user.html', {'username': username, 'user_logged_in': user_logged_in})

@login_required
def passengerlist(request):
    username = request.user.username
    passenger = Passenger.objects.all()
    user_logged_in = True
    return render(request, 'admin/passengerlist.html', {'username': username, 'user_logged_in': user_logged_in, 'passenger':passenger})


@login_required
def ticketlist(request):
    username = request.user.username
    ticket = Tickets.objects.all()
    user_logged_in = True
    return render(request, 'admin/ticketlist.html', {'username': username, 'user_logged_in': user_logged_in, 'tickets':ticket})

