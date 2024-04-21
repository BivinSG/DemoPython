from . import views
from django.urls import path

urlpatterns = [

    # path('',views.demo,name='demo'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
    # path('operations/',views.addition,name='operations')
    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact')
]
