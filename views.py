from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
import random
def Homepage(request):
    return render(request,'Homepage.html')

def home(request):
    return render(request,'home.html')


from django.shortcuts import render

def homepage(request):
    return render(request, 'Homepage.html')

def design(request):
    return render(request,'design.html')

def cart(request):
    return render(request,'cart.html')



def service(request):
    return render(request,'service.html')
def details(request):
    return render(request,'details.html')


def chatbot(request):
    return render(request,'chatbot.html')

def About(request):
    return render(request,'About.html')



def life(request):
    return render(request,'life.html')
