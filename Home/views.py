from django.shortcuts import render, redirect
from .models import Contact   # IMPORTANT: Model import karna mat bhoolna

def home(request):
    return render(request, 'home.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message
        )

        return redirect("/contact/?success=true")

    return render(request, 'contact.html')

def resume(request):
    return render(request, 'resume.html')

def about(request):
    return render(request, 'about.html')
