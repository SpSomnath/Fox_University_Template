from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render(request, 'home.html')


def send_email(request):
    subject = 'Werlcome Fox university'
    message = 'Welcome to CodeOn family Hi, There you have successfully subscribed us. All new update you will recive first'
    email_from = settings.EMAIL_HOST_USER
    username = request.GET.get('email')
    recipient_list = [username]
    send_mail( subject, message, email_from,  recipient_list, fail_silently=False,)

    return redirect('/')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')

def staff(request):
    return render(request, 'staff.html')

def blog(request):
    return render(request, 'blog.html')

def applyNow(request):
    return render(request, 'applyNow.html')

def courses(request):
    return render(request, 'courses.html')