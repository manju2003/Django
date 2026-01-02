from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def course_detail(request):
    return render(request, "course_detail.html")

def request_callback(request):
    return render(request,"request-callback.html")