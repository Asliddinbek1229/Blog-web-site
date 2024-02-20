from django.urls import path
from .views import SignUpView, logout_func

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', logout_func, name='logout'),
]