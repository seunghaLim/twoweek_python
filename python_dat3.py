# 탈출문자 
print("백문이 불여일견\n백견이 불여일타") #\n

# \" 랑 \' - 문장 내에서 따옴표 역할
#print("저는 "나도코딩" 입니다") - 오류남
print("저는 \"나도코딩\" 입니다")  

#\\ 문장 내에서 \만 찍힘
#print("C:\Users\LSH\source\Python") - 오류남
print("C:\\Users\\LSH\\source\\Python")

#\r 커서를 맨 앞으로 이동
print("Red Apple\rPine") #PineApple로 출력

#\t - 탭키

#\b - 앞에 문자 하나 삭제
print("Redd\bApple") #RedApple로 출력


#퀴즈

#http:// 제거
add = "http://naver.com"
add = add[7:]   #아니면 add = add.replace("http://", "")

#.com 제거
index = add.index(".")
add = add[0:index]  #아니면 add = add[:add.index(".")]


len = len(add)
num_e = add.count("e")

print(add[:3] + str(len) + str(num_e) + "!")


#리스트[] - 순서를 가지는 객체의 집합

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수", "하하"]
print(subway)

#조세호의 위치 구하기
print(subway.index("조세호"))

#뒤에서부터 다른 개체 넣기
subway.append("정준하")
print(subway)

#뒤에서부터 개체 빼기
print(subway.pop())
print(subway)

#유재석 조세호 사이에 김구라 에 넣기
subway.insert(1, "김구라")  #['유재석', '김구라', '조세호', '박명수', '하하']
print(subway)

#같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway.count("유재석"))

#정렬

num_list = [1, 5, 3, 4, 2]
num_list.sort()
print(num_list)

#역 정렬
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#자료형 상관 없음
list = [2, "조세호", True]
print(list)

#리스트 합치기
num_list = [1, 5, 3, 4, 2]

num_list.extend(list)      #인수로 넣은 값이 뒤에 가서 붙음
print(num_list)


#사전 자료형- {} 사용
#선언
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet)

#값 가져오기
#방법1
print(cabinet[3])       #유재석
print(cabinet[100])     #김태호
#print(cabinet[10])  #[]를 사용해서 없는 값을 가져올 경우 키에러가 뜸. 밑에 코드는 실행 안됨

#방법2
print(cabinet.get(3))
print(cabinet.get(10))  #get을 사용할 경우 오류는 안뜨고 NONE이라고만 뜸
print(cabinet.get(10, "잘못된 키 입니다"))  #NONE 말고 뒤에 넣어준 값으로 뜸

#키값에 해당하는 값이 있는지 확인
print(3 in cabinet)     #True
print(10 in cabinet)       #False

#인덱스 말고 문자열로도 캐비넷 선언 가능
cabinet2 = {"A-3": "유재석", "B-10": "박명수"}
print(cabinet2)     #{'A-3': '유재석', 'B-10': '박명수'}

#사전에 값 추가
print(cabinet2)
cabinet2["C-30"] = "정형돈"
cabinet2["A-3"] = "강호동"
print(cabinet2)     #{'A-3': '강호동', 'B-10': '박명수', 'C-30': '정형돈'}

#사전에 값 빼기
del cabinet2["A-3"]
print(cabinet2)     #{'B-10': '박명수', 'C-30': '정형돈'}

#키값만 출력
print(cabinet2.keys())

#값만 출력
print(cabinet2.values())

#키와 값 둘 다 출력
print(cabinet.items())

#사전 free
cabinet2.clear()
print(cabinet2)

#튜플 - 사전과 비슷하지만 삽입 및 삭제가 불가함. 동작 속도가 더 빠름. 변경되지 않는 목록 작성할 때 사용.
menu = ("돈까스", "고치돈")
print(menu)
print(menu[0])
print(menu[1]) 

#menu.add("가츠동")      #추가 안됨

(name, age, hobby) = ("임승하", 22, "영화감상")
print(name)
print(age)
print(hobby)

#집합(세트) - 중복이 안되고 순서가 없음
my_set = {1, 2, 3, 3, 4, 4, 5}
print(my_set)

python = {"유재석", "양세형", "김종국"}
java = set(["유재석", "박명수"])    #[]리스트로 선언해놓고 set함수를 통해 집합으로 선언 가능

#교집합
print(python & java)        #{'유재석'}
print(python.intersection(java))

#합집합
print(python | java)        #{'김종국', '유재석', '박명수', '양세형'}
print(python.union(java) )

#차집합
print(java - python)        #{'박명수'}
print(java.difference(python))

#집합에 원소 추가
python.add("김태호")
print(python)       #{'김종국', '유재석', '양세형', '김태호'}

#집합에 원소 제거
java.remove("박명수")
print(java)     #{'유재석'}

#자료구조의 변경
menu = {"커피", "우유", "마카롱"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))
from random import *

#퀴즈
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
shuffle(list)

gift = sample(list, 4)
chicken = gift.pop()

print("--당첨자 발표--")
print("치킨 당첨자: %d" % chicken)
print("커피 당첨자: " + str(gift))
print("--축하합니다--")

'''
from random import *
users = range(1, 21)    #그냥 range타입
users = list(users)     #list로 바꿔줌

suffle(users)

winners = sample(users, 4)

print("--당첨자 발표--")
print("치킨 당첨자: {0}".format(winers[0]))
print("커피 당첨자: {0}".format(winners[1:]))
print("--축하합니다--")


'''

