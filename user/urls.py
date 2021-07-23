from django.contrib.auth import logout
from django.urls import path
from . import views
app_name = "user"

urlpatterns = [
    path('register/',views.userregister,name="register"),
    path('login/',views.userlogin,name="login"),
    path("logout/",views.userlogout, name="logout")
]
