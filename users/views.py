from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .helpers import check_user_group

from inventory.models import Product, Company

from users.models import PhoneNumber, UserInventory, CreditCard


@csrf_exempt
def login_user(request, template_name="templates/login.html"):
    if request.user.is_authenticated:
        return redirect("products")
    if request.method == 'GET':
        return render(request, template_name)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if check_user_group(user, "Seller") and Company.objects.filter(user=user).exists():
                return JsonResponse({"message": "success_seller"}, status=200)
            elif check_user_group(user, "Seller") and not Company.objects.filter(user=user).exists():
                return JsonResponse({"message": "success_create"}, status=200)
            else:
                return JsonResponse({"message": "success"}, status=200)
        else:
            return JsonResponse({"message": "error"}, status=200)


def sign_up(request, template_name="templates/sign_up.html"):
    if request.user.is_authenticated:
        return redirect("products")
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


def edit_user(request, pk, template_name="templates/edit_user.html"):
    if request.method == "GET":
        return render(request, template_name)
    elif request.method == 'POST':
        user = User.objects.filter(id=pk).update(
            username=request.POST.get("username"),
            password=request.POST.get("password"),
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            email=request.POST.get("email"),
        )
        phone = PhoneNumber.objects.update(
            phone_number=request.POST.get("phone_number")
        )
        # user.objects.save()
        return JsonResponse({"message": "success"}, status=200)


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("login")


def profile_info(request, pk, template_name="templates/profile.html"):
    data = {}

    user = User.objects.get(id=pk)
    print(user)
    print(check_user_group(user, "Seller"))
    if PhoneNumber.objects.filter(user=user).exists():
        phone_number = PhoneNumber.objects.get(user=user)
    else:
        phone_number = None

    data["user"] = user
    data["phone_number"] = phone_number

    return render(request, template_name, data)


def reset_password(request, pk, template_name="templates/resetpassword.html"):
    if request.method == 'GET':
        return render(request, template_name)
    elif request.method == 'POST':
        user = User.objects.filter(id=pk).update(
            password=request.POST.get("new_password"),
            confirm_password=request.POST.get("confirm_password"),
        )
        return JsonResponse({"message": "success"}, status=200)


@csrf_exempt
def buy_product(request):
    if request.method == "POST":
        print("request here ->", request.POST.get("test_parameter"))
        product = Product.objects.get(id=request.POST.get('product'))

        inventory = UserInventory.objects.create(
            user=request.user,
            product=product
        )
        return JsonResponse({"message": "success"}, status=200)


def personal_inventory(request, template_name="templates/user_inventory.html"):
    # if request.method == "POST":
    #     tag = request.method.get("tag")
    #     products = Product.objects.filter(tag=tag)
    #     filtered_products = serialize("json", products)
    #     return JsonResponse({"message": "success", "filtered_products": filtered_products})
    data = {}
    user = request.user
    inventory = UserInventory.objects.filter(user=user)

    data["inventory"] = inventory

    return render(request, template_name, data)


def sign_up_seller(request, template_name="templates/sign_up_seller.html"):
    if request.method == "GET":
        return render(request, template_name)

    if request.method == "POST":
        user = User.objects.create_user(
            username=request.POST.get("username"),
            password=request.POST.get("password"),
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            email=request.POST.get("email")
        )
        phone_number = PhoneNumber.objects.create(
            phone_number=request.POST.get("phone_number")
        )
        return JsonResponse({"message": "success"}, status=200)


def register_card(request, template_name="templates/register_card.html"):
    if request.method == "GET":
        data = {"user": request.user}
        return render(request, template_name, data)
    if request.method == "POST":
        register = CreditCard.objects.create(
            card_holder=request.user,
            credit_card_number=request.POST.get("credit_card_number"),
            expiration_date=request.POST.get("expiration_date"),
            cvv_code=request.POST.get("cvv_code"),
            credit_card_limit=request.POST.get("credit_card_limit"),
            bilance=request.POST.get("bilance")
        )
        return JsonResponse({"message": "success"}, status=200)


def confirm_payment(request, pk, template_name="confirm_payment.html"):
    data = {}
    if request.method == "GET":
        user = request.user
        creditcard = CreditCard.objects.filter(card_holder=user).get()
        product = Product.objects.get(id=pk)
        # product = Product.objects.get(id=request.POST.get('product'))
        data["creditcard"] = creditcard
        data["product"] = product

        return render(request, template_name, data)





