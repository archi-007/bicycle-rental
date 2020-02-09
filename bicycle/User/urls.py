from django.urls import path,include
from django.contrib.auth import views as auth_views
from User import views


app_name='User'
urlpatterns = [
    path('sign-in/',auth_views.LoginView.as_view(),name='sign-in'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout', auth_views.LogoutView.as_view(), {'next_page': '/index.html/'}),
]
