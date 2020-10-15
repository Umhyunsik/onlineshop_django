
from django.shortcuts import render,get_object_or_404
from .models import *
from cart.forms import AddProductForm

#함수형 뷰 첫번째 무조건 request
def product_in_category(request,category_slug=None):
    current_category=None
    #objects라는 매니저 에게 전체카테고리 불러오기
    categoreis=Category.objects.all()
    #가능한것들만 불러오기
    products=Product.objects.filter(available_display=True)
    if category_slug:
        # 카테고리에서 카테고리 슬러그에 있는걸 가져올거야 없으면 404페이지 띄우
        current_category=get_object_or_404(Category,slug=category_slug)
        products=products.filter(category=current_category)
        # 지연평가 함 filter를 먹여도 여러번 사용되는게 아님

    return render(request,'shop/list.html',{'current_category':current_category,
                                            'categories':categoreis,
                                            'products':products})


def product_detail(request,id,product_slug=None):
    product=get_object_or_404(Product,id=id,slug=product_slug)
    add_to_cart=AddProductForm(initial={'quantity':1})
    return render(request,'shop/detail.html',{'product':product,
                                              'add_to_cart':add_to_cart})


# Create your views here.
