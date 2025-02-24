from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

import midtransclient, random,string
# Create your views here.

def index(request):
    product = Product.objects.all()[:3]
    return render(request, "pages/index.html", {"product":product})

def signin(request):
    form = LoginForm(data=request.POST)

    if form.is_valid():
        login(request, form.get_user())
        return redirect("index")
    return render(request, "pages/login.html", {"form":form})

def signup(request):
    form = RegisterForm(data=request.POST)

    if form.is_valid():
        form.save()
        return redirect("signin")
    return render(request, "pages/register.html", {"form":form})

def cart(request):
    snap = midtransclient.Snap(
        is_production=False,
        server_key="SB-Mid-server-Be5vrLDGnPYgEh8n28XsS2OP",
        client_key="SB-Mid-client-SoPv4O1s4b0CkuXH"
    )
    order_id = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    cart = request.session.get('cart', [])
    total_price = sum(int(item["price"]) * item['quantity'] for item in cart)
    token = snap.create_transaction_token({
        "transaction_details": {
            "order_id": order_id,
            "gross_amount": int(total_price)
        }, 
        "credit_card":{
            "secure" : True
        },
    })
    return render(request, "pages/cart.html", {"cart": cart, "total_price":total_price, "token":token, "client_key":"SB-Mid-client-SoPv4O1s4b0CkuXH"})

def allproduct(request):
    product = Product.objects.all()
    return render(request, "pages/product.html",{"product":product})

@login_required
def add_to_cart(request, product_id):
    if request.method == "POST":
        product = Product.objects.get(id=product_id)

        if 'cart' not in request.session:
            request.session['cart'] = []

        cart = request.session['cart']
        for item in cart:
            if item['id'] == product.id:
                item['quantity'] += 1
                break
        else:
            cart.append({'id': product_id, 'name': product.nama, 'stock':product.stok,'image':product.gambar.url,'price': str(product.harga), 'quantity': 1, 'category':product.kategori})

        request.session['cart'] = cart

        return redirect('cart')

@login_required
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])
    cart = [item for item in cart if item['id'] != product_id]

    request.session['cart'] = cart

    return redirect('cart')