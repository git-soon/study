# 모듈
# # 방법1
# import calc
# print(calc.add(10, 1))

# # 방법2
# import calc as a
# print(a.add(10, 1))

# # 방법3
# from calc import add as aa, sub as a
# print(aa(1, 2))
# print(a(10, 2))

# # 방법4
# from calc import *
# print(add(10, 20))
# print(mutiply(3, 4))

# 표준모듈

#from datetime import datetime, timedelta, timezone
# now = datetime.today() #현재시간
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

# print(f"{now.year}년 {now.month}월 {now.day}일")

#now = datetime.now() 
# print(now)

# # 특정 날짜 계산
# next_week = now + timedelta(weeks=2,)
# print(next_week)

# 타임존
# print(timezone.utc)
# print(datetime.now(timezone.utc))
# print(datetime.now(timezone(timedelta(hours=9))))

# 날짜 포멧 변경
# print(now.strftime("%Y년%m월%d일 %H:%M:%S"))

# from datetime import date, datetime

# open_day = date(year=2025, month=3, day=24)
# #print(date.today())
# #print(date.today().weekday())
# week = ["월", "화", "수", "목", "금", "토", "일"]
# print(week[date.today().weekday()])
# now  = datetime.now()
# print(now.strftime(f"%Y년 %m월 %d일({week[date.today().weekday()]})"))

# # 지나간 날짜 계산
# pass_day = date.today() - open_day
# print(f"개강 후 {pass_day.days}일이 지났습니다")


# # time 모듈
# import time

# # 현재시간 출력
# print(time.time())
# #print(time.localtime())
# # print("5초대기")
# # time.sleep(5)
# # print("대기완료")
# start = time.perf_counter() # 정밀시간측정
# time.sleep(2)
# end = time.perf_counter()
# print(f"{end - start:.5f}")

# 수학모듈
# import math

# print(math.pi)
# print(math.sqrt(25))
# print(math.factorial(5))
# print(math.ceil(2.3)) #올림
# print(round(4.6)) #반올림
# print(math.floor(7.9)) #내림


# # random 모듈
# import random
# import math

# print(random.randint(100, 999)) #정수리턴
# print(random.uniform(1.1, 9.9)) #실수리턴
# print(random.random())
# print(random.randrange(100, 999)) # 두번째 인수는 미포함
# choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(random.choice(choices))

# rand = 1000 + math.floor(random.random() * 9000)
# print(rand)


# # 실습. 로또 번호 뽑기
# import random

# # lotto = set()
# # while len(lotto) < 6:
# #     lotto.add(random.randint(1, 45))
# # print(sorted(lotto))

# lotto = random.sample(range(1, 46), 6)
# print(sorted(lotto))


# import sys

# #print(sys.argv)

# if "-h" in sys.argv or "--help" in sys.argv:
#     print("사용법: python main.py [옵션]")
#     print("-h, --help       도움말표시")
#     print("-v, --version    버전정보표시")
#     sys.exit(0)

# if "-v" in sys.argv or "--version" in sys.argv:
#     print("버전 : 1.0.0")
#     sys.exit(0)

#import os

# # print(os.getcwd())
# # os.chdir(os.getcwd()) #경로이동
# # dir = os.popen('dir')
# # print(dir.read())
#os.mkdir("test")
#os.rmdir("test")
#print(os.environ.get("PATH"))


import json

data = {
    "name": '홍길동', 
    'age': 20,
    'city': '서울'
}

json_str = json.dumps(data)
print(json_str)

json_obj = json.loads (json_str)
print(json_obj)