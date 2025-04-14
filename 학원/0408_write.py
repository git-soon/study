# 파일 입출력

# # 파일 쓰기
# with open("test.txt", "w", encoding="utf-8")as file:
#     file.write("안녕하세요\n")
#     file.write("파이썬 파일 쓰기 연습 \n")


# # 내용 쓰기
# with open("test.txt", "a", encoding="utf-8") as file:
#     file.write("내용추가")
#     file.write("1234568")  # 숫자는 문자열 형태로 작성


# # 여러개를 한번에 추가
# line = ["첫 번째\n", "두번째\n", "세번째\n"]
# with open("list.txt", "w", encoding="utf-8") as f:
#     f.writelines(line)

# # 사용자로부터 내용 입력 받기
# with open("user.txt", "w", encoding="utf-8") as f:
#     while True:
#         line = input("파일에 넣을 문자열 입력 (종료하려면 '종료' 입력) : ")
#         if line == "종료":
#             print("입력을 종료 합니다.")
#             break

#         f.write(line + "\n")


# # 파일 읽기

# with open("user.txt", "r", encoding="utf-8") as file:
#     print(file.read)

# with open("user.txt", "r", encoding="utf-8") as file:
#     print(file.readline())
#     print(file.readline())

# with open("user.txt", "r", encoding="utf-8") as file:
#     print(file.readlines)

# #공백 제거
# with open("user.txt","r",encoding="utf-8") as file:
#     line = file.readline()
#     while line:
#         print(line.strip())
#         line = file.readline()

# # enumerate(리스트) – 리스트의 요소들을 튜플형태로 (인덱스, 요소값) 으로 반환 : 봔환값이 두개 (인덱스,값)
# with open("user.txt", "r", encoding="utf-8") as file:
#     line = file.readlines()

#     for idx, value in enumerate(line):
#         print(f'{idx} 인덱스 값은 : {value.strip()} 입니다.')

# 바이너리 : 바이너리 파일이란 영상, 이미지, 음성 등이 대부분인 파일로 0과 1로 이루어진 파일이다.

with open("avi.jpeg", "rb") as file:

    # data = file.read()
    # print(f'{len(data)} 바이트')
    header = file.read(10)
    print(header)
    # png 파일은 항상 b'\x89png\
    # jpg 파일은 항상 b'\xff\xd8\xff\xe0\x00\


def identitiy_file(file_path):

    with open(file_path, "rb") as file:
        header = file.read(4)  # 4바이트가 확장자의 매직넘머
        print(header)

        if header[:2] == b'\xff\xd8':  # jpg 2바이트. 뒤 2바이트삭제
            return "jpg" or "jpeg"

        elif header == b'\x89PNG':  # png 첫 4 바이트가 89 50 4e 47
            return "png"

        else:
            return "unknown"
