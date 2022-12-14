from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth.views import LogoutView 
from django.urls import path, include
from django.views.generic import TemplateView
from carts.views import cart_detail_api_view
from accounts.views import login_page, register_page, logout_page, guest_register_view
from addresses.views import checkout_address_create_view, checkout_address_reuse_view
from dashboard.views import retorna_total_vendido, relatorio_faturamento, dashboard
from .views import (home_page,  
                    contact_page,
                    RelatorioProdutosView,
)

urlpatterns = [
    path('', home_page, name='home'),
    path('contact/', contact_page, name='contact'),
    path('cart/', include("carts.urls", namespace="cart")),
    path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
    path('checkout/address/reuse/', checkout_address_reuse_view, name='checkout_address_reuse'),
    path('api/cart/', cart_detail_api_view, name='api-cart'),
    path('login/', login_page, name='login'),
    path('register/guest/', guest_register_view, name='guest_register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_page, name='register'),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
    path('search/', include("search.urls", namespace="search")),
    path('products/', include("products.urls", namespace="products")),
    path('dashboard/', dashboard, name='dashboard'),
    path('relatorio-total-vendido/', retorna_total_vendido, name="retorna_total_vendido"),
    path('relatorio-faturamento', relatorio_faturamento, name="relatorio_faturamento"),
    path('relatorio-produtos/', RelatorioProdutosView.as_view(), name='relatorio-produtos'),
    path('restrito/', admin.site.urls),
    path('', include('chat.urls')),
 
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)