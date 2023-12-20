from django.urls import path
from . import views

urlpatterns = [
    path("sign-in/", views.sign_in, name='sign_in'),
    path("sign-up/", views.sign_up, name="sign_up"),
    path("logout/", views.log_out, name='logout')
]
