from django.urls import path,include
from .views import SignupPageView

urlpatterns=[

 #la ruta accounts/ es obligatorio 
path("accounts/", include("django.contrib.auth.urls")),
path("signup",SignupPageView.as_view(),name="signup"),

]