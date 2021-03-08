from django.shortcuts import render
from django.http import request
from django.core.mail import send_mail
from django.conf import settings


def ContactView(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        message_comment = request.POST['message-comment']
        msg_mail = str(message) + "\n " + str(message_comment) + "\nFrom " + str(message_email)

        send_mail(
            "Contacted by " + message_name,
            msg_mail, 
            message_email, 
            [settings.EMAIL_HOST_USER],
            fail_silently=False
            )
        return render(request, 'contact.html', {'message_name':message_name,
                                                'message_email': message_email,
                                                'message': message,
                                                'message_comment': message-comment})
    else:
        return render(request, 'contact.html', {})
