from django.http.request import HttpRequest
from inertia import render

def home_view(request: HttpRequest):
    return render(request, "Home", props={"text": "Props from Django Server!"})


def about_view(request: HttpRequest):
    return render(request, "About", props={"text": "Props from Django Server!"})