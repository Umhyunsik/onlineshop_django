import csv
import datetime

from django.contrib import admin
from django.http import HttpResponse


def export_to_csv(modeladmin,request,queryset):
    opts=modeladmin.model._meta #필드의형태를 얻어올수있다.
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields=[field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many ]

    writer.writerow([field.verbose_name for field in fields])

    for obj in queryset:
        data_row=[]
        for field in fields:
            value=getattr(obj,field.name)
            if isinstance(value,datetime.datetime):
                value= value.strftime("%Y-%m-%d")
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description ='Export to CSV'


from .models import Order,OrderItem
class OrderItemInline(admin.TabularInline):
    model=OrderItem
    raw_id_fields = ['product']#검색버튼을가지고 편하게 관리

from django.urls import reverse
from django.utils.safestring import mark_safe
#안전한내용인지 파악하고 html display

def order_detail(obj):
    url =reverse('orders:admin_order_detail',args=[obj.id])
    html=mark_safe(f"<a href='{url}'>Detail</a>")
    return html
order_detail.short_description= "Detail"

def order_pdf(obj):
    url =reverse('orders:admin_order_pdf',args=[obj.id])
    html=mark_safe(f"<a href='{url}'>PDF</a>")

    return html
order_pdf.short_description = "PDF"
#admin page 해당 title 변

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','address','postal_code','city','paid',order_detail,order_pdf,'created','updated']
    list_filter = ['paid','created','updated']
    inlines=[OrderItemInline]
    #inline은 foriegn key로 등록되어있는애들을 한꺼번에 추가할수있음
    actions=[export_to_csv]
admin.site.register(Order,OrderAdmin)