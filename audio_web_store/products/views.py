from django.shortcuts import render
from .models import Product

def products_home_view(request):

    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "products/home.html", context)
