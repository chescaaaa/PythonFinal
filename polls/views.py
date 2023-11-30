from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello motherfather.")

def sample(request):
    context = {
        "user_fullname" : "Chiwa",
        "greetings" : "Hiiii",
        "skills" : {"tulog", "kain"}
    }
    return render(request, 'template.html', context)