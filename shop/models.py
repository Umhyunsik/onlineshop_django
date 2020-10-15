from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    # name으로 검색될수 있으니 indexing해주기
    name=models.CharField(max_length=200,db_index=True)
    #meta_description 검색엔진에 노출될것들
    meta_description=models.TextField(blank=True)
    #slug 카테고리에대한 번호 <pk> 한글쓰려면 allow_unicode써야
    slug=models.SlugField(max_length=200,db_index=True,unique=True,allow_unicode=True)
    class Meta:
        ordering=['name']
        verbose_name='category'
        verbose_name_plural='categories' #복수형

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # 상세페이지 결정
        return reverse('shop:product_in_category',args=[self.slug])

    pass
class Product(models.Model):
    # 카테고리가 지워져도 제품은 지워지면안되니까 -> category set_null
    #related_name은 카테고리입장에서 어떻게 불러올건지에 대
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name='products')
    name=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,db_index=True,unique=True,allow_unicode=True)
    image=models.ImageField(upload_to='products/%Y%m%d',blank=True)
    description=models.TextField(blank=True)
    meta_description=models.TextField(blank=True)

    #총 여덟자리까지 지정
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    available_display=models.BooleanField('Display',default=True)
    available_order=models.BooleanField('Order',default=True)

    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created','-updated']
        index_together=[['id','slug']]
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_detail',args=[self.id,self.slug])