# #부모클래스가 생성자가 없을때
# class animal:
#     def speak(self):
#         print('동물이 소리를 냅니다')

#     def move(self):
#         print('동물이 움직입니다')
        
# # 자식 클래스
# # 자식 클래스는 부모 클래스의 속성과 메서드를 상속받는다.
# class dog(animal):
#     def __init__(self, name):
#         self.name = name
        
#     def speak(self):
#         print(f'{self.name}가 멍멍합니다')

#     def move(self):
#         print(f'{self.name}가 뛰어다닙니다')






# # 부모클래스에 생성자가 존재할때
# class Animal:
#     def __init__(self, name):
#         self.name = name
        
#     def speak(self):
#         print(f'{self.name}가 소리를 냅니다')

#     def move(self):
#         print(f'{self.name}가 움직입니다')


# # 자식 클래스
# class Cat(Animal):
#     def __init__(self, name, sound):
#         super().__init__(name) # 부모 클래스의 생성자를 호출한다.
#         self.sound = sound
        
#     def speak(self):
#         print(f'{self.name}이/가 {self.sound}로 짖습니다.')


# cat = Cat("장화","야아아아옹")
# cat.move()
# cat.speak()
# cat.move()


# # 다중상속
# class Engine:
#     def start(self, horsepower, count):
#         self.horsepower = horsepower
#         self.count = count

# class Wheels:
#     def __init__(self, Wheel_count):
#         self.Wheel_count = Wheel_count

# class Car(Engine, Wheels):                          # Car 클래스는 Engine과 Wheels 클래스를 상속받는다.
#     def __init__(self, horsepower, count, wheel_count):
#         Engine.__init__(self, horsepower, count)   # Engine 클래스의 생성자를 호출한다.
#         Wheels.__init__(self, wheel_count)         # Wheels 클래스의 생성자를 호출한다.

#     def info(self):
#         print(f'이 자동차는 {self.horsepower}마력과, {self.count}개의 엔진, 그리고 {self.wheel_count}개의 바퀴를 가지고 있습니다.')

#     def test(self): 
#         print(f'어디??? {self.count}') 

# car = Car(200, 2, 4)
# car.info()

# print(Car.mro())    # 클래스의 상속 관계를 확인할 수 있다.
#                     # mro() 메서드는 메서드 해석 순서를 반환한다.

# # 다중상속의 경우, 메서드 해석 순서는 왼쪽에서 오른쪽으로 진행된다.
# # 따라서, Engine 클래스의 start() 메서드가 먼저 호출된다.
# # 그 다음으로 Wheels 클래스의 __init__() 메서드가 호출된다.
# # 마지막으로 Car 클래스의 info() 메서드가 호출된다.
# # 이 순서는 클래스의 상속 관계에 따라 결정된다.   
# # super().__init__() 메서드는 단일 상속시에만 사용할 수 있다.
# # 다중 상속시에는 super() 메서드를 사용하지 않고, 부모 클래스의 생성자를 직접 호출해야 한다.
# # 다중 상속시에는 메서드 해석 순서를 확인하여, 어떤 클래스의 메서드가 먼저 호출되는지 확인해야 한다.


# #오버 라이딩
# # 오버라이딩은 부모 클래스의 메서드를 자식 클래스에서 재정의하는 것이다.
# # 오버라이딩을 사용하면 부모 클래스의 메서드를 자식 클래스에서 재정의하여 사용할 수 있다.
# class Parent:
#     def greet(self):
#        print("안녕하세요, 부모 클래스입니다.")

# class Child(Parent):
#     def greet(self):
#         super().greet()  # 부모 클래스의 greet() 메서드를 호출한다.
#         print("안녕하세요, 자식 클래스입니다.")

# parent = Parent()
# child = Child()
# parent.greet()  # 부모 클래스의 greet() 메서드 호출
# child.greet()   # 자식 클래스의 greet() 메서드 호출

# # 부모 클래스의 greet() 메서드가 먼저 호출되고, 그 다음에 자식 클래스의 greet() 메서드가 호출된다.
# # 따라서, 부모 클래스의 greet() 메서드에서 "안녕하세요, 부모 클래스입니다."가 출력되고,  # # 자식 클래스의 greet() 메서드에서 "안녕하세요, 자식 클래스입니다."가 출력된다.
# # 오버라이딩을 사용하면 부모 클래스의 메서드를 자식 클래스에서 재정의하여 사용할 수 있다.
 
# 실습. 상속과 오버라이딩

# #부모 클래스
# class Product:
#     def __init__(self, name, price, quantitiy):
#         self.name = name
#         self.price = price
#         self.quantitiy = quantitiy
        
#     # 재고 업데이트 메서드    
#     def undate_quantitiy(self, amount):
#         self.quantitiy += amount
#         print(f'{self.name}의 재고가 {amount}만큼 {"증가" if amount > 0 else "감소"}했습니다. 현재 재고: {self.quantitiy}개')

#     # 상품 정보 출력 메서드
#     def display_info(self):
#         print(f'상품명: {self.name} \n가격: {self.price}원 \n재고: {self.quantitiy}개')


# # 자식 클래스
# class Electronic(Product):
#     def __init__(self, name, price, quantitiy, warranty_period):
#         super().__init__(name, price, quantitiy)  # 부모 클래스의 생성자를 호출한다.
#         self.warranty_period = warranty_period 
#         warranty_period = 12 # 기본값 12개월 

#     # 보증기간 연장 메서드
#     def expend_warranty(self, expend_warranty): #month
#         self.warranty_period += expend_warranty
        
#         # if self.warranty_period == 0:
#         #     print(f'{self.name}의 보증기간이 없습니다.')
#         # else:
#         #     print(f'{self.name}의 보증기간은 {self.warranty_period}개월입니다.')
#         # return self.warranty_period

#     # 상품 정보 출력 메서드
#     def display_info(self):
#         super().display_info()  # 부모 클래스의 display_info() 메서드를 호출한다.
#         print(f'{"보증기간이 {expend_warranty}개월 연장되었습니다. 현재 보증 기간 : {self.expend_warranty}"  if self.expend_warranty > 0 else " "}')
#         print (f'상품명 : {self.name} \n가격 : {self.price}원 \n재고 : {self.quantitiy}개 \n보증기간 : {self.warranty_period}개월')


#     #Food 클래스 설계조건, 추가 변수 : expiration_date (유통기한 - 날짜 형태는 "YYYY-MM-DD")
#     # is_expired 메서드 : 유통기한이 지났는지 확인하고 결과 출력하는 메서드
# class Food(Product):
#     def __init__(self, name, price, quantitiy, expiration_date):
#             super().__init__(name, price, quantitiy)
#             self.expiration_date = expiration_date

#     def expiration(self, expiration_date, today):
#         self.expiration_date = expiration_date
#         self.today = today
#             # expiration_date = "2025-04-05" # 유통기한
#             # today = "2025-04-04"
#         if today > expiration_date:
#             print(f'{self.name}은 유통기한이 지났습니다.')
#         else:
#             print(f'{self.name}은 유통기한이 남아 있습니다.')


#     def display_info(self):
#         super().display_info()
#         print(f'상품명 : {self.name} \n가격 : {self.price}원 \n재고 : {self.quantitiy}개 ')

# tv = Electronic("LG TV", 1000000, 10, 12)
# tv.display_info()
# tv.expend_warranty(12)
# tv.display_info()


#추상 클래스
# # 추상 클래스는 인스턴스를 생성할 수 없는 클래스이다.
# # 추상 클래스는 자식 클래스에서 반드시 구현해야 하는 메서드를 정의할 수 있다.
# # 추상 클래스는 abc 모듈을 사용하여 정의할 수 있다.
# # 추상 클래스는 @abstractmethod 데코레이터를 사용하여 정의할 수 있다.

# from abc import ABC, abstractmethod

# class PaymentSystem(ABC):

#     # 추상 메서드 : 자식 클래스에서 반드시 구현해야 하는 메서드
#     # 추상 메서드는 @abstractmethod 데코레이터를 사용하여 정의할 수 있다.
#     @abstractmethod
#     def authenticate(self):
#         pass

#     @abstractmethod
#     def process_payment(self, amount):
#         pass

#     def payment_info(self,amount):
#         print(f"{amount}원 결제가 완료되었습니다.")

# class KaKaoPay(PaymentSystem): # 자식 클래스 : 여기서 추상 메서드를 구현해야 한다.
#     def authenticate(self): # 인증 메서드 : 위에 똑같이 만들면 된다.
#         print("카카오페이 인증 완료")

#     def process_payment(self, amount):
#         print(f"카카오페이로 {amount}원 결제")
#         self.payment_info(amount)


# pay = 5000




# #클래스 매서드
# class Converter: # 인스턴스를 만들지 않고 사용한다.
#     converton_rate = 1.60934 # 1 mile = 1.60934 km

#     @classmethod
#     def miles_to_km(cls, miles): #cls : 클래스 자기자신, self : 인스턴스 자기자신 ,
#         return miles * cls.converton_rate
    
# print(Converter.miles_to_km(10)) # 16.0934

# #생성자 메서드 없는거
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_birth_year(cls,name,birth_year):
#        age = 2025 - birth_year
#        return cls(name, age)

# p1 = Person.from_birth_year("홍길동", 2000)     




# #클래스변수를 사용
# Class Counter:
#     count = 0 # 클래스 변수

#     @classmethod
#     def increment(cls):
#         cls.count += 1

#     @classmethod
#     def get_count(cls):
#         return cls.count

# print(Counter.get_count()) # 0
# Counter.increment()
# print(Counter.get_count()) # 1


# #정적 매서드 : 인스턴스나 클래스에 의존하지 않고 독립적으로 동작하는 메서드
# class Mathutils:
#     @staticmethod # staticmethod 데코레이터 : 정적 메서드로 정의한다. 
#     def add(a, b):
#         return a + b
    
#     def sub(a, b):
#         return a - b
    
# print(Mathutils.add(10, 20)) # 30
# print(Mathutils.sub(10, 20)) # -10
    



#실습 2 클래스 종합 프로그래밍
#날짜별 전력 사용량
electricity = [
    {"date": "2024-11-01", "usage": 12.5},
    {"date": "2024-11-02", "usage": 15.3},
    {"date": "2024-11-03", "usage": 10.8},
    {"date": "2024-11-04", "usage": 14.2},
    {"date": "2024-11-05", "usage": 13.6}
    ]




#추상 클래스 생성
from abc import ABC, abstractmethod

class ElectricityData(ABC):
    @abstractmethod
    def usage_data(self):
        pass
    def total_usage(self):
        pass

    @classmethod
    def highest_usage(cls):
        pass
    
    @classmethod
    def usage_in_range(cls, start_date, end_date):
        pass

    def calculate_total_usage(self, date):
        pass
    def add_usage(self, date, usage):

#매서드 제작
#1. 추상 메서드
# calculate_total_usage() : # 전력 사용량데이터를 기반으로 총 사용량을 계산하는 메서드
# get_usage_on_data(date): # 특정 날짜의 전력 사용량을 반환

#일반 메서드
# add_usage(date, usage): # 새로운 전력 사용량 데이터를 추가하는 메서드
# remove_usage(date): # 특정 날짜의 전력 사용량 데이터를 삭제하는 메서드


#usage_data : 전력 사용량 데이터를 담은 리스트로, 각 항목은 날짜와 사용량을 포함한 딕셔너리 형태입니다.

    @property
    def total_usage(self): # 총 전력 사용량을 계산하는 메서드
        return sum(item["usage"] for item in self.data)
    
    @usage_data.setter
    def usage_data(self, data):
        self.data = data
        data = electricity[data,usage]






#구현 할거
#1. 데이터를 입력하여 총 전력 사용량을 계산하고 특정 날짜의 사용량을 조회할 수 있어야 한다.
#2. 데이터 추가 및 삭제가 가능해야 한다.
#3. 정적 메서드를 통해 가장 높은 전력 사용량과 해당 날자를 찾아라
#4. 클래스 매서드를 통해 특정 날짜 범위 내의 사용량을 출력하라