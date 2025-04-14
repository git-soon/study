# season = ['봄', '여름', '가을', '겨울']

# print(season)
# print('sesason[0] : ', season[0])


# text = 'hello'  # text = 1

# letters = list(text)
# print('letters', letters)  # letters ['h', 'e', 'l', 'l', 'o']

# shop = ['반팔', '청바지', '이어폰', ['무선 키보드', '유선 키보드', '기계식 키보드']]

# # 슬라이싱
# print(shop[0:])
# print(shop[:-2])

# # print(shop[10]) 에러


# shop[0] = '긴팔'
# print(shop)  # ['긴팔', '청바지', '이어폰', ['무선 키보드', '유선 키보드', '기계식 키보드']]

# del shop[0]
# print(shop)  # ['청바지', '이어폰', ['무선 키보드', '유선 키보드', '기계식 키보드']]

# del shop[0:1]
# print(shop)  # ['이어폰', ['무선 키보드', '유선 키보드', '기계식 키보드']]

# num1 = [1, 2, 3]
# num2 = [4, 5, 6]

# print('num1 + num2 : ', num1 + num2)  # num1 + num2 :  [1, 2, 3, 4, 5, 6]

# num1 = num1 + num2
# print(num1*2)  # [1,2,3,4,5,6,1,2,3,4,5,6]
# num1 = [5, 2, 7, 3]
# print(num1)

# num_asc = sorted(num1, reverse=True)
# print(num_asc)

# print('num1 : ', num1)
# num1.sort()pwd
# print('num1 : ', num1)
# num1.sort(reverse=True)
# print('num1 : ', num1)


# text = 'hello, world'
# list1 = list(text)
# print('list1 : ', list1)

# list1_asc = sorted(text)
# print(list1_asc)


# rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

# print('2번째 인덱스 :', rainbow[2])

# print('알파벳 순서로 정렬한값 출력 :', sorted(rainbow))

# rainbow.append('ivory')
# print('좋아하는색 맨 마지막에 추가 :', rainbow)

# del rainbow[2:6]
# print('3~6번째 값 삭제하기기 :', rainbow)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# value = matrix[1][2]

# print("matrix[1][2] : ", value)

# matrix[1] = matrix[1]+[100]
# print(matrix)

# matrix += [[10, 11, 12]]
# print(matrix)
# '''
# '''
# s1 = {1, 2, 3, 4, 5}
# s2 = {1, 3, 5, 7, 9}
# s3 = {2, 3, 4, 5, 6, 7}

# ss4 = s1.intersection(s3)
# print(ss4)
# s4 = s1.intersection(s3).difference(s2)
# print(s4)

# s4_1 = s1.intersection(s2, s3)
# print(s4_1)


# fruits = {"apple": '사과', "banana": '바나나', "kiwi": '키위'}
# print("fruits : ", fruits)

# fruits.update({'grape': '포도', 'melon': '멜론'})
# print(fruits)

# print(fruits.get("peach"))

# # 1
# student = {}
# print(student)

# # 2
# student = dict(Alice=85, Bob=90, Charlie=95)
# print(student)

# # 3,4
# student.update({"David": 80, "Alice": 88})
# print(student)

# # 5
# del student["Bob"]
# print(student)

a = 1
print(a % 2)
