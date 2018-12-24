from django.shortcuts import redirect

def login(func):
    def login_func(request,*args,**kwargs):
        if request.session.has_key('user_id'):
            return func(request,*args,**kwargs)
        else:
            red = redirect('/user/login/')
            red.set_cookie('url',request.get_full_path())
            return red
    return login_func