from _datetime import datetime
from django.shortcuts import HttpResponse, render
from post.models import Product, Category
# def hello_view(request):
#   if request.method == 'GET':
#     return HttpResponse("Hello! Its my project,hjhj ")
#
# def current_date_view(request):
#   if request.method == 'GET':
#     current_date = datetime.now().strftime("%Y-%m-%d")
#     return HttpResponse(f"Current date: {current_date}")
#     # return HttpResponse(f'current date ')
#
# def goodbye_view(request):
#   if request.method == 'GET':
#     return HttpResponse("Goodbye user!")

def main_view(request):
  if request.method =='GET':
    product = Product.objects.all()
    return render(request, 'index.html')

def products_view(request):
  if request.method == 'GET':
    product = Product.objects.all()

    context = {"products": product}

    return render(request, 'products/products.html', context=context)


def category_view(request):
  if request.method == 'GET':
    category = Category.objects.all()

    context = {"categories": category}

    return render(request, 'products/categories.html', context=context)
