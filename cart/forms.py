from django import forms

class AddProductForm(forms.Form):
    quantity=forms.IntegerField()
    is_update = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)# 어떻게 노출할지 정하는게 wdiget
    #false로 안하면 값 없다고 판단되는 경우
