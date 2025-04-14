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


# # 실습 4 내가 하려는거거
# num = input("구하려는 배수 값을 입력하세요 : ")

# for i in range(num1, num2):
#     i += 1


# def number_times(num1, num2):
#     count = 0

#     def no_less(x):
#         result = num2 % num1 == 0
#         return

#     for _ in range(num2):

#         if num2 % num1 == 0:
#             count += 1
#             times = list(filter((no_less, )))

#     return print(f'{times}\n{num1}의 배수의 개수 :', count)


# number_times(3, 30)

# # 한꺼번에 여러개 반환


# def get_return():
#     arr = ["사과", "바나나"]
#     dic = {
#         "name": "홍길동"
#         "age": 20
#     }
#     num = 30
#     return arr, dic, num


# arr, dic, num = get_return()
# print(arr)
# print(dic)
# print(num)


# # 실습 4 강의

# # 방법 1.
# def counts(num):
#     lists = [i for i in range(1, 31) if i % num == 0:]
#     count = len(lists)
#     return lists, count


# num = 4
# lists, count = counts(num)
# print(f'{num}의 배수 : {lists}')
# print(f'{num}의 배수의 개수 : {count}')

# # 방법 2


# def count(num):
#     # 중첩함수 - 이 함수 내에서만 사용이 가능
#     def check(x):
#         return x % num == 0

#     list = list(filter(check,range(1,31)))
#     retun lists, len(lists)


# #재귀함수
# def sos(i):
#     print("help me")
#     if i == 1: #종료 조건
#         return ""
    
#     else:
#         return sos(i-1)
    
# sos(10)

# #팩토리얼
# def factorial(n):
#     print("n의 값 : ",n)
#     if n == 1: #종료 조건
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# factorial(5)
                   
# #피보나치 수열 (내가 하는거)

# def fibonacci(n):
#     f = 0 #순서 변수
#     g = 1 #수열 변수
#     f += 1
#     g += fibonacci(n-1) +fibonacci(n-2)
#     print(f"{f}번째 숫자", g)
#     if f == n + 1: # 종료조건
#         return ""
     
#     else:
#         return (n-1) + (n-2) #재귀 단계
    
# #순서 변수, 수열 변수 따로따로 해야...


# #피보나치 수열 (수업)
# def fibonacci(n):

#     if n == 0:
#         return 0
    
#     elif n == 1:
#         return 1
    
#     else:
#         return fibonacci( n - 1 ) + fibonacci ( n - 2 )

# print(fibonacci(10))

# #람다식
# add = lambda x,y : x + y
# print(add(5,6))

# #일반식 
# def add(x,y):
#     return x + y

# # 매개 변수가 1개인 람다 함수
# oneup = lambda x : x + 1
# print(oneup(1))
# print((lambda x : x + 1)(1))

# square = lambda x : x**2
# print(square(4))
# print((lambda x : x**2)(4))


# #람다 함수를 매개변수로 전달
# def call(func):
#     for __ in range(10):
#         func()

# def hello():
#     print("안녕하세요")

# #call hello
# call(lambda : print("안녕하세요"))


# map with lambda

numbers = [1,2,3,4,5,6,7,8,9,10]

# #지금까지 했던 코드
# def square(x):
#     return x**2

# print(list(map(square, numbers)))

# #lambda
# print(list(map(lambda x : x**2, numbers)))

# #filter with lambda
# def even_number(x):
#     return x % 2 == 0

# print(list((filter(even_number,numbers))))

# print(list(filter(lambda x : x % 2 == 0,numbers)))

#실습 4 with lambda 

num = int(input("구하려는 배수를 넣어주세요 : "))
num_print = list(filter(lambda x : x % num == 0, range(1,31)))
print(num_print)
print(f'{num}의 배수의 개수 : {len(num_print)}')


# 실습 6. 함수 종합 프로그래밍
# 데이터 분석 할수있는 함수들을 생성하여 제작
# 1. 도시별 평균 기온 계산
# 2. 도시별 최고/ 최소 기온 찾기
# 3. 도시별 강수량 분석
# 4. 데이터 추가
# 5. 전체 데이터 출력
# 6. 종료

start_menu = input("[날씨 데이터 분석 프로그램] \n 1.평균 기온 계산  \n 2. 최고//최저 기온 찾기 \n 3. 강수량 분석 \n 4. 날씨 데이터 추가 \n 5.전체 데이터 출력 \n 6.종료 \n 원하는 기능의 번호를 입력하세요 : " )
day_input = input("원하는 날짜를 입력하세요 (YYYY-MM-DD) : ")
city = input("도시 이름을 입력하세요")
avg_teamp = input("평균 기온을 입력하세요(`C) : ")
rain_input = input("강수량을 입력하세요(mm) : ")

wheather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-21", "서울", 8.3, 0.0],
    ["2024-11-21", "부산", 12.0, 0.0]
]

while True:

    # 1. 도시별 평균 기온 계산
    if start_menu == "1":
        if city == "서울":
            a = filter(lambda x : wheather_data[1] == city, wheather_data ) # 서울만 값 분리하기기
            b = list(map(lambda x : x[2], a)) #서울의 평균 기온 값만 뽑아낸거
            # 이 다음은 뽑아낸 기온들 다 더해서 list 길이 만큼 나누면 되는거 같은데 ()
            print(pass)

        elif city == "부산":
            a = filter(lambda x : wheather_data[1] == city, wheather_data ) # 부산
            b = list(map(lambda x : x[2], a)) #부산의 평균 기온 값만 뽑아낸거
         



    # 2. 도시별 최고 최대 기온 찾기
    elif start_menu == "2":
         if city == "서울":
            a = filter(lambda x : wheather_data[1] == city, wheather_data ) # 서울만 값 분리하기기
            b = list(map(lambda x : x[2], a)) #서울의 평균 기온 값만 뽑아낸거
            # 이 다음은 
            print(pass)

        elif city == "부산":
            a = filter(lambda x : wheather_data[1] == city, wheather_data ) # 부산
            b = list(map(lambda x : x[2], a)) 
    
    
    # 3. 강수량 분석
    
    
    # 4. 데이터 추가
    
    
    # 5. 전체 데이터 출력
    
    # 6. 종료
    if start_menu == "6":
        break