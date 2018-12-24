import hashlib
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import UserInfo
from df_goods.models import GoodsInfo
from . import user_decorator

def register(request):
    return render(request,'df_user/register.html',{'title':'用户注册'})

def register_exist(request):
    name = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=name).count()
    return JsonResponse({'count': count})

def register_handler(request):
    #获取注册信息
    post = request.POST
    uname = post.get('user_name')
    pwd = post.get('pwd')
    cpwd = post.get('cpwd')
    uemail = post.get('email')
    #密码判断
    if not cpwd == pwd:
        return redirect('user:register')
    m = hashlib.md5()
    m.update(pwd.encode())
    upwd = m.hexdigest()
    #新建用户
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd
    user.uemail = uemail
    user.save()
    return redirect('user:login')

def login(request):
    uname = request.COOKIES.get('uname','')
    context = {'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
    return render(request,'df_user/login.html',context)

def login_handler(request):
    #接受请求信息
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    remember = post.get('remember',0)
    #根据用户名查询对象
    user = UserInfo.objects.filter(uname=uname)
    if len(user)==1:
        s1 = hashlib.md5()
        s1.update(upwd.encode())
        if s1.hexdigest() == user[0].upwd:
            url = request.COOKIES.get('url','/')
            red = redirect(url)
            #用户名是否记住
            if remember != 0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            request.session['user_id'] = user[0].id
            request.session['user_name'] = user[0].uname
            return red
        else:
            context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1, 'uname': uname, 'upwd': upwd}
            return render(request, 'df_user/login.html', context)
    else:
        context = {'title':'用户登录','error_name':1,'error_pwd':0,'uname':uname,'upwd':upwd}
        return render(request,'df_user/login.html',context)

def logout(request):
    request.session.flush()
    return redirect('/goods/')

@user_decorator.login
def info(request):
    user_email = UserInfo.objects.get(pk=request.session['user_id']).uemail
    goods_ids = request.COOKIES.get('goods_ids','')
    goods_list = []
    if goods_ids != '':
        goods_ids1 = goods_ids.split(',')
        for goods_id in goods_ids1:
            good = GoodsInfo.objects.get(id=int(goods_id))
            goods_list.append(good)
    else:
        pass
    context = {'title':'用户中心','user_email':user_email,'user_name':request.session['user_name'],
               'goods_list':goods_list,
               }
    return render(request,'df_user/user_center_info.html',context)

@user_decorator.login
def order(request):
    context = {'title':'用户中心'}
    return render(request,'df_user/user_center_order.html',context)

@user_decorator.login
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        #user.uresvaddress = post.get('uresvaddress')
        user.uname = post.get('uname')
        user.uaddress = post.get('uaddress')
        user.uems = post.get('uems')
        user.uphone = post.get('uphone')
        user.save()
    context = {'title':'用户中心','user':user}
    return render(request,'df_user/user_center_site.html',context)