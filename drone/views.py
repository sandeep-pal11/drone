from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from contactdata.models import ContactData
from shop.models import Product, Order
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.sessions.models import Session
Session.objects.all().delete()

@login_required
def myaccount(request):
    orders = Order.objects.filter(user=request.user).order_by('-date')
    return render(request, 'myaccount.html', {'orders': orders})
# Home Page

def index(request):
    return render(request, 'index.html')

def get_cart_items(request):
    cart = request.session.get('cart', {})
    cart_items = []

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        cart_items.append({
            'id': product.id,
            'name': product.name,
            'image': product.image.url,
            'price': float(product.price),
            'quantity': quantity,
            'total_price': float(product.price) * quantity
        })

    return JsonResponse({'cart_items': cart_items})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return JsonResponse({'message': 'Product added to cart'})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return JsonResponse({'message': 'Item removed'})

def update_cart(request, product_id, change):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += int(change)
        if cart[product_id] <= 0:
            del cart[product_id]

    request.session['cart'] = cart
    return JsonResponse({'message': 'Cart updated'})

def clear_cart(request):
    request.session['cart'] = {}
    return JsonResponse({'message': 'Cart cleared'})

# Shop Page
def shop(request):
    shopdata = Product.objects.all()
    return render(request, 'shop.html', {'shopdata': shopdata})

# Product Details
def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'productdetails.html', {'product': product})

# About Us Page
def aboutus(request):
    return render(request, 'about.html')

# Blog Page
def blog(request):
    return render(request, 'blog.html')

# Contact Page
def contact(request):
    return render(request, 'contact.html')

# Contact Form Handling
def contactdata(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        number = request.POST.get('number')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactData.objects.create(
            firstname=firstname, lastname=lastname, 
            number=number, email=email, message=message
        )
        messages.success(request, 'Your message has been sent successfully!')

    return render(request, 'contact.html')

# My Account Page
def myaccount(request):
    return render(request, 'myaccount.html')

# My Account 2 Page
def myaccount2(request):
    return render(request, 'myaccount2.html')

# Blog Details Page
def blogdetails(request):
    return render(request, 'blogdetails.html')

# Wishlist Page
def wishlist(request):
    return render(request, 'wishlist.html')

# Compare Page
def compare(request):
    return render(request, 'compare.html')

# Cart Page
def cart(request):
    return render(request, 'cart.html')

# Checkout Page
def checkout(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')

        # Admin ko email bhejna
        send_mail(
            subject='🛒 New Order Received',
            message=f'''
New order placed!

Name: {name}
Email: {email}
Phone: {phone}
Address: {address}, {city}, {state} - {pincode}
            ''',
            from_email='your_email@gmail.com',
            recipient_list=['sandeeppal8471@gmail.com'],
            fail_silently=False,
        )

        messages.success(request, "🎉 Order placed successfully! Admin has been notified.")
        return render(request, 'index.html')  # ✅ Sahi
  # home url name hona chahiye

    return render(request, 'checkout.html')

# Privacy Policy Page
def privacypolicy(request):
    return render(request, 'privacy-policy.html')

# User Registration
def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.warning(request, "Passwords do not match.")
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            messages.warning(request, "Username already exists.")
            return render(request, 'register.html')

        if User.objects.filter(email=email).exists():
            messages.warning(request, "Email already exists.")
            return render(request, 'register.html')

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Your account has been created successfully!")
        return redirect('login')
    
    return render(request, 'login.html')

# User Login
def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, 'Email and Password are required.')
            return render(request, 'login.html')

        user = User.objects.filter(email=email).first()
        if user:
            user = authenticate(request, username=user.username, password=password)
            if user:
                auth_login(request, user)
                messages.success(request, 'Login successful')
                return redirect('/')
            else:
                messages.error(request, 'Invalid email or password, please try again.')
        else:
            messages.error(request, 'Invalid email or password, please try again.')

    return render(request, 'login.html')

# Logout
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login')

# Portfolio Page
def portfolio(request):
    return render(request, 'portfolio.html')

# Not Found (404 Page)
def notfound(request):
    return render(request, '404.html')
