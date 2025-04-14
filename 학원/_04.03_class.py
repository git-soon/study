# #클래스

# #클래스의 정의
# class Car: # 클래스 이름은 대문자로 시작한다.
    
#     #클래스 변수
#     model ="" # #클래스 변수는 모든 인스턴스가 공유하는 변수이다.
#     cc = 0  

#     #함수 추가(메서드)    # 메서드는 클래스 안에 정의된 함수를 의미한다. 
#     def info(self):     # self는 인스턴스 자신을 의미한다.
#         print(f'모델명은 {self.model},배기량은 {self.cc}cc입니다.')


# car1 = Car()             #인스턴스 생성
# car1.model = "싼타페"     #인스턴스 변수
# car1.cc = 2000


# car2 = Car()
# car2.model = "타스만" 
# car2.cc = 3500 


# print(f'모델명 {car1.model}이고 {car1.cc}cc 입니다.')

# print(f'모델명 {car2.model}이고 {car2.cc}cc 입니다.')

# #매서드 호출
# car1.info()
# car2.info()



# #생성자가 존재하는 클래스 
# class Car: 
#     #생성자 : 생성자는 클래스가 인스턴스화 될 때 자동으로 호출되는 메서드이다.
#     # 생성자는 __init__() 메서드로 정의된다.
#     # 생성자는 인스턴스 변수를 초기화하는 역할을 한다. 
    
#     def __init__(self, model, cc): # 임마는 리턴값이 없다, 이 생성자는 초기화라고 생각하면된다
#         self.model = model
#         self.cc = cc

#     def __str__(self):                                # __str__() 메서드는 인스턴스를 문자열로 표현할 때 호출된다. 
#         return f"모델: {self.model}, 배기량: {self.cc}" # return은 문자열을 반환한다.

#     def info(self):                          # info() 메서드는 인스턴스의 정보를 출력하는 역할을 한다.
#         print(f'모델명은 {self.model},배기량은 {self.cc}cc입니다.')


# car1 = Car("산타페",2000)
# car2 = Car("타스만",3500)
# car1.info()     # car1 인스턴스의 info() 메서드 호출
# car2.info()



# #객체 리스트
# print("===승용차 리스트===")
# cars = {                # set()은 중복을 허용하지 않는 집합 자료형이다. 
#     Car("소나타", 2000),
#     Car("쏘렌토", 2200),
#     Car("아반떼", 1600)
# }

# for car in cars:    # for문을 사용하여 cars 집합의 각 요소를 car 변수에 대입한다.
#     print(car)


#실습1. 사칙연산 클래스 만들기

#내가 했는데 안된거

class Math:     

    def __init__(self, num1, num2):     # 생성자
        self.num1 = num1 # 인스턴스 변수 
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2    # 더하기

    def sub(self):
        return abs(self.num1-self.num2)
    
    def mul(self):
        return self.num1 * self.num2    # 곱하기
    
    def div(self):
        if self.num2 == 0:          # 0으로 나누는 경우
            return "0으로 나눌 수 없습니다."    
        else:
            return self.num1//self.num2     # 정수 나누기
    
    def __into__(self):     # 인스턴스 변수를 출력하는 메서드
        return f"num1 : {self.num1}, num2 : {self.num2}"       ## 인스턴스 변수 출력

temp1 = Math(100,200)
temp2 = Math(9,10)

print(temp1.__into__())
print(temp1.add())
print(temp1.sub())
print(temp1.mul())
print(temp1.div())


# #강의
class Calculation:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    
    def sub(self):
        return abs(self.num1 - self.num2)
    
    def mul(self):
        return self.num1*self.num2
    
    def div(self):
        if self.num2 == 0:
            return "분모가 0이 될수 없습니다."
        
        return f'{int(self.num1/self.num2*100)/100:.2f}'

        
calc = Calculation(10,7)
print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())



# #클래스 변수와 인스턴스 변수
# class Dog:
#     kind = "진돗개" #클래스 변수

#     def __init__(self,name):
#         self.name = name #인스턴스 변수

# #인스턴스변수 접근
# dog1 = Dog("백구")
# print(dog1.name)

# #클래스 변수 접근
# print(dog1.kind)
# print(Dog.kind) #일반적으로 클래스변수에 접근하는 방법

# class Example:
#     shared = "공유변수" #클래스변수

#     def __init__(self,name):
#         self.name = name #인스턴스 변수

# example1 = Example("A")
# example2 = Example("B")

# # 클래스 변수 변경
# Example.shared = "변경된 변수"
# print(example1.name)
# print(example2.name)


# #사번 자동 발급
# class Employee:
#     serial_num = 1000 #기본값 (클래스 변수)

#     def __init__(self,name):
#         Employee.serial_num +=1 #z클래스변수 1씩증가
#         self.id = Employee.serial_num #사번
#         self.name = name

#     def __str__(self):
#         return f"사번 : {self.id}, 이름 : {self.name}"
    
# e1 = Employee ("홍길동")
# print(e1)
# e2 = Employee ("임꺽정")
# print(e2)



# class Supermarket:
#     # 클래스끼리 손님 숫자 공유 = 클래스 변수 필요
#     total_coustomer

#     def __init__(self, location, name, product, customer): # 위치, 이름, 상품, 고객 수
#         self.location = location 
#         self.name = name
#         self.product = product
#         self.customer = customer
#         customer = 0
#         # 추가로 지점 여러개의 손님 숫자 공유?
        
#     def print_location(self):
#         return (f"위치: {self.location}")
    
#     def change_category(self, new_product):
#         self.product = new_product
    
#     def show_list(self):
#         pirnt( f"상품: {self.product}")

#     def enter_customer(self):
#         customer += 1
#         Supermarket.enter_customer += 1

#     def print_info(self):
#         return print(f"위치: {self.location}\n상품: {self.product}\n위치: {self.location}, 이름: {self.name}, 고객 수: {self.customer}명")
    

# s1 = Supermarket("마포구 염리동", "마켓온", "음료", 12)
# s1.print_info()
# s1.enter_customer()
# s1.enter_customer()
# s1.enter_customer()
# supermarket1.change_category("과자")
# supermarket1.show_list()
# supermarket1.print_info()
# # 추가로 지점 여러개의 손님 숫자 공유?




# #정보 은닉
# class person:
#     def __init__(self):
#         self.name = ""
#         self.age = 0

#     #이르믕ㄹ 설정
#     def setname(self,name):
#         self._name = name

#     #이름을 출력
#     def getname(self):
#         return self._name
    
#     #나이를 설정
#     def setage(self,age):
#         self._age = age

#     #나이를 출력
#     def getage(self):
#         return self._age
    





    #getter,setter
class person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age


    #getter, 데코레이터는 무조건 바로밑에 작성해야한다, 한칸 띄기 안됨

    # @property    #이런거 안됨

    # def name(self,name):
    #     return self.__name


    @property #getter
    def name(self):
        return self.__name
    
    #setter
    @name.setter
    def name(self,name):
        return self.__name = name

    @property
    def age(self,age):
        return self.__age
    
    #setter
    @name.setter
    def age(self,age):
        return self.__age = age


# #실습 3 건강상태 클래스 만들기
# # class health:

# #     hp = range(1,101)

# #     def __init__(self,name,drunk,work):
# #         self.__name = name
# #         self.__drunk = drunk
# #         self.__work = work

# #     def get_drunk(self):  #술을 마시면 체력이 1 감소하는 매서드
# #         return hp -= i

# #     def get_work(self):
# #         return hp += 


# class HpStat:

#     def __init__(self, name, drunk, work):
#         self.__name = name
#         self.__drunk = drunk
#         self.__work = work
#         self.__hp = 50

#     @property
#     def name(self):
#         return self.__name
    
#     @property
#     def drunk(self):
#         return self.__drunk
    
#     @property
#     def work(self):
#         return self.__work

#     def get_drunk(self):
#         self.__hp -= self.__drunk
#         if self.__hp < 1:
#             self.__hp = 1
#         return self.__hp
    
#     def get_work(self):
#         self.__hp += self.__work
#         if self.__hp > 100:
#             self.__hp = 100
#         return self.__hp
    
#     def __str__(self):
#         return f"{self.__work}시간 운동하다. \n 술을 {self.__drunk}마시다. \n {self.name} - hp : {self.__hp}"
    
