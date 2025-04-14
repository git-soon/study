# #예외 처리
# try:
#     x = int(input("숫자를 입력하세요 : "))
#     result = 10/x

# except ZeroDivisionError as e:
#     print("예외 메세지", e)

# except ValueError as e:
#     print("예외 메세지", e)

# # 위 두개를 하나로 합칠수 있음 : 여러개의 예외처리를 한번에 할수 있다.
# except (ZeroDivisionError, ValueError) as f:
#     print("예외 메세지", f)

# else:
#     print(f'result : {result}')

# finally:
#     print("무조건 실행되는 부분")


# # 예외처리가 없었을때
# x = int(input("숫자를 입력하세요 : "))
# result = 10 / x
# #에러 발생

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    return a / b


try:
    result = divide(10, 2)

except ZeroDivisionError as e:
    print(e)

else:
    with open("result.txt ", "w", encoding="utf-8") as file:
        file.write(f'{result}')
