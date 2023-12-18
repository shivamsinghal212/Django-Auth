from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import JsonResponse


class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("request", request.path)
        if request.path == "/api/user/login" or "admin" in request.path:
            response = self.get_response(request)
            return response
        try:
            response = JWTAuthentication().authenticate(request)
        except Exception:
            return JsonResponse({"error": "invalid token"}, status=401)

        if response is not None:
            user, token = response
            request.first_name = user.first_name
            request.last_name = user.last_name
            request.usr = user
        else:
            return JsonResponse({"error": "invalid auth"}, status=401)

        response = self.get_response(request)
        return response
