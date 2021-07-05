from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        # send email
        send_mail(
            subject,  # subject
            message,  # message
            email,  # from email
            ['hardeyslim@gmail.com', 'funsho.adeosun01@gmail.com'],
        )

        return render(request, 'contact.html', {"name":name})
    else:
        return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')


def reservation(request):
    return render(request, 'make_reservation.html')
