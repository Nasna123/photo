from django.urls import path
from.import views

urlpatterns=[
    path('page1/',views.fun1,name='page1'),
    path('home/',views.home,name='home'),
    path('img/',views.img,name='img'),
    path('about/',views.about,name='about'),
]