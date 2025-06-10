# # 구구단을 외자 구ㅜ단을 웨좌!!!!

# def goo_goo_dan(dan, end):
#     print(f'{dan}단')
#     for i in range(1, end):
#         print(f'{dan} X {i} = {dan * i}')


# goo_goo_dan(9, 25)

# def say_hello(year, name):
#     age = 2025 - year + 1
#     print(f'{name}님의 나이는 {age} 입니다.')


# say_hello(1996, "순대")

# def calc_sum(num1, num2):
#     total = 0
#     for i in range(num1, num2+1):
#         total += i

#     return total

# print(calc_sum(1, 10))

# def fruits():
#     return ["apple", "banana", "kiwi", "ananas"]


# print(fruits())


# def students():
#     return {
#         "name": "치엥",
#         "age": 20,
#         "major": "electric"
#     }


# def same(num1, num2):
#     if num1 == num2:
#         print("결과(곱) : ", num1 * num2)

#     else:
#         print("결과(합) : ", num1 + num2)


# print(same(2, 2))

# price = int(input("가격을 입력해 주세요. : "))

# def deliver(price):
#     print(price)
#     deliver_price = 2500
#     if price < 20000:
#         price += deliver_price

#     elif price >= 20000:
#         price = price

#     else:
#         print("잘못된 금액 입니다. 다시 입력해 주세요")

#     return price


# print(f'상품의 가격 : {deliver(price)}원 입니다.')

# def times(num):
#     return [i**2 for i in num]


# number = [2, 3, 4, 5, 6]
# print(times(number))


# vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']
# user = input("1.소비자\n2.주인\n \n사용자 종류를 입력하세요 :")

# serch = vending_machine.index(consumer)

# # while True:
# #     if user == "종료":
# #         break

# #     if user == "소비자" or "1":
# #         consumer = input("마시고 싶은 음료? ")

# #         if consumer in vending_machine:
# #             print(f'{consumer}드릴게요~')
# #             vending_machine.remove(consumer)  # 삭제하는거 드가야됨

# #         else:
# #             print('없음')

# #     elif user == "주인" or 2:
# #         owner = input("1.추가 \n2.삭제 \n할 일 선택 : ")

# #         if owner == '추가' or 1:
# #             owner_to_do = input('추가할 음료수? : ')
# #             vending_machine.append(owner_to_do)
# #             vending_machine.sort()

# #         elif owner == "삭제" or 2:
# #             owner_to_do2 = input('삭제할 음료수? :')
# #             vending_machine.remove()

# #         else:
# #             print("잘못 입력하셨습니다. 다시 선택해 주세요요")
# #             continue

# #     else:
# #         print("잘못 입력하셨습니다. 다시 입력해 주세요")
# #         continue

# # 1. check_machine : 남은 음료수를 확인할 수 있는 함수

# def check_machine():
#     if user == "남은 음료수 확인":
#     return print(vending_machine)

# # 2. 음료수가 있는지 확인하는 함수
# # 2-1. 입력받은 음료수가 리스트 내에 있는지 확인
# # : vending_machine.index(check), check = input("찾으실 음료 이름을 작성해 주세요 : ")
# # 2-3. 있으면 있다고 프린트, 없으면 없다고 프린트

# #수업때 한거

# 1. 남은 음료수가 있는지 확인 할수 있는 함수
# def check_machine(drink):
#     return drink in vending_machine

# 2. 음료수가 있는지 확인하는 함수
# def is_drink():


# 3. 음료수를 추가하는 함수
# def add_drink():


# 4. 음료수를 제거하는 함수


# #내가 한거거
# check = input("찾으실 음료 이름을 작성해 주세요 : ")
# def is_drink(check):
#     if vending_machine.index(check) != ValueError:
#         print(f'{check}가(이) 존재합니다.')

#     else:
#         try:
#             vending_machine.index(check)
#         except ValueError:
#             print(f'{check}가(이) 존재 하지 않습니다.')

# 3.음료수 추가 함수수


# def add_drink(owner_to_do):
#     owner_to_do = input('추가할 음료수? : ')
#     vending_machine.append(owner_to_do)
#     vending_machine.sort()


# # 기본 매개변수
# def pr_str(txt="안녕하세요", count=1):
#     for _ in range(count):
#         print(txt)


# pr_str()
# pr_str("반갑습니다.")
# pr_str("어서 오세요", 3)

# # 만약 pr_str("어서 오세요", 3)이걸 어서오세요 말고 안녕하세요 3번 쓰고 싶으면 그냥 pr_str(count = 3)이렇게 하면된다.


# # _ 이거 그러면 txt를 받는거 맞나 ?
# # 그러면 뒤에 for _ in _ 하면 뒤에 _는 count 받는거 아닌가?

# # 함수 호출 키워드


# def intro(name, age, city):
#     print(f'{name}의 나이는 {age} 이고 {city}에 삽니다.')


# intro("홍길동", 30, "마포구")
# intro(city="서울 마포구", name="임꺽정", age=30)
# intro(city="서울 마포구", name="임꺽정", 30)
# # 아니 그냥 city 는 30 되서 30에 삽니다 이렇게는 안되나?

# # 가변 매개 변수


# # def calc_avg(*args):
# #     print(args)
# #     total = 0
# #     for i in args:
# #         total += i
# #     return total/len(args)


# # print(calc_avg(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# def text_def(a, b, *args):
#     print("a :", a)
#     print("b :", b)
#     print("args : ", args)


# text_def(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# # 결과값 a = 1, b=2, args = (3,4,5,6,7,8,9,10)


# def text_def(a, b, c, *args):
#     print("a :", a)
#     print("b :", b)
#     print("args : ", args)


# text_def(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# # 결과값 a = 1, b=2, args = (4,5,6,7,8,9,10) 왜냐면 3은 c 가 할당
# # 따라서 args는 앞에꺼 다 할당하고 나머지들 모두를 할당한다다

# # 가변 키워드 매개변수


# def intro(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key} : {value}')


# intro(name="홍길동", gender="남자", age=20, city="서울 용산구")


# # 내장함수
# # 절대값 - abs(정수)
# def myabs(x):
#     if x < 0:
#         return -x

#     else:
#         return x


# print(myabs(-10))
# print(abs(-20))

# # 거듭 제곱
# print(pow(3, 4))


# def my_poe(x, y):
#     num = 1
#     for i in range(y):
#         print(f'i = {i},{num*x} = {num} x {x}')

# # num =1 은 왜한거지?

# # map = 함수를 써서 리스트 만드는거 - 좀만더 해보면 이해 될듯듯


# def square(x):
#     return x ** 3


# numbers = [2, 4, 6, 8]
# squared = map(square, numbers)
# print(list(squared))

# # filter - 함수 조건으로 리스트 값 걸러 내는거거


# def even_number(x):
#     result = x % 2 == 0
#     return result


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# print(list(filter(even_number, numbers)))


# 실습 4 내가 하려는거거
num = input("구하려는 배수 값을 입력하세요 : ")

for i in range(num1, num2):
i += 1


def number_times(num1, num2):
    count = 0

    def no_less(x):
        result = num2 % num1 == 0
        return

    for _ in range(num2):

        if num2 % num1 == 0:
            count += 1
            times = list(filter((no_less, )))

    return print(f'{times}\n{num1}의 배수의 개수 :', count)


number_times(3, 30)

# 한꺼번에 여러개 반환


def get_return():
    arr = ["사과", "바나나"]
    dic = {
        "name": "홍길동"
        "age": 20
    }
    num = 30
    return arr, dic, num


arr, dic, num = get_return()
print(arr)
print(dic)
print(num)


# 실습 4 강의

# 방법 1.
def counts(num):
    lists = [i for i in range(1, 31) if i % num == 0:]
    count = len(lists)
    return lists, count


num = 4
lists, count = counts(num)
print(f'{num}의 배수 : {lists}')
print(f'{num}의 배수의 개수 : {count}')

# 방법 2


def count(num):
    # 중첩함수 - 이 함수 내에서만 사용이 가능
    def check(x):
        return x % num == 0

    list =
