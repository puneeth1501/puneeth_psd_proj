from django.http import HttpResponse

def home_page(request):
    return HttpResponse('<h1 style="color:red;">Hi, am Puneeth Chowdary!</h1>')