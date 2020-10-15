#장고에서 form을 쓰는이유 사용자들이 브라우저에서 어떤정보를 서버로보낼떄 더 정제된 모습으로 보내도록
from .models import Order
from django import forms
#특정 모델에관한 내용을 폼으로 만들고싶을때 모델폼

#모델은없으나 이메일보내기 일반폼사용

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['first_name','last_name','email','address','postal_code','city']


