"""
URL configuration for demoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    # path('footer',views.footer),
    path('header',views.header),
    path('login',views.login),
    path('uhome',views.user_home),
    path('adhome',views.admin_home),
    path('view-user',views.view_user),
    path('add_product',views.add_product),
    path('product_details',views.product_details),
    path('edit_product',views.edit_product),
    path('logout_admin',views.logout_admin),
    path('user_logout',views.logout),
    # path('cart/',views.cart1),
    path('cart/',views.display_product),
    path('addcart/<int:pid>',views.addcart),
    path('cart/increment/<int:cart_id>/', views.increment_quantity, name='increment_quantity'),
    path('cart/decrement/<int:cart_id>/', views.decrement_quantity, name='decrement_quantity'),
    path('remove/<int:id>',views.remove_cart),
    path('single_booking/<int:id>',views.single_booking),
    path('book_details',views.booking_dtls)
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)