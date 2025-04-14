# 클래스

# 클래스의 정의
# class Car:
#     model = ""
#     cc = 0

#     # 함수추가(메서드)
#     def info(self):
#         print(f"모델명은 {self.model}, 배기량은 {self.cc}cc")

# car1 = Car() # 인스턴스 생성
# car1.model = "싼타페"
# car1.cc = 2000

# car2 = Car()
# car2.model = "타스만"
# car2.cc = 3500

# # print(f"모델명 {car1.model}이고 {car1.cc}cc 입니다.")
# # print(f"모델명 {car2.model}이고 {car2.cc}cc 입니다.")

# # 메서드 호출
# car1.info()
# car2.info()


# 생성자가 존재하는 클래스
# class Car:
#     #생성자
#     def __init__(self, model, cc):
#         self.model = model
#         self.cc = cc

#     def __str__(self):
#         return f"모델: {self.model}, 배기량: {self.cc}cc"

#     def info(self):
#         print(f"모델명은 {self.model}, 배기량은 {self.cc}cc")

# car1 = Car("싼타페", 2000)
# car2 = Car("타스만", 3500)
# # car1.info()
# # car2.info()
# print(car1)
# print(car2)

# #객체 리스트
# print("승용차 리스트")
# cars = [
#     Car("소나타", 2000),
#     Car("쏘렌토", 2200),
#     Car("아반테", 1600)
# ]
# for car in cars:
#     print(car)
"""

#실습1. 사직연산 클래스 만들기
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def mul(self):
        return self.num1 * self.num2
    def div(self):
        if self.num2 == 0:
            return "분모가 0이 될 수 없습니다"
        
        return self.num1 / self.num2
    
calc = Calculator(10, 7)
print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())



# 클래스 변수와 인스턴스 변수
class Dog:
    kind = "진돗개" # 클래스 변수

    def __init__(self, name):
        self.name = name # 인스턴스 변수

# 인스턴스변수 접근
dog1 = Dog("백구")
print(dog1.name)
# 클래스변수 접근
#print(dog1.kind) 
print(Dog.kind) #일반적으로 클래스변수에 접근하는 방법



class Example:
    shared = "공유변수" # 클래스변수

    def __init__(self, name):
        self.name = name # 인스턴스 변수

example1 = Example("A")
example2 = Example("B")

# 클래스변수 변경
Example.shared = "변경된변수"
print(example1.shared)
print(example2.shared)
# 인스턴스변수 변경
example1.name = "C"
print(example1.name)
print(example2.name)

"""

# 사번 자동 발급
class Employee:
    serial_num = 1000 

    # def __init__(self, name):
    #     Employee.serial_num += 1 #클래스변수 1씩증가
    #     self.id = Employee.serial_num #사번
    #     self.name = name

    # 인스턴스변수
    def __init__ (self, name):
        self.serial_num = 1000
        self.serial_num += 1
        self.id = self.serial_num
        self.name = name

    def __str__(self):
        return f"사번 : {self.id}, 이름 : {self.name}"

e1 = Employee("홍길동")
print(e1)
e2 = Employee("임꺽정")
print(e2)
employees = [
    Employee("이몽룡"),
    Employee("성춘향"),
    Employee("변사또"),
    Employee("전우치")
]
for e in employees:
    print(e)