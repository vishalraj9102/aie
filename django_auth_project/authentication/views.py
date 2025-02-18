from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from django.http import JsonResponse
from .models import User
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserDetailsSerializer
from .utils import generate_otp, send_email
from django.views.decorators.csrf import csrf_protect
from rest_framework.permissions import AllowAny

class RegisterView(APIView):
    permission_classes = [AllowAny]  # Allow registration for new users

    def post(self, request):
        # CSRF token is handled automatically by Django Rest Framework
        csrf_token = get_token(request)  # Optional: Add this if you need to manually handle it
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            otp = generate_otp()
            try:
                send_email(email, f"Your OTP is: {otp}")
            except Exception as e:
                return Response({'error': f'Failed to send OTP: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            request.session['otp'] = otp
            request.session['email'] = email
            request.session['password'] = password
            return Response({'message': 'OTP sent to email', 'csrf_token': csrf_token}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        csrf_token = get_token(request)  # Optional: Add this if you need to manually handle it
        otp = request.data.get('otp')
        if otp == str(request.session.get('otp')):
            email = request.session.get('email')
            password = request.session.get('password')
            if not User.objects.filter(email=email).exists():
                user = User.objects.create_user(email=email, password=password)
                return Response({'message': 'Registration successful', 'csrf_token': csrf_token}, status=status.HTTP_201_CREATED)
            return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        csrf_token = get_token(request)  # Optional: Add this if you need to manually handle it
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                response = JsonResponse({'message': 'Login successful'})
                response.set_cookie('auth_token', user.id, httponly=True, secure=False)
                response['X-CSRFToken'] = csrf_token  # Include CSRF token in the response
                return response
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserDetailsSerializer(request.user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        response = Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
        response.delete_cookie('auth_token')
        return response
