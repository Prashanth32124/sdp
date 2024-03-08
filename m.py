# views.py

import random
from django.core.mail import send_mail
from django.shortcuts import render

def send_otp(request):
    # Generate a random 6-digit OTP
    otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])

    # Send OTP to the user's email address
    send_mail(
        'Your OTP',  # Subject
        f'Your OTP is: {otp}',  # Message
        'mudunuriprashnth143@gmail.com',  # From email address
        ['rmudunnuriprashanth143@gmail.com'],  # To email address
        fail_silently=False,
    )

    # For demonstration purposes, you might want to store the OTP in the session or database for verification later
    request.session['143143'] = otp

    return render(request, 'otp_sent.html')
