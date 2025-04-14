# # 창고 정리
# def solution(storage, num):
#     clean_storage = []
#     clean_num = []
#     for i in range(len(storage)):
#         if storage[i] in clean_storage:
#             pos = clean_storage.index(storage[i])
#             clean_num[pos] += num[i]
#         else:
#             clean_storage.append(num[i])
#             clean_num.append(num[i])

#     # 아래 코드에는 틀린 부분이 없습니다.

#     max_num = max(clean_num)
#     answer = clean_storage[clean_num.index(max_num)]
#     return answer


# solution(["pencil", "pencil", "pencil", "book"], [2, 4, 3, 1])

# num_list = input("리스트 삽입")
# answer = []

# if num_list[-1] > num_list[-2]:
#     fin1 = num_list[-1] - num_list[-2]

#     answer = num_list.append(fin1)

# elif num_list[-1] < num_list[-2]:
#     answer = num_list.append(num_list[-1]*2)

# print(answer)


# a = 10
# b = 20

# c = a + b
# d = a*b
# e = c**2


# z = ["q", "w", "e", 'r', 't']
# print(type(z[2]))

def solution(arr, queries):
    answer = []

    for i in queries:
        i += 1
        a = queries[i][0]
        b = queries[i][1]

    for n in arr:
        temp = n.replace(a, b)
        temp1 = n.replace(b, a)

        answer.append(temp1)
    return answer
