from rest_framework.decorators import api_view
from rest_framework.response import Response  # Create your views here.
from .models import CustomUser
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from .serializers import CustomUserSerializer


@api_view(["POST"])
def login(request):
    user_name = request.data.get("username", "")
    password = request.data.get("password", "")
    status = 200
    if not user_name or not password:
        return Response({"error": "Username or password cannot be null"}, status=400)
    try:
        user_obj = CustomUser.objects.get(username=user_name)
    except CustomUser.DoesNotExist:
        return Response({"error": "User does not exist"}, status=400)

    pwd_valid = check_password(password, user_obj.password)

    if pwd_valid:
        # create jwt token
        refresh = RefreshToken.for_user(user_obj)

        resp = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
    else:
        status = 401
        resp = {
            "error": "invalid username or password",
        }
    return Response(resp, status=status)


@api_view(["GET"])
def profile(request):
    serializer = CustomUserSerializer(request.usr)
    return Response(serializer.data)


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing all/single user instances.
    usage: /api/user/ , /api/user/<id>
    """

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
