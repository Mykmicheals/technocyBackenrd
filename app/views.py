from unicodedata import name
from urllib import response
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from yaml import serialize
from .models import Brand, Category, Phone, Laptops, Banner, PopularProducts, Television
from .serializer import BrandSerializer, CategorySerializer, PhoneSerializer, LaptopSerializer, PopularProductsSerializer, UserSerializer, TelevisionSerializer
from django.views.decorators.csrf import csrf_protect

from rest_framework import viewsets

from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def home(request):
    return render(request, 'index.html')


def index(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return JsonResponse(serializer.data, safe=False)


def brands(request):
    brands = Brand.objects.all()
    serializer = BrandSerializer(brands, many=True)
    return JsonResponse(serializer.data, safe=False)


def phone(request):
    if request.method == 'GET':
        phones = Phone.objects.all()
        serializer = PhoneSerializer(phones, many=True)
        return JsonResponse(serializer.data, safe=False)


# def product_cat(request):
#     query = request.GET.get('category')
#     print(query)
#     products = PopularProducts.objects.filter(category__name='Gaming')
#     serializer = PopularProductsSerializer(products, many=True)
#     return JsonResponse(serializer.data, safe=False)


def phone_detail(request, slug):
    phone = Phone.objects.get(slug=slug)
    if request.method == 'GET':
        serializer = PhoneSerializer(phone)
        return JsonResponse(serializer.data)


def popular_products(request):
    if request.method == 'GET':
        popular = PopularProducts.objects.all()
        serializer = PopularProductsSerializer(popular, many=True)
        return JsonResponse(serializer.data, safe=False)


def popular_details(request, slug):
    if request.method == 'GET':
        popular = PopularProducts.objects.get(slug=slug)
        serializer = PopularProductsSerializer(popular)
        return JsonResponse(serializer.data, safe=False)


def laptop(request):
    if request.method == 'GET':
        laptops = Laptops.objects.all()
        serializer = LaptopSerializer(laptops, many=True)
        return JsonResponse(serializer.data, safe=False)


def laptop_detail(request, slug):
    laptop = Phone.objects.get(slug=slug)
    if request.method == 'GET':
        serializer = LaptopSerializer(laptop)
        return JsonResponse(serializer.data)


# def banner(request):
#     if request.method == 'GET':
#         banner = Banner.objects.all()
#         serializer = BannerSerializer(banner, many=True)
#         return JsonResponse(serializer.data, safe=False)


def television(request):
    if request.method == 'GET':
        tel = Television.objects.all()
        serializer = TelevisionSerializer(tel, many=True)
        return JsonResponse(serializer.data, safe=False)


def television_detail(request, slug):
    if request.method == 'GET':
        tel = get_object_or_404(Television, slug=slug)
        serializer = TelevisionSerializer(tel)
        return JsonResponse(serializer.data, safe=False)
