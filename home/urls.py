from  . import views
from django.urls import path


app_name = 'home'
urlpatterns = [
    
    
    path('', views.Home.as_view(), name='home'),
    path('comingsoon', views.ComingSoon.as_view(), name='comingsoon'),
    path('service', views.Service.as_view(), name='service'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('career', views.Career.as_view(), name='career'),
    path('mytest', views.MyTest.as_view(), name='mytest'),
    path('sugar/<int:cat_id>/', views.Sugar.as_view(), name='sugar'),
    path('privacy_policy', views.PrivacyPolicy.as_view(), name='privacy_policy'),
    path('terms', views.Terms.as_view(), name='terms'),
    path('success_sent', views.SuccessSent.as_view(), name='success_sent'),
   
]
