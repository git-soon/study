# 사칙 연산 클래스 만들기
class Math:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return abs(self.num1 - self.num2)

    def mul(self):
        if self.num2 == 0:
            return "0으로 나눌수 없습니다."
        else:
            return self.num1 * self.num2

    def div(self):
        return (f'{self.num1//self.num2:.2f}')


cal = Math(100, 200)
print(cal.add())
print(cal.sub())
print(cal.mul())
print(cal.div())


class Product:
    def __init__(self, name, price, quantity):

        self.name = name
        self.price = price
        self.quantitiy = quantity

    # 재고 업데이트 메서드
    def update_quantity(self, month):
        self.month = month
        print(
            f"{self.name}재고가 {amount}만큼 {'증가'if amount > 0 else '감소'}했습니다. 현재 재고 {self.quantitiy}")

    # 상품 정보 출력 메서드
    def display_info(self):
        print(f'상품명 : {self.name}')
        print(f'가격 : {self.price}원')
        print(f'재고 : {self.quantitiy}개')

# Electronic 클래스 설계 조건
# 추가 변수 : warranty_period(보증기간, 기본값 12 개월)
# 새로운 메서드 : extend__warranty(month)를 작성하여 보증 기간을 연장
# 오버 라이딩 : display_info 메서드를 오버라이딩하여 보증 기간 정보를 포함한 상품 정보를 출력

# Electronic 클래스


class Electronic(Product):
    def __init__(self, warranty_period=12):  # 보증 기간 기본값 12 개월을 period = 12로 표현
        super().__init__()
        self.warranty_period = warranty_period

    # 보증기간 연장 ㄱㄱ
    def extend__warranty(self, month):
        self.warranty_period += month

    def display_info(self):
        super().display_info()  # 아니 이게 그대로 가져온거고 밑에 추가적으로 뭘 쓰면 그게 오버라이딩 아님?
        print(f'보증기간 : {self.warranty_period}개월')

# food 클래스 설계조건
# 추가 변수 : expiration_date(유통기한 - 날짜형태는 "YYYY-MM-DD")
# 새로운 매서드 : is_expired(current_date)를 작성하여 유통기한이 지났는지 여부를 확인하고 결과를 출력
# 오버 라이딩 : display_info 메서드를 오버라이딩하여 유통기한 정보를 포함한 상품 정보를 출력


class Food(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date

    # 유통기한 확인
    def is_expierd(self, current_date):
        if current_date > self.expiration_date:
            print(f"{self.name}은/는 유통기한이 지났습니다.")
        else:
            print(f"{self.name}은/는 유통기한이 남았습니다.")

    def display_info(self):
        return super().display_info()
