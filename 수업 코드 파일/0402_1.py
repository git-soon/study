# #재귀함수
# def sos(i):
#     print("help me!!!")
#     if i == 1: #종료조건
#         return ""
#     else:
#         return sos(i - 1)

# sos(10)

# #팩토리얼
# def factorial(n):
#     print("n의값 ", n)
#     if n == 1: # 종료 조건
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# print(factorial(5))   
# # n => else => 5 * factorial(4) 
# # n = 4 => 4 * factorial(3)
# # n = 3 => 3 * factorial(2)
# # n = 2 => 2 * factorial(1)
# # n = 1 

# #실습. 피보나치 수열
# def fibonacci(n):
#     if n == 0:
#         return 0 
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(6))


# 람다식
# # 일반함수
# def add(x, y):
#     return x + y
# print(add(3, 4))
# 람다함수
# add = lambda x, y : x + y
# print(add(5, 6))

# 매개변수가 1개인 람다 함수
# oneup = lambda x : x + 1
# print(oneup(1))
# print((lambda x : x + 1)(1))

# square = lambda x : x ** 2
# print(square(4))
# print((lambda x : x ** 2)(4))


# # 람다함수를 매개변수로 전달
# def call(func):
#     for _ in range(10):
#         func()

# # def hello():
# #     print("안녕하세요")

# # call(hello)
# call(lambda : print("안녕하세요"))

#map() 람다이용
# numbers = [2, 4, 6, 8]
# def square(x):
#     return x ** 2
# print(list(map(square, numbers)))

# print(list(map(lambda x: x ** 2, numbers)))

#filter() 람다이용
# numbers = [1,2,3,4,5,6,7,8,9]
# def even_number(x):
#     return x % 2 == 0
# print(list(filter(even_number, numbers)))
# print(list(filter(lambda x : x % 2 != 0 , numbers)))

# 실습4. 함수만들기를 람다식으로 작성
# def counts(num):
#     lists = list(filter(lambda x :  x % num == 0, range(1, 31)))
#     return lists, len(lists)

# num = 6
# lists, count = counts(num)
# print(f"{num}의 배수 : {lists}")
# print(f"{num}의 배수의 개수 : {count}")

# 실습6. 힌트
city = "서울"
x = [
    ["서울", 10],
    ["부산", 20],
    ["서울", 30]
]
a = filter(lambda x: x[0] == city, x)
# print(list(a))
print(list(map(lambda x: x[1], a)))