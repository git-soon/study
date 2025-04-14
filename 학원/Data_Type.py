'''
# 데이터 타입(Data Type)
# 1. 숫자

# 정수 (int; integer) - 소수점 없는 숫자
from sys import getsizeof
a = 10

# 실수 (float) - 소수점 있는 숫자
b = 3.14

# 복소수 (complex) = 실수부와 허수부로 구성된 숫자
c = 3 + 4j

print(a, type(a))
print(b, type(b))
print(c, type(c))

# 2. 문자열 (string)
name = "창순"
print(name, type(name))

# 3. 불리언(bool; boolean)
참 = True
거짓 = False

print(참, type(참))
print(거짓, type(거짓))

# 비교 연산의 결과로 불리언 값을 얻을 수 있습니다.
print('bool', 10 > 5, type(10 > 5))
print('bool', 10 == 5, type(10 == 5))
print('bool', 10 <= 5, type(10 <= 5))

# none 타입
# 아직 값이 할당되지 않았음을 표시
result = None

str = '문자열 입니다.'
print(getsizeof(1))
print(getsizeof("문자열"))
print(getsizeof(str))

num = input("숫자를 입력 하시오 : ")
print(num)
a = num/2
print(a)
'''

'''
name = "안녕\n 하세요"
print(name)

country = "대한민국"
city = "서울"
people = "한국인"

text = "저는 올해 {0}살 입니다." .format(30)
print(text)
text = "저는 {0}사람이며 {1}에 살고 있습니다." .format(country, city)
print(text)
text = "제가 사는 {0}은은 {country}에 있습니다.".format(city, country="한국")
print(text)
text = "나는 {1}이다. {{ 그리고 }} {0}에 산다." .format(city, people)
print(text)

text = "{}점수 : {}점 \n{}점수 : {}점" .format("영어", 100, "수학", 90)
print(text)

a = "[{0:<10}]".format("hey")
print(a)
'''
''''''
# print the dog!
a = '''
       |\_/|
       |q p|    /}
       ( o )""""\
       |"^"      |
       ||_/=\\___| 
       '''

print(a, type(a))

back = "\\"
dot = '"'
emoji = '"^"'
dog_foot = "|_//=\\"

dog = "|\_/| %6s" % ""
print(dog)  # (\_/|      )

dog = "|q p| %4s/}" % ""
print(dog)  # (|q p|     /})

dog = "({0:^3})".format(0)
dog1 = "{0:{dot}>6}" .format(back, dot='"')
dog2 = dog + dog1
print(dog2)  # ( ( 0 )"""""\ )

dog = "|{0:>8}|" .format(emoji)
print(dog)  # || 사이에 "^"를 왼쪽으로 몰아 넣고 빈칸을을 5칸 넣을수 없나?

dog = "|{0:_>3}|" .format(dog_foot)
print(dog)

name = "김창순"
text = f'문자열 실습입니다. {{ name }}'
