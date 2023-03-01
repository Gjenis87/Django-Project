from django.http import JsonResponse
from django.shortcuts import render, redirect
from inventory.models import Product, Company

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def home(request, template_name="templates/home.html"):
    my_dict = {
        "first_name": "Gjenis",
        "last_name": "Alkovaq",
        "age": "22",
        "country": "Kosova",
        "flag": False,
    }

    return render(request, template_name, my_dict)


@csrf_exempt
def create_product(request, template_name="templates/create_Product.html"):
    if request.method == "GET":
        return render(request, template_name)
    elif request.method == "POST":
        product = Product.objects.create(
            name=request.POST.get("name"),
            price=request.POST.get("price"),
            barcode=request.POST.get("barcode"),
            expiry_date=request.POST.get("expiry_date"),
            quantity=request.POST.get("quantity"),
            tag=request.POST.get("quantity"),
            description=request.POST.get("description")
        )
        company = Company.objects.create(
            company_name=request.POST.get("company_name"),
            product=product,
        )

        return JsonResponse({"message": "success"}, status=200)


def product_list(request, template_name="templates/productsLists.html"):
    data = {}
    products = Product.objects.filter()
    data["products"] = products

    return render(request, template_name, data)


def edit_product(request, pk, template_name="templates/edit_Product.html"):

    if request.method == "GET":
        data = {}
        product = Product.objects.get(pk=pk)
        data["product"] = product
        return render(request, template_name, data)

    if request.method == "POST":
        product = Product.objects.filter(id=pk).update(
            name=request.POST.get("name"),
            price=request.POST.get("price"),
            barcode=request.POST.get("barcode"),
            expiry_date=request.POST.get("expiry_date"),
            quantity=request.POST.get("quantity"),
            tag=request.POST.get("tag"),
            description=request.POST.get("description"),
        )
        company = Company.objects.create(
            company_name=request.POST.get("company_name")
        )

        return JsonResponse({"message": "success"}, status=200)


def single_product(request, pk, template_name="templates/single_product.html"):
    data = {}
    product = Product.objects.get(pk=pk)
    companies = Company.objects.filter(product=product)

    data["product"] = product
    data["companies"] = companies

    return render(request, template_name, data)


def delete_product(request, pk):

    # if request.method == "DELETE":
    product = Product.objects.filter(id=pk)
    product.delete()

    return redirect("products")
