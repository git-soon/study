"""
#실습2. 슈퍼마켓 클래스
class Supermarket:
    total_customer = 0

    def __init__(self, location, name, product, customer):
        self.location = location
        self.name = name
        self.product = product
        self.customer = customer
        Supermarket.total_customer += customer

    def print_location(self):
        print(f"위치 : {self.location}")

    def change_category(self, new_product):
        self.product = new_product

    def show_list(self):
        print(f"상품 : {self.product}")
    
    def enter_customer(self):
        self.customer += 1
        Supermarket.total_customer += 1

    def show_info(self):
        print(f"위치: {self.location}, 이름: {self.name}, 상품: {self.product}, 고객수: {self.customer}, 총 고객수: {Supermarket.total_customer}")

s1 = Supermarket("은평구 응암동", "GS25", "과자", 10)
s1.show_info()
s2 = Supermarket("은평구 갈현동", "GS25", "과자", 5)
s2.show_info()

s1.enter_customer()
s1.enter_customer()
s1.print_location()
s1.change_category("음료")
s1.show_list()
s1.show_info()



# 정보은닉
class Person:
    def __init__(self):
        self._name = ""
        self._age = 0

    #이름을 설정
    def setname(self, name):
        self._name = name

    #이름을 출력
    def getname(self):
        return self._name
    
    #나이를설정
    def setage(self, age):
        self._age = age
    
    #나이를 출력
    def getage(self):
        return self._age
    
p1 = Person()
p1.setname("홍길동")
print(p1.getname())
p1.setage(20)
print(p1.getage())


# getter, setter
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    #getter
    @property
    def name(self):
        return self.__name
    
    #setter
    @name.setter
    def name(self, name):
        self.__name = name

    #getter
    @property
    def age(self):
        return self.__age
    
    #setter
    @age.setter
    def age(self, age):
        self.__age = age

p1 = Person("홍길동", 20)
print(p1.name)
print(p1.age)
p1.name = "이몽룡"
p1.age= 23
print(p1.name, p1.age)
"""


# 실습3. 건강상태 클래스 만들기
class Health:
    def __init__(self, name):
        self._hp = 100
        self._name = name

    # def getname(self):
    #     return self._name
    # def setname(self, name):
    #     self._name = name
    # def info(self):
    #     print(f"{self.getname()}")

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, hp):
        if hp >= 100:
            self._hp = 100
        elif hp < 0:
            self._hp = 0
        else:
            self._hp = hp

    def exersise(self, hour):
        self.hp += hour
        print(f"{hour}시간 운동을 하였습니다")
    
    def drink(self, cups):
        self.hp -= cups
        print(f"{cups}잔 술을 마셨습니다")


    def info(self):
        print(f"{self.name}의 hp는 {self.hp}")

p1 = Health("나몸짱")
p1.exersise(3)
p1.drink(10)
p1.info()

p2 = Health("나약해")
p2.hp = 30
p2.exersise(3)
p2.drink(15)
p2.info()