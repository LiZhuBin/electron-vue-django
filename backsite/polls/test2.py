# Create your views here.
from django.http import HttpResponse
from . import models
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
print(models.Client.objects.all())