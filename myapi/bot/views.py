from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TelegramUser
from .serializers import TelegramUserSerializer


class RegisterUserView(APIView):
    def post(self, request):
        serializer = TelegramUserSerializer(data=request.data)
        if serializer.is_valid():
            # Проверяем, существует ли пользователь с таким user_id
            user_id = serializer.validated_data.get('user_id')
            if TelegramUser.objects.filter(user_id=user_id).exists():
                user = TelegramUser.objects.get(user_id=user_id)
                return Response(
                    TelegramUserSerializer(user).data,
                    status=status.HTTP_200_OK
                )

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
