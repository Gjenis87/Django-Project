from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

from users.models import PhoneNumber


def login_user(request, template_name="templates/login.html"):
    if request.method == 'GET':
        return render(request, template_name)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "success"}, status=200)
        else:
            return JsonResponse({"message": "error"}, status=200)


def sign_up(request, template_name="templates/sign_up.html"):

    if request.method == 'GET':
        return render(request, template_name)
    elif request.method == 'POST':
        if not request.POST.get("phone_number").isdigit():
            return JsonResponse({"message": "error"}, status=200)
        user = User.objects.create_user(
            username=request.POST.get("username"),
            password=request.POST.get("password"),
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            email=request.POST.get("email"),
        )

        PhoneNumber.objects.create(
            phone_number=request.POST.get("phone_number"),
            country_code=request.POST.get("country_code"),
            user=user

        )
        return JsonResponse({"message": "success"}, status=200)
