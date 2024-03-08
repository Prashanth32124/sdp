from django.urls import path
from . import views

urlpatterns = [
    path('Homepage/', views.Homepage, name='Homepage'),
    path('', views.home, name='home'),
    path('home', views.Homepage, name='homepage'),  # Consider removing this duplicate pattern
path('design/', views.design, name='design'),
path('cart/', views.cart, name='cart'),
path('details/', views.details, name='details'),
path('service/', views.service, name='service'),
path('Homepage/design',views.design,name='design'),
path('Homepage/details/', views.details, name='details'),
path('chatbot/', views.chatbot, name='chatbot'),
path('service/home/',views.home,name='home'),
path('service/home/service',views.service,name='service'),
path('About',views.About,name='About'),
path('service/home/About',views.About,name='About'),
path('About/home/About',views.About,name='About'),
path('life',views.life,name='life'),
path('design/details',views.details,name='details'),
]
