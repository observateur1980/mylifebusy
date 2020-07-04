from  . import views
from django.urls import path


app_name = 'home'
urlpatterns = [
    
    
    path('', views.Home.as_view(), name='home'),
    path('button', views.Button.as_view(), name='button'),
    path('card', views.Card.as_view(), name='card'),
    path('color', views.Color.as_view(), name='color'),
    path('border', views.Border.as_view(), name='border'),
    path('animation', views.Animation.as_view(), name='animation'),
    path('other', views.Other.as_view(), name='other'),
    path('chart', views.Chart.as_view(), name='chart'),



    path('contact_list', views.ContactList.as_view(), name='contact_list'),
    path('contact_detail/<int:pk>', views.ContactDetail.as_view(), name='contact_detail'),
    path('contact_create', views.ContactCreate.as_view(), name='contact_create'),
    path('contact_update/<int:pk>', views.ContactUpdate.as_view(), name='contact_update'),
    path('contact_delete/<int:pk>', views.ContactDelete.as_view(), name='contact_delete'),


    # path('comingsoon', views.ComingSoon.as_view(), name='comingsoon'),
    # path('service', views.Service.as_view(), name='service'),
    # path('contact', views.Contact.as_view(), name='contact'),
    # path('career', views.Career.as_view(), name='career'),
    # path('mytest', views.MyTest.as_view(), name='mytest'),
    # path('sugar/<int:cat_id>/', views.Sugar.as_view(), name='sugar'),
    # path('privacy_policy', views.PrivacyPolicy.as_view(), name='privacy_policy'),
    # path('terms', views.Terms.as_view(), name='terms'),
    # path('success_sent', views.SuccessSent.as_view(), name='success_sent'),
   
]
