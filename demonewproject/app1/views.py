from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
from .models import *
def header(request):
    return render(request,'header.html')

def index(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        dob=request.POST['dob']
        address=request.POST['address']
        username=request.POST['username']
        password=request.POST['password']
        d=register(name=name,email=email,dob=dob,address=address,username=username,password=password)
        d.save()
        messages.success(request,"Profile Details added")
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            data=register.objects.get(username=username)
            if username==data.username and password==data.password:
                request.session['id']=username
                return redirect(user_home)
            else:
                messages.error(request,'Invalid Username or Password')
        except Exception:
            if username == 'admin' and password == 'admin':
                request.session['id1'] = username
                return redirect(admin_home)
            else:
                messages.error(request, 'Invalid Username or Password')
    return render(request,'login.html')

def user_home(request):
    if 'id' in request.session:
        user=register.objects.get(username=request.session['id'])
        l=[]
        datas=''
        try:
            datas = Cart.objects.filter(user_details=user)
            d1=datas
            print(datas)
            for i in datas:
                l.append(i.product_details)
        except:
            pass
        data=product.objects.all()
        print(l)
        return render(request,'user-home.html',{'data':data,'datas':l,'d1':d1})
    return redirect(login)

def admin_home(request):
    if 'id1' in request.session:
        return render(request,'admin-home.html')
    return redirect(login)

def view_user(request):
    if 'id1' in request.session:
        data=register.objects.all()
        print(data)
        return render(request,'view-user.html',{'d':data})
    return redirect(login)

def add_product(request):
    if 'id1' in request.session:
        if request.method=='POST':
            pid=request.POST['pid']
            pname=request.POST['pname']
            price=request.POST['price']
            quantity=request.POST['quantity']
            pimg=request.FILES['pimg']
            data=product(pid=pid,pname=pname,price=price,quantity=quantity,image=pimg)
            data.save()
            messages.success(request, 'Product Added Successfully...')
            return redirect(add_product)
        return render(request,'add-product.html')
    return redirect(login)

def product_details(request):
    if 'id1' in request.session:
        data=product.objects.all()
        return render(request,'product-details.html',{'data':data})
    return redirect(login)

def edit_product(request):
    if 'id1' in request.session:
        if request.method=='POST':
            pid=int(request.POST['pid'])
            pname=request.POST['pname']
            price=request.POST['price']
            quantity=request.POST['quantity']
            pimg=request.FILES['pimg']
            product.objects.filter(pid=pid).update(pname=pname,price=price,quantity=quantity,image=pimg)
            messages.success(request, 'Product Updated Successfully...')
            return redirect(product_details)
        data = product.objects.all()
        return render(request,'edit-product.html',{'data':data})
    return redirect(login)

def logout_admin(request):
    if 'id1' in request.session:
        request.session.flush()
        return redirect(login)

def cart1(request):
    if 'id' in request.session:
        user = register.objects.get(username=request.session['id'])
        datas = Cart.objects.filter(user_details=user)
        print(datas,user)
        return render(request,'cart.html',{'d1':datas})
    return redirect(login)

def addcart(request, pid):
    if 'id' in request.session:
        u=register.objects.get(username=request.session['id'])
        print(u)
        item=product.objects.get(pk=pid)
        print(item)
        data=Cart(product_details=item,user_details=u,total_price=item.price)
        data.save()
        messages.success(request,'Cart added successfully')
        return redirect(display_product)
    return redirect(login)

def display_product(request):
    if 'id' in request.session:
        u=register.objects.get(username=request.session['id'])
        b=Cart.objects.filter(user_details=u)
        qty=1
        total=0
        for i in b:
            total+=i.product_details.price*i.quantity
        return render(request,'display-product.html',{'data':b,'total':total})
    return redirect(login)


def increment_quantity(request, cart_id):
    
    cart_item = Cart.objects.get(pk=cart_id)
    if cart_item.product_details.quantity > 1:
        cart_item.quantity += 1
        cart_item.save()
        cart_item.total_price=cart_item.quantity*cart_item.product_details.price
        cart_item.save()
   

    return redirect(display_product)

def decrement_quantity(request, cart_id):
    cart_item = Cart.objects.get(pk=cart_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect(display_product)

def logout(request):
    if 'id' in request.session or 'id1' in request.session:
        request.session.flush()
        return redirect(login)

def file(request):
    return render(request,'file_upload.html')

def remove_cart(req,id):
    data=Cart.objects.get(pk=id)
    data.delete()
    return redirect(display_product)


def single_booking(re,id):
    item=product.objects.get(pk=id)
    if re.method=='POST':
        qty=int(re.POST['qty'])
        t_price=re.POST['total_price']
        item.quantity-=qty
        item.save()
        import datetime
        a=datetime.datetime.now().strftime("%Y-%m-%d")
        print(a)
        user=register.objects.get(username=re.session['id'])
        book=bookings.objects.create(date=a,user_details=user,item_details=item,quantity=qty,total_price=t_price)
        book.save()
        return redirect(user_home)
    return render(re,'booking_form.html',{'item':item})

def booking_dtls(re):
    user=register.objects.get(username=re.session['id'])
    book=bookings.objects.filter(user_details=user)
    return render(re,'bookings.html',{'bookings':book})

def multiple_booking(re):
    user=register.objects.get(username=re.session['id'])
    items=Cart.objects.filter(user_details=user)

    return render(re,'booking_multiple.html',{'items':items})
def buynow(req):
    user=register.objects.get(username=req.session['id'])
    items=Cart.objects.filter(user_details=user)
    import datetime
    a=datetime.datetime.now().strftime("%Y-%m-%d")
    for i in items:
        item=product.objects.get(pk=i.product_details.pk)
        print(item.pname)
        data=bookings.objects.create(user_details=user,item_details=item,quantity=i.quantity,total_price=i.total_price,date=a)
        data.save()
    messages.success(req,'all cart items are booked')
    return redirect(user_home)


def update_product(req,id):
    item=product.objects.get(pk=id)
    if req.method=='POST':
        item.pname=req.POST['name']
        item.price=req.POST['price']
        item.quantity=req.POST['quantity']
        try:
            item.image=re.FILES['image']
            import os
            os.remove
            item.save()
        except:
            item.save()
        return redirect(product_details)
    return render(req,'product-details.html',{'item':item})
    
def delete_item(req,id):
    item=product.objects.get(pk=id)
    item.delete()
    return redirect(product_details)


