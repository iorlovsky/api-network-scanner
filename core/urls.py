from django.urls import path

from core.views import users

urlpatterns = [
    path('login/', users.SigninView.as_view()),
    path('signup/', users.SignupView.as_view()),
]