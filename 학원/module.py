# import random
# from datetime import datetime
# # timedelta = 값들을 반환 : 시간 계산할수 있게 해주는 뭐 그런거
# # timezone : 시간대 말하는거 , utc = 영국 그리니치 천문대 시간, 기중
# # timesteamp : 1970년대 부터 영국 시간대 숫자 카운트 하는거
# # 타임 관련된것을 많이 찾아 보는게 좋다


# # time 모듈
# import time

# # 현제시간 출력
# print(time.time())
# print(time.localtime())
# print("5초 대기")
# time.sleep(5)  # sleep = 대기 ,sleep(5) = 5초 대기
# print("대기완료")

# start = time.perf_counter()  # 정밀 시간측정
# time.sleep(2)
# end = time.perf_counter()
# print(end-start)

# # 실습. 로또 번호 뽑기 ----------------------------------------
# # 1. 1~45 까지의 수 중에서 랜덤으로 6개의 숫자를 뽑는다
# # 2. 6개의 숫자 중 중복되는 숫자가 없도록 한다.
# # 3. 오름차순으로 정렬 한다.

# import random
# result = []

# for _ in range(6):
#     lotto = random.randint(1, 45)

#     if lotto not in result:  # 중복 안되게
#         result.append(lotto)

# result.sort()
# print(f'실행결과 : \n{result}')

# #-------------------------------------------------------------

# #실습 수업

# lotto = random.sample(range(1,46),6)
# print(lotto)


# import os
# import sys
# print(sys.argv)


# print(os.getcwd())  # 현재 작업 경로 출력
# os.chdir(os.getcwd())  # 현재 작업 경로 dlehd
# dir = os.popen('dir')  # dir = 디렉토리
# print(dir.read())  # 현재 작업 경로의 파일 목록 출력
# # os.mkdir('test')  # test 폴더 생성
# os.rmdir('test')  # test 폴더 삭제
# # os.rename('test','test2') # test 폴더 이름 변경
# print(os.environ.get('PATH'))  # 환경변수 출력
# print(os.path.abspath('test'))  # test 폴더의 절대 경로 출력

# 쌍 따옴표면 제이슨이고
# 홑 따옴표면 파이썬 딕셔너리다
# 제이슨은 자바스크립트에서 사용하는 데이터 형식이다.


# 실습 타자 연습게임 -----------------------------
# 게임이 시작되면 영어 단어가 화면에 표시된다.
# 사용자는 해당 단어를 최대한 빠르고 정확하게 입력해야 한다.
# 바르게 입력했으면 다음 문제로 넘어가고 "통과"를 출력한다.
# 오타가 나면 "오타"를 출력하고 다시 입력을 받는다.
# 종료 조건을 생성하여 종료시 게임시간을 측정한다.
# 게임을 시작하는 함수와 단어 목록을 추가한다.

# 내가 한거
# 시작
# 시작 시간 저장
# 영어 단어 화면표시 (words 에서 random으로 1개씩 뽑아오기)
# 영어 단어 input
# 정확히 입력 = 다음단어, 잘못 입력 = print(오타 다시 입력하세요.), 이거 for 문인가? while도 되것네
# 종료 조건을 입력하면 게임 종료 , 입력한 단어 개수, 걸린시간, 평균 단어당 입력시간 프린트


import time
import random

words = ["mountain", "river", "ocean", "forest",
         "desert", "tree", "flower", "ditto"]
i = 0


def random__word(self, r_word):
    self.r_word = r_word
    r_word = words[random.sample(1, 6)]
    print(r_word)


start = time.perf_counter()
while i < len(words):

    print(f'{i+1}번째')
    print(f'단어 : {random__word}')
    answer = input("입력 : ")

    if answer == "종료" or 'q':
        break

    if answer == random__word:
        print('통과')
        i += 1
        # 그리고 다음 넘어가는거 어케하지?

    else:
        print("오타! 다시 입력하세요")

    end = time.perf_counter()
    total_t = end - start

print(f"총 {i} 개의 단어를 입력하셨습니다.")
print(f"총 걸린 시간 : {total_t:.2f}초")
print(f'평균 단어당 입력 시간 : {total_t/i:.2f}초 입니다.')


# return 과 break 차이점
