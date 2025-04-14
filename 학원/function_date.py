
date = "20250325"

print(date[:4] + "년" + date[4:6] + "월" + date[6:] + "일")

# 1번
name = input("이름을 입력하세요:")
age = int(input("나이를 입력하세요:"))
print("안녕하세요 %s님 ( %d세 )" % (name, age))

# 2번
name = input("이름을 입력하세요:")
birth_year = int(input("태어난 년도를 입력하세요:"))
this_year = int(input("올해 년도를 입력하세요:"))
age = this_year - birth_year + 1
print("올해는 %d년, %s님의 나이는 %d세 입니다." % (this_year, name, age))
