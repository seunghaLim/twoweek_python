#변수

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >=3 #나이가 3보다 이상이면 adult(true)

print("우리집 " + animal + "의 이름은" + name + "예요")
print(name + "는 " + str(age) + "살이며, 산책을 아주 좋아해요")     #정수형을 +가 포함된 print문에서 출력하고 싶다면 str 붙여야 함(정수형 -> 문자열)
print(name + "는 어른일까요? " + str(is_adult))     #bool형도 str 붙여줌


#print(age)  +가 없는 경우에는 그냥 변수만 print에 넣어줌
#print(name, "는 ", age, "살이며, 산책을 아주 좋아해요")  str 없이 ,를 사용해서 출력 가능 ,가 들어가면 무조건 띄어쓰기



#주석
#으로 한줄 주석 가능
'''
여러줄
주석 가능
'''

#변수 활용 퀴즈

station = "사당"
print(station + " 행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + " 행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station, "행 열차가 들어오고 있습니다.")



#연산자
print(2**3)     #2^3
print(10%3)     #나머지 1
print(6/3)  #2.0
print(10//3)    #3 

print(10 >= 3)  #False

print(3 == 3)    #True
print(4 == 2)   #False
print( 3+4 == 7)    #True

print(not(1 != 3))  #False

print((3>0) and (3<5))  #True
print((3>0) & (3<5))  #True

print((3>0) or (3>5))  # True
print((3>0) | (3>5))  #True

