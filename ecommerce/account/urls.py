from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),

    # urls de verificacao de email

    # url de verificacao de email
    path('email-verification', views.email_verification, name='email-verification'),


    # url de verificacao de email enviada
    path('email-verification-sent', views.email_verification_sent,
         name='email-verification-sent'),


    # url de verificacao de email sucesso
    path('email-verification-success', views.email_verification_success,
         name='email-verification-success'),


    # url de verificacao de email falhou
    path('email-verification-failed', views.email_verification_fail,
         name='email-verification-failed'),



]
