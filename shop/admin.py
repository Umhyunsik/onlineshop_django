from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug']
    #장바구니 추가할때 자바스크립트가 동작함
    prepopulated_fields = {'slug':('name',)}
#첫번째방법
admin.site.register(Category,CategoryAdmin)

#두번째방법 어노테이션 기법
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug','category','price','stock','available_display','available_order','created','updated']
    list_filter = ['available_display','created','updated','category']
    #미리 이름 만들어주기 prepopulated
    prepopulated_fields = {'slug':('name',)}
    list_editable = ['price','stock','available_display','available_order']