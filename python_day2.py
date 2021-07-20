#수식
print((2+3)*5)  #25

number = (2+3)*5
print(number)   #25
number += 2     
print(number)   #27
number *= 2
print(number)   #54
number /= 2
print(number)   #27
number %= 5
print(number)   #2

#숫자처리함수

print(abs(-5))      #절댓값함수
print(pow(4,2))     #제곱함수
print(max(5, 12))   #12
print(min(5, 12))   #5
print(round(3.14))  #반올림함수 
print(round(4.99)) 

from math import *      #라이브러리 호출
print(floor(4.99))
print(ceil(4.99))
print(sqrt(16))

#랜덤 함수(난수)
from random import *
print(random())     #0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)     #0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))   #0 ~ 10 미만의 임의의 값 생성(형변환)

print(int(random() * 10) +1)   #1 ~ 10 이하의 임의의 값 생성(형변환)
print(int(random() * 45) +1)   #1 ~ 45 이하의 임의의 값 생성(형변환)

print(randrange(1, 46))   #1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45))   #1 ~ 45 이하의 임의의 값 생성


#퀴즈

#from random import *
date = int(randint(4, 28))
print("오프라인 스터디 모임 날짜는 매월", date, "일로 선정되었습니다.")
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")


#문자열
sentence = '나는 소년입니다'
print(sentence)
sentence = "파이썬은 쉬워요"
print(sentence)
sentence = """
나는 소년이고 
파이썬은 쉬워요
"""
print(sentence)


#슬라이싱
jumin = "000206-1234567"

print("성별 : " + jumin[7])     #7번째 출력
print("연 : " + jumin[0:2])     #0부터 2 직전까지. 즉 0번째와 1번째 출력
print("월 : " + jumin[2:4])     #2부터 4 직전까지. 즉 2번째와 3번째 출력
print("일 : " + jumin[4:6])     #4부터 6 직전까지. 즉 4번째와 5번째 출력 
print("생년월일 : " + jumin[:6])   #처음부터 6 직전까지. = jumin[0:6]
print("뒤 7자리 : " + jumin[7:])    #7부터 끝까지. = jumin[7:14]
print("뒤 7자리 (뒤에부터) : " + jumin[-7:])    #뒤에서 7번째(1부터 끝까지)


#문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())      #True
print(len(python))
print(python.replace("Python", "Java"))
# print(python)하면 똑같이 Python is Amazing 나옴

index = python.index("n")
print(index)        #제일 첫번째로 등장하는 n의 인덱스 출력 (5)
index = python.index("n", index + 1)    #그 다음으로 등장하는 n의 인덱스 출력 (15)
print(index)

print(python.find("n"))         #문자열 안에서 n이 등장하는 인덱스 출력 (5)
print(python.find("java"))      #find에서 찾기 실패하면 -1 반환
#print(python.index("Java"))     #index에서 찾기 실패한 경우 이 열부터 오류를 내고 끝내버림

print(python.count("n"))    #문자열 안에서 n이 몇번 나오는지 출력(2)


#문자열 포맷
print("a" + "b")
print("a", "b")

#방법 1 %사용
print("나는 %d살입니다." % 20)
print("나는 %s를 좋아해요" % "파이썬")
print("Apple은 %c로 시작해요" % "A")

#%s는 정수, 문자, 문자열 다 받을 수 있음
print("나는 %s살입니다." % 20)
print("나는 %s를 좋아해요" % "파이썬")
print("Apple은 %s로 시작해요" % "A")

print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))

#방법 2 format() 사용
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨강"))   #파란 - 0, 빨강 - 1. 파란-빨강 순으로 출력
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨강"))   #파란 - 0, 빨강 - 1. 빨강 - 파란 순으로 출력

#방법 3
print("나는 {age}살이며 {color}색을 좋아합니다.".format(age = 20, color = "빨간"))
print("나는 {age}살이며 {color}색을 좋아합니다.".format(color = "빨간", age = 20,))

#방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며 {color}색을 좋아해요")

