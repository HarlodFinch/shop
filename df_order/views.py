from django.shortcuts import render

def order_info(request):
    context = {
        'title':'订单',
    }
    return render(request,'df_user/user_center_order.html',context)
