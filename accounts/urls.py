from django.urls import path
from .views import signup_view

urlpatterns = [
    path('signup/', signup_view.as_view(), name='signup'),
]