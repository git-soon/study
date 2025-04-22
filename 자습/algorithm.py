# # fizzbuzz
# for i in range(1, 51):
#     if (i % 3 == 0) and (i % 5 == 0):
#         print('fizzbizz', end=' ')

#     elif i % 3 == 0:
#         print('fizz', end=' ')

#     elif i % 5 == 0:
#         print('buzz', end=' ')

#     else:
#         print(i, end=' ')

# 자판기와 거스름돈 개수 조절
# 1. 시작
# 2. 투입금액
# 3. 상품 금액
# 4. 거스름돈 계산
# 5. 거스름돈 출력
# 6. 종료


# 1. 시작

# 2. 투입금액
insert_price = int(input("insert : "))

# 3. 상품 금액
product_price = int(input("product : "))

# 4. 거스름돈 계산
change = insert_price - product_price

# 5. 거스름돈 출력
# 5천원
r5000 = change//5000
q5000 = change % 5000
print('5000: ' + str(r5000))

# 천원
r1000 = q5000//1000
q1000 = q5000 % 1000
print('1000: ' + str(r1000))

# 5백원
r500 = q1000//500
q500 = q1000 % 500
print('500: ' + str(r500))

# 백원
r100 = q500//100
q100 = q500 % 100
print('100: ' + str(r100))

# 50원
r50 = q100//50
q50 = q100 % 50
print('50: ' + str(r50))

# 10원
r10 = q50//10
q10 = q50 % 10
print('10: ' + str(r10))

# 5원
r5 = q10//5
q5 = q10 % 5
print('50: ' + str(r5))

# 10원
r1 = q5//1
q1 = q5 % 1
print('1: ' + str(r1))


# 6. 종료
# 위 방식으로만 하면 제품 가격보다 적은 돈을 넣으면 - 오류 발생

# # 위 코드를 반복문을 사용하여 보다 직관적으로 만들기

# #1. 시작
# change_list = [5000, 1000, 500, 100, 50, 10, 5, 1]

# # 2. 투입금액
# insert_price = input("insert : ")

# # 3. 상품 금액
# product_price = input("product : ")

# # 4. 거스름돈 계산
# change = int(insert_price - product_price)

# for i in change_list:
#     r = change_list//i
#     change %= i
#     print(str(i) + ':' + str(r))
