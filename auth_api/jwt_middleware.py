from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import JsonResponse


def is_url_auth_excluded(url):
    return url.startswith(("/api/user/login", "/admin"))


class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if is_url_auth_excluded(request.path):
            response = self.get_response(request)
            return response
        try:
            response = JWTAuthentication().authenticate(request)
        except Exception:
            return JsonResponse({"error": "invalid token"}, status=401)

        if response is not None:
            user, token = response
            request.usr = user
        else:
            return JsonResponse({"error": "invalid auth"}, status=401)

        response = self.get_response(request)
        return response
