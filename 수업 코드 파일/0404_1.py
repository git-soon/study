# # 부모클래스가 생성자가 없을때
# class Animal:
#     def speak(self):
#         print("동물이 소리를 냅니다.")

#     def move(self):
#         print("동물이 움직입니다.")

# # 자식클래스
# class Cat(Animal):
#     def meow(self):
#         print("야옹!")

# cat = Cat()
# cat.speak()
# cat.move()
# cat.meow()

#부모클래스에 생성자가 존재할때
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name}이/가 소리를 냅니다.")

#     def move(self):
#         print(f"{self.name}이/가 움직입니다.")

# #자식클래스
# class Cat(Animal):
#     def __init__(self, name, sound = "야옹"):
#         super().__init__(name)
#         self.sound = sound

#     def moew(self):
#         print(f"{self.name}이/가 {self.sound}로 짖습니다.")

# cat = Cat("장화", "야아아아옹!")
# cat.speak()
# cat.move()
# cat.moew()


# 다중상속
# class Engine:
#     def __init__(self, horsepower, count):
#         self.horsepower = horsepower
#         self.count = count

# class Wheels:
#     def __init__(self, wheel_count):
#         self.wheel_count = wheel_count

# class Car(Engine, Wheels):
#     def __init__(self, horsepower, count, wheel_count):
#         Engine.__init__(self, horsepower, count)
#         Wheels.__init__(self, wheel_count)

#     def info(self):
#         print(f"이 자동차는 {self.horsepower} 마력과 {self.count}엔진과 {self.wheel_count}개의 바퀴를 가지고 있습니다.")

#     # def test(self):
#     #     print(f"어디????? {self.count}")

# car = Car(200, 2, 4)
# car.info()
# #car.test()
# #print(Car.mro())


# 오버라이딩
# class Parent:
#     def greet(self):
#         print("안녕하세요. 부모 클래스입니다.")

# class Child(Parent):
#     def greet(self):
#         super().greet() # 부모클래스의 메서드를 호출출
#         print("안녕하세요. 자식 클래스입니다.")

# # parent = Parent()
# # parent.greet()
# child = Child()
# child.greet()

# 실습. 상속과 오버라이딩
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # 재고 업데이트 메서드
    def update_quantity(self, amount):
        self.quantity += amount
        print(f"{self.name} 재고가 {amount}만큼 {'증가' if amount > 0 else '감소'}했습니다. 현재 재고: {self.quantity}")

    # 상품 정보 출력 메서드
    def display_info(self):
        print(f"상품명: {self.name}")
        print(f"가격: {self.price}원")
        print(f"재고: {self.quantity}개")

# 자식 클래스
class Electronic(Product):
    def __init__(self, name, price, quantity, warranty_period = 12):
        super().__init__(name, price, quantity)
        self.warranty_period = warranty_period

    # 보증기간 연장
    def extend_warranty(self, months):
        self.warranty_period += months
        print(f"보증기간이 {months}개월 연장되었습니다. 현재 보증기간 : {self.warranty_period}개월")

    # 오버라이딩
    def display_info(self):
        super().display_info()
        print(f"보증기간: {self.warranty_period}개월")

class Food(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date #유통기한 YYYY-MM-DD

    #유통기한 확인
    def is_expired(self, current_date):
        if current_date > self.expiration_date:
            print(f"{self.name}은/는 유통기한이 지났습니다.")
        else:
            print(f"{self.name}은/는 유통기한이 남았습니다.")

    def display_info(self):
        super().display_info()
        print(f"유통기한 : {self.expiration_date}")


# tv = Electronic("삼성스마트TV", 1500000, 2, 24)
# tv.display_info()
# tv.extend_warranty(12)
# tv.display_info()

milk = Food("서울우유", 3000, 30, "2025-04-20")
milk.is_expired("2025-04-21")
milk.display_info()

