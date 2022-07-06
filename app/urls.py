from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
from rest_framework import routers
from .views import UserViewSet
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('users', UserViewSet)

app_name = 'app'

urlpatterns = [
    path('register', include(router.urls)),
    path('auth', obtain_auth_token),
    path('category', views.index, name='index'),
    path('', views.home),
    # path('banner', views.banner, name='banner'),
    path('brands', views.brands),
    path('phones', views.phone, name='phone'),
    path('laptops', views.laptop, name='laptop'),
    path('phone/<slug:slug>', views.phone_detail),
    path('laptop/<int:id>', views.laptop_detail),
    path('popular/<slug:slug>', views.popular_details),
    path('popular_products', views.popular_products, name='popular'),
    path('television', views.television, name='telvision'),
    path('tel_detail/<slug:slug>', views.television_detail)
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
