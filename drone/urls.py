from django.contrib import admin
from django.urls import path, include
from drone import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('shop/', views.shop, name="shop"),
    path('productdetails/<int:product_id>/', views.product_details, name='product_details'),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('myaccount/', views.myaccount, name="myaccount"),
    path('contactdata/', views.contactdata, name="contactdata"),  
    path('blogdetails/', views.blogdetails, name="blogdetails"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('compare/', views.compare, name="compare"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('privacypolicy/', views.privacypolicy, name="privacypolicy"),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name="logout"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('myaccount/', views.myaccount, name="myaccount"),
    path('notfound/', views.notfound, name="notfound"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
