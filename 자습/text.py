# 실습3
# 자판기 음료 리스트
vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']

# 1. 남은 음료수 확인 함수


def check_machine():
    print("남은 음료수:", vending_machine)

# 2. 음료수가 있는지 확인하는 함수


def is_drink(drink):
    return drink in vending_machine

# 3. 음료수를 추가하는 함수


def add_drink(drink):
    vending_machine.append(drink)
    vending_machine.sort()
    print("추가 완료")
    check_machine()


# 4. 음료수를 제거하는 함수
def remove_drink(drink):
    if is_drink(drink):
        vending_machine.remove(drink)
        print(f"{drink} 제거 완료")
    else:
        print(f"{drink}는(은) 목록에 없습니다.")
    check_machine()


while True:
    user = input("사용자 종류를 입력하세요:\n1.소비자\n2.주인\n(종료하려면 '종료' 입력): ")

    if user == "종료":
        print("프로그램을 종료합니다.")
        break

    if user == "1" or user == "소비자":
        drink = input("마시고 싶은 음료? ")
        if is_drink(drink):
            vending_machine.remove(drink)
            print(f'{drink} 드릴게요.')

        else:
            print(f"{drink}는(은) 지금 없네요.")

    elif user == "2" or user == "주인":
        work = input("할 일 선택:\n1.추가\n2.삭제\n")

        if work == "1" or work == "추가":
            drink = input("추가할 음료수?")
            add_drink(drink)

        elif work == "2" or work == "삭제":
            drink = input("삭제할 음료수?")
            remove_drink(drink)

    else:
        print("잘못된 값입니다.")
