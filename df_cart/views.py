from django.shortcuts import render,redirect,reverse
from django.http import JsonResponse
from df_user import user_decorator
from df_user.models import UserInfo
from df_goods.models import GoodsInfo
from .models import CartInfo

@user_decorator.login
def cart(request):
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid)
    context = {
        'title':'购物车',
        'page_name':1,
        'carts':carts,
    }
    return render(request,'df_cart/cart.html',context)

@user_decorator.login
def add(request,id,count,pindex):
    user = UserInfo.objects.get(pk=request.session['user_id'])
    goods = GoodsInfo.objects.get(pk=int(id))
    try:
        cart = CartInfo.objects.get(user=user, goods=goods)
        cart.count += count
        cart.save()
    except:
        CartInfo.objects.create(user=user, goods=goods, count=count)
    return redirect(reverse('goods:list',args=(goods.gtype_id,pindex,1)))

@user_decorator.login
def addcount(request,id):
    user = UserInfo.objects.get(pk=request.session['user_id'])
    goods = GoodsInfo.objects.get(pk=int(id))
    try:
        cart = CartInfo.objects.get(user=user,goods=goods)
        cart.count += 1
        cart.save()
    except:
        pass
    return JsonResponse({'count':cart.count})

@user_decorator.login
def descount(request,id):
    user = UserInfo.objects.get(pk=request.session['user_id'])
    goods = GoodsInfo.objects.get(pk=int(id))
    try:
        cart = CartInfo.objects.get(user=user, goods=goods)
        cart.count -= 1
        cart.save()
    except:
        pass
    return JsonResponse({'count':cart.count})

@user_decorator.login
def edit(request):
    user = UserInfo.objects.get(pk=request.session['user_id'])
    if request.method == 'GET':
        gid = request.GET.get('good_id')
        count = request.GET.get('count')
        good = GoodsInfo.objects.get(pk=int(gid))
    context = {'title': '付款', 'user': user, 'good':good,'count':count}
    return render(request, 'df_cart/place_order.html', context)

@user_decorator.login
def delete(request,id):
    cart = CartInfo.objects.get(goods=GoodsInfo.objects.get(pk=int(id)))
    cart.delete()
    return redirect(reverse('cart:cart'))

@user_decorator.login
def place_order(request):
    list = []
    user = UserInfo.objects.get(pk=request.session['user_id'])
    if request.method == 'GET':
        ids = request.GET.getlist('cart_id')
        for gid in ids:
            cart = CartInfo.objects.get(user=user, goods_id=int(gid))
            list.append(cart)

    context = {'title':'付款','user':user,'carts':list}
    return render(request,'df_cart/place_order.html',context)
