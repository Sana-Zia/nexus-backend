from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
            "role": user.role,
            "bio": user.bio,
            "startup_info": user.startup_info,
            "investment_info": user.investment_info,
        })

    def put(self, request):
        user = request.user

        user.bio = request.data.get("bio", user.bio)
        user.startup_info = request.data.get("startup_info", user.startup_info)
        user.investment_info = request.data.get("investment_info", user.investment_info)

        user.save()

        return Response({"message": "Profile updated successfully"})