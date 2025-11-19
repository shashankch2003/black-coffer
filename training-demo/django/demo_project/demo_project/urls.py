from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def hello(request):
    return JsonResponse({"message": "Hello from Django demo!"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
]
