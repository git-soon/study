# # 함수 시작

# # 함수 실습 1
# # 두수를 매개변수로 전달하여 서로 같으면 곱하고, 서로 다르면 더하는 함수를 정의하고 호출하는 프로그램을 작성하세요.
# def cal(num1, num2):
#     if num1 == num2:
#         return num1 * num2

#     else:
#         return num1 + num2


# print(cal(2, 2))
# print(cal(2, 5))

# # 함수 실습 2
# # 주문 상품 가격이 20,000원 미만이면 배송비 (2,500)포함하고, 아니면 배송비를 포함하지 않는 프로그램을 작성하세요


# def deliver(price):
#     deliver_fee = 2500
#     if price < 20000:
#         return price + deliver_fee

#     elif price > 20000:
#         return price

#     else:
#         print("잘못된 정보입니다. 다시 입력해주세요")

# def d_kwargs(**kwargs):
#     return print(kwargs)


# d_kwargs(a=1, b=2, c=3, d=4, e=5, f=6, g=7)


# def multi(a, b):
#     return a+b, a*b, a-b


# add, mul, cha = multi(3, 4)

# print(add)
# print(mul)
# print(cha)

# def test(name, age, gender=True):
#     print("나의 이름은 ()입니다.".format(name))
#     print("나의 나이는 ()입니다.".format(age))
#     if gender:
#         print("남자입니다.")

#     else:
#         print("무성별입니다.")


# test('김창순', 30, not True)


import requests
from bs4 import BeautifulSoup

# 1. 사이트 접속
url = "https://www.museum.go.kr/site/main/content/openinghour"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 2. 관람시간 크롤링
# 관람시간 정보가 들어 있는 클래스명을 찾아야 함
# .museum-time은 임시, 실제 클래스명을 확인해야 함
time_section = soup.select_one('div.info-txt info-time')
if time_section:
    print("관람시간:")
    print(time_section.get_text(strip=True))
else:
    print("관람시간 정보를 찾을 수 없습니다.")

# # 3. 관람료 크롤링
# price_section = soup.select_one('.museum-fee')  # .museum-fee도 임시, 구조에 따라 바꿔야 함
# if price_section:
#     print("\n관람료:")
#     print(price_section.get_text(strip=True))
# else:
#     print("관람료 정보를 찾을 수 없습니다.")
