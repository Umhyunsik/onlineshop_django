# onlineshop_django
## iamport 결제시스템 온라인쇼핑몰 

### 사용기술

+ aws s3 , rds 
+ django
+ iamport


### app

+ cart (장바구니)
+ coupon (할인쿠폰)
+ shop (물건 등록,보여주기)
+ order (물건 주문하기)


### aws s3 
+ config/s3media.py
media파일 전용 upload (물건사진)
'onlineshop-media-hyunsik'

### aws s3 
+ 'onlineshop-static-hyunsik' css,js 파일 전용 upload


### 1) cart
+ 물건 담기

login 전에 장바구니 담았던 제품들을 로그인 후에도 유지되어야하니 session을 request 받아 cart_id 를 받아옴 .
모든페이지에 카트 정보 담는것 context_processors.py 추가, settings.py 변경


### 2) coupon
+ 장바구니내 물건 할인 

쿠폰이 존재한다면 session에 값 넣어줌 

### 3) shop

+ 전체보기 , 카테고리 내 물품 보기 


### 4) order 

+ iamport를 이용해서 결제시스템 받아오기 , 결제 진행후 db에 저장 


![스크린샷 2020-10-16 오전 12 13 18](https://user-images.githubusercontent.com/22265915/96160768-5c493000-0f51-11eb-8380-ae14c407c05a.png)







