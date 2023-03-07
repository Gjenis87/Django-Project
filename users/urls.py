from django.urls import path
from users import views

urlpatterns = [
    path('login', views.login_user, name="login"),
    path('signUp', views.sign_up, name="signup"),
    path('logout', views.log_out, name="logout"),
    path('edit/<int:pk>', views.edit_user, name="edit"),
    path('profile/<int:pk>', views.profile_info, name="profile"),
    path('reset/<int:pk>', views.reset_password, name="reset"),
]
