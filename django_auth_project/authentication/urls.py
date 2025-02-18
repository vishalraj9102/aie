from django.urls import path
from .views import RegisterView, VerifyRegistrationView, LoginView, UserDetailsView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('register/verify/', VerifyRegistrationView.as_view(), name='verify-registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('me/', UserDetailsView.as_view(), name='user-details'),
    path('logout/', LogoutView.as_view(), name='logout'),
]