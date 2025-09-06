from django.urls import path
from django.http import HttpResponse

def test_view(request):
    return HttpResponse("Test response from role app")

urlpatterns = [
    path('test/', test_view, name='test'),
]