


from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from accounts.serializers import AccountsSerializer, RegisterSerializer


class AccountsView(APIView):
    def post(self, request):
        
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            jwt = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(jwt)
            access_token = str(jwt.access_token)
            return Response(data = {
                "user": serializer.data,
                "message": "register success",
                "token": {
                    "access": access_token,
                    "refresh": refresh_token
                }
            }, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk):
        
        users = User.objects.all()
        serializer = AccountsSerializer(users, many=True)
        return Response(data=serializer.data)
    
    def delete(self, request, pk):
        user = User.objects.get(id=pk)
        user.delete()
        return Response(data={"message": "success"}, status=status.HTTP_200_OK)
    def put(self, request, pk):
        user = get_object_or_404(User, id=pk)
        serializer = RegisterSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)