from django.urls import path
from users import views

urlpatterns = [
    path('login', views.login_user, name="login"),
    path('signUp', views.sign_up, name="signup"),
    path('logout', views.log_out, name="logout")
]
