# from _datetime import datetime
from django.shortcuts import HttpResponse, render, redirect
from post.models import Product, Category, Review
from post.forms import ProductCreateForm, CategoryCreateForm, ReviewCreateForm, ProductCreateForm2
from django.conf import settings
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
  settings.PAGE_SIZE
  if request.method == 'GET':
    product = Product.objects.all()

    search = request.GET.get('search')
    if search:
      product = product.filter(name__icontains=search)

    max_page = product.__len__()/settings.PAGE_SIZE

    if round(max_page)< max_page:
      max_page = round(max_page)+1
    else:
      max_page = round(max_page)

    page = int(request.GET.get('page', 1))

    start = (page - 1) * settings.PAGE_SIZE
    end = page * settings.PAGE_SIZE

    product = product[start:end]


    context = {"products": product,
               "pages": range(1, max_page+1)}

    return render(request, 'products/products.html', context=context)


def category_view(request):
  if request.method == 'GET':
    category = Category.objects.all()

    context = {"categories": category}

    return render(request, 'products/categories.html', context=context)

def product_detail_view(request, p_id):
  if request.method == 'GET':
    try:
      product = Product.objects.get(id=p_id)
    except Product.DoesNotExist:
      return HttpResponse('Page not found')
    context = {"product": product}

    return render(request, 'products/product_detail.html', context=context)

def review_view(request):
  if request.method == 'GET':
    review = Review.objects.all()

    context = {"reviews": review}
  return render(request, 'products/product_detail.html', context=context)


def product_create(request):
  if request.method == 'GET':
    context = {
      "form": ProductCreateForm
    }
    return render(request, 'products/create_product.html', context=context)
  if request.method == 'POST':
    form = ProductCreateForm(request.POST, request.FILES)
    if form.is_valid():
      Product.objects.create(**form.cleaned_data)
      return redirect("/products/")

    context = {
      "form": form
    }
    return render(request, 'products/create_product.html', context=context)

def category_create(request):
  if request.method == 'GET':
    context = {
    "form": CategoryCreateForm
    }
    return render(request, 'products/create_categories.html', context=context)

  if request.method == 'POST':
    form = CategoryCreateForm(request.POST)
    if form.is_valid():
      Category.objects.create(**form.cleaned_data)
      return redirect("/category/")

    context = {
      "forms": form
    }
    return render(request, 'products/create_categories.html', context=context)

def review_create(request):
  if request.method == 'GET':
    context = {
    "form": ReviewCreateForm
    }
    return render(request, 'products/product_detail.html', context=context)

  if request.method == 'POST':
    form = ReviewCreateForm(request.POST)
    if form.is_valid():
      Review.objects.create(**form.cleaned_data)
      return redirect("/products/")

    context = {
      "form": form
    }
    return render(request, 'products/product_detail.html', context=context)

def product_update_view(request, p_id):
  try:
    product = Product.objects.get(id=p_id)
  except Product.DoesNotExist:
    return render(request, 'errors/404.html')

  if request.method == "GET":
    context = {
      "form": ProductCreateForm2(instance=product)
    }
    return render(request, 'products/update.html', context=context)
  if request.method == 'POST':
    form = ProductCreateForm2(
      request.POST,
      request.FILES,
      instance=product
    )

    if form.is_valid():
      form.save()
      return redirect(f'/products/{product.id}/')

    return render(request, 'post/update.html', {"form": form})

