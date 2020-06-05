from django.urls import path

from . import views

urlpatterns=[
    
    path('charge/',views.charge,name="charge"),
    path('payment/', views.HomePageView.as_view(), name='Home'),
    path('',views.index,name="Index"),
]