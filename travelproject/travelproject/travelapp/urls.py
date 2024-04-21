from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    # path('operations/',views.addition,name='operations')
    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact')
]
