#조건문
'''
if 조건 :
    실행할 내용
elif 조건 :
    실행할 내용
else:
    실행할 내용
'''

weather = "비"

if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없음")


weather = input("오늘 날씨는 어때요? ") #문장을 실행하고 나서 사용자에게 입력값을 받는 함수. 입력값은 항상 문자열로 받음
if weather == "비" or weather == "눈":
    print("우산")
elif weather == "미세먼지":
    print("마스크")
else:
    print("준비물 필요 없음")

temp = int(input("기온은 어때요? "))    #int로 형변환 시켜줘야함
if temp > 30:
    print("더워")
elif temp > 20 and temp <= 30 : 
    print("적당")
elif temp <= 20:
    print("조금 쌀쌀함")
else:
    print("추워")


#반복문
for waiting_num in [0, 1, 2, 3, 4]:
    print("대기번호: {}".format(waiting_num))

for waiting_num in range(5):    #0부터 시작해서 5 직전까지. 01234
    print("대기번호: {}".format(waiting_num))

for waiting_num in range(1, 6):     #1부터 시작해서 6 직전까지. 12345
    print("대기번호: {}".format(waiting_num))

starbucks = ["아이언맨", "블랙 위도우", "캡틴 아메리카"]
for customers in starbucks:
    print("{0}님, 주문하신 커피 나왔습니다.".format(customers)) 

while
'''
while 조건:
    실행할 내용
'''

customer = "토르"
count = 5
while count > 0:
    print("{0}님, 주문하신 커피 나왔습니다. 호출 {1}번 남았습니다".format(customer, count))
    count -= 1
    if (count == 0):
        print("{}님, 커피는 폐기처리 되었습니다".format(customer))

count = 1
while True:       #무한루프 만들기
    print("{0}님, 주문하신 커피 나왔습니다. 호출 {1}회 째".format("아이언맨", count))
    count += 1


customer = "토르"
person = "Unknown"

while customer != person:
    print("{}님, 주문하신 커피 나왔습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")

print("맛있게 드세요, {}님!".format(customer))

#break랑 continue 사용

absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue    #continue를 만나면 밑에 명령 실행하지 않고 다음 반복으로 넘어감 
    if student in no_book:
        print("자습해라. {0}은 교무실로 따라와".format(student))
        break   #반복문 반복 중지
     
    print("{0}번, 일어나서 책 읽어라".format(student))

#한줄 for문 for 변수 in 범위
#출석번호 1,2,3,4,5에 100씩 더하기로 함

student = [1, 2, 3, 4, 5]
student = [i+100 for i in student]
print(student)

#학생 이름을 길이로 변환
student = ["Iron man", "Black Widow", "Thor"]
lenth = [len(i) for i in student]
print(lenth)

#학생 이름을 대문자로 변환
student = ["Iron man", "Black Widow", "Thor"]
upper = [i.upper() for i in student]
print(upper)

#퀴즈
from random import *
count = 0       #총 탑승 승객 수
for customer in range(1, 51):
    time = randrange(1, 51) 
    if time >= 5 and time <= 15:        # if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
        count += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
print("총 탑승 승객 : {} 분".format(count))

#함수
#함수 정의 - def 함수이름():
#아규먼트 - 괄호 사이에 넣어줌

def open_account():
    print("새로운 계좌가 생성되었습니다")

def deposit(balance, money):        #입금
    print("입금이 완료되었습니다. 잔액은 {}원 입니다.".format(balance+money))
    return balance + money

def withdraw(balance, money):     #출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {}원 입니다.".format(balance - money))
        return balance - money
    else :
        print("출금이 완료되지 않았습니다. 잔액은 {}원 입니다.".format(balance))
        return balance 

def withdraw_night(balance, money):
    commision = 100
    return commision, balance - money - commision       #튜플 형식으로 리턴값을 2개 줄 수도 있음

open_account()      #새로운 계좌가 생성되었습니다

balance = 0;
balance = deposit(balance, 1000)
print(balance)      #입금이 완료되었습니다. 잔액은 1000원 입니다.

balance = withdraw(balance, 2000)        #출금이 완료되지 않았습니다. 잔액은 1000원 입니다.
balance = withdraw(balance, 500)        #출금이 완료되었습니다. 잔액은 500원 입니다. 

commision, balance = withdraw_night(balance, 200)
print(commision)    #100
print(balance)  #200

#기본값
def propile (name, age=17, main_lang="파이썬"):     #함수 선언 시 아규먼트 넣어줄 때부터 값을 할당함. 이후에 함수 호출할 때는 기본값이 아닌 값만 넣어줌
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}".format(name, age, main_lang))

propile("유재석")
propile("김태호")

#키워드값
def profile (name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석", main_lang= "파이썬", age = 16)     #함수 호출할 때 키워드값을 사용하면 굳이 선언 시에 넣었던 순서 안지키고 해도 됨
profile(age = 17, name="김태호", main_lang= "자바")

#가변인자

def profile(name, age, *language):      #아규먼트 앞에 *표 - 가변인자 
    print("이름: {0}\t나이: {1}\t".format(name, age), end = " ") #end = "" - 프린트한 다음에 줄바꿈 안해줌
    for lang in language:   #입력받은 가변인자 출력
        print(lang, end=" ")
    print()

profile("유재석", 17, "java", "python", "c++")
profile("김태호", 17, "c")
profile("조세호", 17)

# 지역변수와 전역변수

gun = 10

def checkpoint(soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))

print("전체 총: {0}".format(gun))     
checkpoint(2)    
print("남은 총: {0}".format(gun))

#local variable 'gun' referenced before assignment 라고 오류가 뜸.


gun = 10

def checkpoint(soldiers):
    gun = 20    #같은 이름의 변수라도 함수 밖에서 선언된 것과 안에서 선언된 것은 다름 
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))

print("전체 총: {0}".format(gun))     #10
checkpoint(2)     #18
print("남은 총: {0}".format(gun))     #10

gun = 10

def checkpoint(soldiers):
    global gun  #앞에 global을 붙여서 전역변수를 사용하겠다는 뜻 
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))

print("전체 총: {0}".format(gun))       #10
checkpoint(2)       #8
print("남은 총: {0}".format(gun))       #8

#퀴즈

def std_weight(height, gender):
    if gender == "M":
        return round(height * height * 22 / 10000, 2)
    else :
        return round(height * height * 21 / 10000, 2)

height = 175
gender = "M"
weight = std_weight(height, gender)

print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, weight))

#표준입출력
표준출력
#sep - 출력 시 개체 사이에 뭘 넣어서 분리해줄지

print("Python", "Java", "C++")      #Python Java C++
print("Python", "Java", "C++", sep = ",")       #Python,Java,C++

#end - 끝날 때 무슨 문자로 끝날지 정해주고, 다음줄을 이어서 출력(줄바꿈X) 
print("Python", "Java", "C++", sep = ",", end = "?")
print("무엇이 더 재밌을까요?")      #Python,Java,C++?무엇이 더 재밌을까요?

#표준출력, 표준에러
import sys
print("python", "java", file=sys.stdout)   #표준출력
print("python", "java", file=sys.stderr)    #표준에러

#ljust rjust - 문자열에서만 사용 가능. 정수 넣고 싶으면 정수부분 str로 둘러야함
score = {"수학": 10, "영어": 50, "코딩": 100}
for subject, score in score.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")   #왼쪽에서부터 8칸의 공간을 확보한 뒤 왼쪽부터 출력 / 오른쪽에서부터 4칸의 공간을 확보한 뒤 오른쪽부터 출력

'''출력예제
수학      :  10
영어      :  50
코딩      : 100
'''

#은행 대기순번표 zfill -  문자열에서만 사용 가능. 정수 넣고 싶으면 정수부분 str로 둘러야함
for num in range(1, 21):
    print("대기번호: " + str(num).zfill(3))     #3 크기의 공간을 확보한 다음에 값을 넣고, 값을 안 넣은 부분은 0으로 채움

#표준입력
answer = input("아무 값이나 입력하세요 : ") 
print("입력하신 값의 타입은 " + str(type(answer)) + "입니다.")        #사용자 입력을 통해서 입력을 받은 경우 항상 문자열로 인식됨

# 표준 출력 포맷 - 순서 {0:빈공간채우기 정렬방향 부호 확보할공간 콤마}
# 빈 자리는 빈공간으로 두고( ), 오른쪽 정렬을 하되(>), 총 10자리 공간을 확보(10)
print("{0: >10}".format(500))       #       500

#양수일 때는 +로, 음수일 때는 -로 표시
print("{0: >+10}".format(500))      #      +500
print("{0: >+10}".format(-500))     #      -500

#왼쪽 정렬하고, 빈칸을 _으로 채우고, 총 10자리 공간을 확보 
print("{0:_<10}".format(500))       #500_______

#3자리마다 콤마를 찍어주기
print("{0:,}".format(100000000))        #100,000,000

#3자리마다 콤마를 찍어주기, +- 부호도 붙임
print("{0:+,}".format(100000000))       #+100,000,000
print("{0:+,}".format(-100000000))      #-100,000,000

#3자리마다 콤마를 찍어주기, +- 부호도 붙임, 자릿수 확보, 빈 자리는 ^
print("{0:^<+30,}".format(100000000))   #-100,000,000^^^^^^^^^^^^^^^^^^

#소수점 출력
print("{0:f}".format(5/3))

#소수점 특정 자리 수까지 출력   #.nf - 소수점n+1자리에서 반올림해서 n번째 자리까지 표시
print("{0:.2f}".format(5/3))        #1.67

#파일 입출력
#파일에 쓰기
score_file = open("score.txt", "w", encoding = "utf8")      #파일 여는 함수 encoding = "utf8" - 한국어 잘 출력되라고 인코딩해주는거
print("수학: 0", file=score_file)       #score_file이라는 파일에다가 print함
print("영어: 50",file=score_file)
score_file.close()      #파일 닫는 함수

score_file = open("score.txt", "a", encoding = "utf8")  #a모드 - 이어쓰기
score_file.write("과학 : 80")       #이렇게 해도 파일에 쓸 수 있는데, 줄바꿈이 안됨 \n 넣어줘야함
score_file.write("\n코딩 : 100")
score_file.close()

#파일 읽기 - 전체 읽어옴
score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.read())
score_file.close()

#한 줄씩 불러오기
score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.readline())    #줄 별로 읽기. 한 줄 읽고 커서는 다음 줄로 이동함. (readlines 아님) 출력 - 수학: 0
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.readline(), end = "")    #수학: 0 
print(score_file.readline(), end = "")    #영어: 50
print(score_file.readline(), end = "")    #과학 : 80
print(score_file.readline(), end + "")    #코딩 : 100

score_file.close()

#파일에 몇 줄인지 모를 때 한 줄씩 불러오기
score_file = open("score.txt", "r", encoding = "utf8")
while True:
    line = score_file.readline()
    if not line:        #line이 없으면 
        break
    print(line, end="")
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
lines = score_file.readlines()      #전체 다 읽어오기
for line in lines:
    print(line, end = "")
score_file.close()

#파일 전체 한 글자씩 읽어오기
score_file = open("score.txt", "r", encoding = "utf8")
while True:
    line = score_file.readline()    #일단 한 줄씩 읽음
    if not line:        #다 읽어서 line이 없으면 break
        break
    for char in line:   #줄 안에서 한 글자씩 가져옴
        print(char)
score_file.close()


#피클 
#피클 만들기
import pickle
file = open("profile.pickle", "wb")     #피클로 만들 때는 바이너리 모드로 열어야 함(wb)
profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
print(file)
pickle.dump(profile, file) #profile에 있는 정보를 profile_file에 저장
file.close()

#피클 읽어오기
file = open("profile.pickle", "rb")
profile = pickle.load(file)     #profile_file에 있는 정보를 profile에 불러오기
print(file)
file.close()

#with
#with로 피클에서 데이터 읽어오기
import pickle
with open("profile.pickle", "rb") as file:      #profile.pickle 파일을 file에 rb모드로 열기
    print(pickle.load(file))        #pickle.load 함수를 통해 파일에 있는 데이터를 읽어올 수 있음

#with로 파일에다가 데이터 쓰기
with open("study.txt", "w", encoding = "utf8") as study_file:
    study_file.write("집에 가고 싶다")

#with로 파일의 데이터 읽기
with open("study.txt", "r", encoding = "utf8") as study_file:
    print(study_file.read())

#퀴즈

for i in range(1, 51):
    report_file = open("{0}주차.txt".format(i), "w", encoding = "utf8")
    report_file.write("- {0}주차 주간보고 - \n".format(i))
    report_file.write("부서 : \n")
    report_file.write("이름 : \n")
    report_file.write("업무 요약 : \n")
    report_file.close()

for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding = "utf8") as report_file:
        report_file.write("- {0} 주차 주간보고\n".format(i))
        report_file.write("부서 : \n")
        report_file.write("이름 : \n")
        report_file.write("업무 요약 : \n")

#클래스 - 붕어빵기계
class Unit: 
    def __init__(self, name, hp, damage):       #__init__ 생성자. 
        self.name = name        #멤버 변수 - class 안에서 정의된 변수. self.mame, self.damage, self.hp 등등...
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
    
marine1 = Unit("마린", 40, 5)       #self를 제외하고 init 함수에 정의된 아규먼트 개수와 동일한 수의 값을 던져줘야 함
marine2 = Unit("마린", 40 ,5)
tank = Unit("탱크", 150, 35)

#객체 - 클래스로부터 만들어지는 것들(마린, 탱크 등...)
#마린과 탱크는 유닛 클래스의 인스턴스

# 클래스 외부에서 멤버 변수를 확장할 수 있음
wraith = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith.name, wraith.damage))   #변수이름.멤버변수 로 멤버 변수에 접근 가능

wraith2 = Unit("빼앗은 레이스", 80, 5)  
wraith2.clocking = True     #유닛 클래스에 없는 멤버 변수도 유닛 외부에서 확장해서 넣을 수 있음 (cloaking은 유닛 클래스에 없는 멤버변수)

if wraith2.clocking == True:     #waruth.clocking이라고 하면 'Unit' object has no attribute 'clocking' 이렇게 오류남
    print("{0}은 현재 클로킹 상태입니다.".format(wraith2.name))
