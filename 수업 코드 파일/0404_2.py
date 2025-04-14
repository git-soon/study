# #추상클래스
# from abc import ABC, abstractmethod

# class PaymentSystem(ABC):

#     #추상메서드
#     @abstractmethod
#     def authenticate(self):
#         pass

#     @abstractmethod
#     def process_payment(self, amount):
#         pass

#     def payment_info(self, amount):
#         print(f"{amount}원 결제가 완료되었습니다.")


# class KakaoPay(PaymentSystem):
#     def authenticate(self):
#        print("카카오페이 인증되었습니다")

#     def process_payment(self, amount):
#         print(f"카카오페이로 {amount}원 결제합니다.")

# pay = 50000
# kakao = KakaoPay()
# kakao.authenticate()
# kakao.process_payment(pay)
# kakao.payment_info(pay)


# 클래스 메서드
# class Converter:
#     conversion_rate = 1.60934

#     @classmethod
#     def miles_to_kilometer(cls, mile):
#         return mile * cls.conversion_rate
    
# print(Converter.miles_to_kilometer(10))

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_birth_year(cls, name, birth_year):
#         age = 2025 - birth_year
#         return cls(name, age)
    
# p1 = Person.from_birth_year("홍길동", 2000)
# print(p1.name, p1.age)

# # 클래스변수를 사용
# class Counter:
#     count = 0

#     @classmethod
#     def increment(cls):
#         cls.count += 1

#     @classmethod
#     def get_count(cls):
#         return cls.count
    
# print(Counter.get_count())
# Counter.increment()
# print(Counter.get_count())


# 정적메서드
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def minus(a, b):
        return a - b
    
print(MathUtils.add(20, 40))    
print(MathUtils.minus(30, 10))