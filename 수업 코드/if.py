# 조건문 시작

# if 조건식:
# 조건식이 참이라면 실행한다


# #1
# pass_word = (input("비밀번호를 입력하세요 : "))
# anser = "123abc"

# for i

# if pass_word == anser:
#     print("비밀번호가 맞습니다.")

# else:
#     print("비밀번호가 틀렸습니다.")

# # 2
# odd_number = int(input("숫자를 입력하세요 : "))

# if odd_number % 2 == 0:
#     print("짝수입니다.")

# else:
#     print("홀수입니다.")


# number = int(input("점수를 입력하세요 : "))

# if number >= 90 and number <= 100:
#     print("학점 : A")

# elif number >= 80:
#     print("학점 : B")

# elif number >= 70:
#     print("학점 : C")

# elif number >= 60 and number < 70:
#     print("학점 : D")

# elif number < 60:
#     print("학점 : F")

# else:
#     print("잘못 입력하셨습니다.")


# age = int(input("나이를 숫자로 입력해주세요"))
# payment = str(input("결재방법을 입력해주세요 (현금 또는 카드) : "))
# pay_cash = ["무료", "450원", "720원", "1200원", "무료"]
# pay_card = ["무료", "450원", "1000원", "1300원", "무료"]

# if age >= 75:
#     print(f"{age}세의 {payment} 요금은 {pay_cash[0]}입니다.")

# elif age >= 20:
#     if payment == "현금":
#         print(f"{age}세의 {payment} 요금은 {pay_cash[-2]}입니다.")

#     elif payment == "카드":
#         print(f"{age}세의 {payment} 요금은 {pay_card[-2]}입니다.")

# elif age >= 14:
#    if payment == "현금":
#         print(f"{age}세의 {payment} 요금은 {pay_cash[-3]}입니다.")

#     elif payment == "카드":
#         print(f"{age}세의 {payment} 요금은 {pay_card[-3]}입니다.")

# elif age >= 8:
#    if payment == "현금":
#         print(f"{age}세의 {payment} 요금은 {pay_cash[-4]}입니다.")

#     elif payment == "카드":
#         print(f"{age}세의 {payment} 요금은 {pay_card[-4]}입니다.")

# if age > 0:
#     print(f"{age}세의 {payment} 요금은 {pay_cash[0]}입니다.")


# fruit = input("과일을 한글로 입력하세요")

# if fruit in ['사과', '바나나', '복숭아']:

# fruit = input("과일을 영문으로 입력하세요.")
# fruit_cal = {"apple": 95, "banana": 105, "cherry": 50}

# if fruit in ["apple", "banana", "cherry"]:
#     if "apple":
#         print(f"{fruit}의 칼로리는 {fruit_cal[fruit]}Kcal 입니다.")
#     elif "banana":
#         print(f"{fruit}의 칼로리는 {fruit_cal[fruit]}Kcal 입니다.")
#     else:
#         print(f"{fruit}의 칼로리는 {fruit_cal[fruit]}Kcal 입니다.")

# else:
#     print("that fruit is`t include ")


# i = 0
# total = 0

# while i <= 10:
#     total += i
#     i += 1

# print(f'1부터 10까지의 합은 {total}입니다.')


# str 들가면 에러가 떠서 그거는 예외처리로 ㄱㄱ 해야할거같다.....
# i = 1
# plus = 0

# while True:
#     num = input("양수를 입력하세요('종료' 입력시 프로그램 종료) : ")
#     num_int = int(num)
#     if num == "종료":
#         break

#     if num_int > 0:
#         while i == num:
#             i += 1
#             plus += i
#             print(f"1부터 {num}까지의 합은 {plus}입니다.")

#     else:
#         print("양수만 입력 하세요")
#     continue

# print("프로그램을 종료합니다.")

# while True:
#     user_input = input("양수를 입력하세요 ('종료' 입력 시 프로그램 종료) :")

#     if user_input == "종료":
#         break

#     if not user_input.isdigit():
#         print("양수만 입력하세요.")
#         continue

#     # 입력된 숫자를 정수로 변환
#     number = int(user_input)

#     if number == 0:
#         continue

#     # 1부터 n까지의 합 계산
#     i = 1
#     total = 0
#     while i <= number:
#         total += i
#         i += 1
#     print(f'1부터 {number}까지의 합은 {total} 입니다.')


# numbers = [1, 2, 3, 4, 5]
# total = 0

# for num in numbers:
#     total += num
#     print(f'합계는 {total}입니다.')


# dict1 = {"name": "창순!", "age": 25, "지역": "서울", "hobby": ["캠핑", "오토바이"]}

# for key in dict1:
#     print(key, end='')
# print()


# # 구구단
# googoo = input("몇단을 출력할까요? :")
# for x in range(1, 10):
#     googoo1 = int(googoo)*x

#     print(f'{googoo} X {x} = {googoo1}', end='')


# # 정수 합 계산
# total = 0
# plus = int(input("어디까지 계산할까요 : "))

# for i in range(1, plus):
#     if i % 2 == 0:
#         total += i
# print(f'1부터 {plus}까지의 홀수의 합: {total}')


# # 평균값 구하기

# 학생1_성적 = {"국어": 83, "영어": 92, "수학": 88}
# 학생2_성적 = {"국어": 90, "영어": 79, "수학": 86}
# 학생3_성적 = {"국어": 88, "영어": 86, "수학": 94}
# student = {"학생1": 학생1_성적, "학생2": 학생2_성적, "학생3": 학생3_성적}

# 국어 = student["학생1"]["국어"] + student["학생2"]["국어"] + student["학생3"]["국어"]
# 영어 = student["학생1"]["국어"] + student["학생2"]["국어"] + student["학생3"]["국어"]
# 수학 = student["학생1"]["국어"] + student["학생2"]["국어"] + student["학생3"]["국어"]

# 국어_average = (국어)/len(values())
# 영어_average = (영어)/len(values())
# 수학_average = (수학)/len(values())


# print(
#     f'학생 3명의 국어 평균 점수는 {국어_average}, 영어 평균 점수는 {영어_average}, 수학 평균점수는 {수학_average}입니다.')


# for i in range(2, 10):
#     print()
#     print(f'[{i}단]')
#     for j in range(1, 10):
#         print(f'{i} X {j} = ', i*j)


# 조건1 사용자는 소비자, 주인 두가지 종류로 입력받기, 그 외에 값은 잘못된 값으로 출력력
# 소비자 일때 마시고 싶은 음료 입력받기
# 갑싱 있으면 벤딩에서 제거, 없으염ㄴ 없음 출력


vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']
user = input("1.소비자\n2.주인\n \n사용자 종류를 입력하세요 :")

serch = vending_machine.index(consumer)

while True:
    if user == "종료":
        break

    if user == "소비자" or 1:
        consumer = input("마시고 싶은 음료? ")

        if consumer in vending_machine:
            print(f'{consumer}드릴게요~')
            vending_machine.remove(consumer)  # 삭제하는거 드가야됨

        else:
            print('없음')

    elif user == "주인" or 2:
        owner = input("1.추가 \n2.삭제 \n할 일 선택 : ")

        if owner == '추가' or 1:
            owner_to_do = input('추가할 음료수? : ')
            vending_machine.append(owner_to_do)
            vending_machine.sort()

        elif owner == "삭제" or 2:
            owner_to_do2 = input('삭제할 음료수? :')
            vending_machine.remove()

        else:
            print("잘못 입력하셨습니다. 다시 선택해 주세요요")
            continue

    else:
        print("잘못 입력하셨습니다. 다시 입력해 주세요")
        continue
