from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage,name='homapage'),
    path('signup/',views.signup_page,name='signup'),
    path('login/',views.login_page,name='login_page'),
    path('check_username/', views.check_username, name='check_username'),
    path('viewuserdetails/', views.signup_view, name='viewuserdetails'),
    path('signup_view/', views.signup_view, name='signup_view'),
    path('meeting/',views.meeting,name='meeting'),
    path('login_view/', views.login_view, name='login_view'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
]