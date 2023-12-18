from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response  # Create your views here.
from .models import CustomUser
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user


@api_view(["POST"])
def login(request):
    user_name = request.data.get("username", "")
    password = request.data.get("password", "")

    if not user_name or not password:
        return Response(status=400)

    # check for superuser
    try:
        user_obj = CustomUser.objects.get(username=user_name)
    except CustomUser.DoesNotExist:
        return Response(status=400)

    pwd_valid = check_password(password, user_obj.password)

    if pwd_valid:
        # create jwt token
        refresh = RefreshToken.for_user(user_obj)

        resp = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
    else:
        resp = {
            "error": "invalid username or password",
        }
    return Response(resp)


@api_view(["GET"])
def profile(request):
    return Response(
        {"first_name": request.usr.first_name, "last_name": request.usr.last_name}
    )
