from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']

        #send email

        send_mail(
            name, #subject
            text, #message
            email, #from email
            ['jesicaabijju@gmail.com'], #to email
        )


        return render(request, 'contact.html', {'name':name})
    else:
        return render(request, 'contact.html', {})
    

def about(request):
    return render(request, 'about us.html', {})

def connect(request):
    return render(request, 'connect.html', {})

def signin(request):
    return render(request, 'sign in.html', {})
