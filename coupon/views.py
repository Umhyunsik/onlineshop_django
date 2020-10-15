from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone #사용기간에 대한 평가 timezone 사용자들의 국가 시간에 맞게 계산 할수있음
from django.views.decorators.http import require_POST

# Create your views here.

from .models import Coupon
from .forms import AddCouponForm

@require_POST
def add_coupon(request):
    now = timezone.now()
    form = AddCouponForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:

            coupon =Coupon.objects.get(code__iexact=code,use_from__lte=now,use_to__gte=now,active=True)#대소문자 가리지않고 구분안함
            #now가 쿠폰 시작from to 안에있어야한다.
            request.session['coupon_id']=coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon_id']=None

    return redirect('cart:detail')

