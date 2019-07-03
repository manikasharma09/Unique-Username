from django.conf.urls import url
from app import views
from django.urls import path,include

urlpatterns = [
    path('signup/', views.SignUpView.as_view()),
    path('validate_username/',views.validate_username),
]