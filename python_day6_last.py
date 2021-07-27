#에러 발생시키기
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("첫 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("잘못된 값을 입력하셨습니다. 한 자리 숫자만 입력하세요")      #두 자리 이상 숫자를 입력하거나 '삼'과 같이 문자를 입력하면 실행됨

#사용자 정의 예외처리

class BigNumberError(Exception):
    pass

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("첫 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("잘못된 값을 입력하셨습니다. 한 자리 숫자만 입력하세요")     
except BigNumberError:
    print("두 자리 이상의 값을 입력하셨습니다. 한 자리 숫자만 입력하세요")  #두 자리 이상의 숫자를 입력했을 때 실행됨


#사용자가 어떤 값을 입력했느냐에 따라서 메시지를 내보낼 수도 있음
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("첫 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("잘못된 값을 입력하셨습니다. 한 자리 숫자만 입력하세요")     
except BigNumberError as err:
    print("두 자리 이상의 값을 입력하셨습니다. 한 자리 숫자만 입력하세요")  #두 자리 이상의 숫자를 입력했을 때 실행됨
    print(err)  #10 5 입력했을 때 두 자리 이상의 값을 입력하셨습니다. 한 자리 숫자만 입력하세요\n 입력값 : 10, 5 이라고 출력


#finally - try 문에서 오류가 발생하건 발생하지 않건 반드시 실행되는 부분. 정의하지 않은 에러 구문에서도 실행할 수 있음
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg


try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("첫 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print("잘못된 값을 입력하셨습니다. 한 자리 숫자만 입력하세요")     
except BigNumberError as err:
    print("두 자리 이상의 값을 입력하셨습니다. 한 자리 숫자만 입력하세요")  
    print(err)  
finally:
    print("계산기를 이용해주셔서 감사합니다")

#퀴즈
class SoldOutError(Exception):
    pass


chicken = 10
waiting = 1
while True:
    try: 
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까? "))
        if order < 1:
            raise ValueError
        if order > chicken:
            print("재료가 부족합니다")
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다". format(waiting, chicken))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError

    except ValueError:
        print("잘못된 값을 입력하셨습니다")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다")
        break

#모듈 
import theater_module
theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_soldier(5)

import theater_module as mv #theater_module을 일일이 타이핑하지 않고 as 별명 으로 설정하면 별명으로 모듈을 사용할 수 있음
mv.price_soldier(5)
mv.price(5)
mv.price_morning(5)

from theater_module import *    #theater_module을 일일이 타이핑하지 않고 바로 모듈 안에 있는 함수를 호출해서 사용할 수 있음
price(5)
price_morning(5)
price_soldier(5)

from theater_module import price, price_morning    #theater_module 모듈의 rice, price_morning 함수만 사용 가능
price(5)
price_morning(5)
#price_soldier(5)   사용할 수 없음

from theater_module import price_soldier as price #theater_module 모듈의 price_soldier 함수만 사용할 건데 price라는 별명을 붙여서 쓸 거임
price(5)        #모듈에 있는 price 함수가 아니라 price_soldier 함수가 호출됨

#패키지 travel 패키지 안에 있는 thailand 모듈 안의 클래스
import travel.thailand  #import 쓸 때 옆에 모듈이나 패키지 단위만 가능. import travel.thailand.ThailandPackage 는 안됨
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()    

from travel.thailand import ThailandPackage #from import 구문에서는 모듈이나 패키지, 클래스 모두 쓸 수 있음
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

#__all__ (*)
from travel import *     #travel 패키지 안에 있는 모든 걸 import하겠다는 소리
trip_to = vietnam.VietnamPackage()
trip_to.detail()    #NameError: name 'vietnam' is not defined 이라고 에러가 뜸. 개발자가 travel 패키지 안에서 공개 범위를 설정해줘야 함

#__init__파일에서 __all__ = [] 리스트 안에 공개할 모듈을 넣어줌. 넣어준 모듈만 공개 가능

#패키지와 모듈이 어느 위치에 있는지 알아보는 함수 inspect.getfile
import inspect
import random
from travel import *
print(inspect.getfile(random))      #C:\Python\Python39\lib\random.py
print(inspect.getfile(vietnam))     #C:\Users\LSH\source\Python\travel\vietnam.py
#C:\Python\Python39\lib 이 위치에다가 패키지를 만들면 따로 패키지를 워크스페이스에 만들지 않아도 파이썬 내장함수 호출하는 것처럼 호출할 수 있음



#pip install pipy 사이트에서 패키지를 가져와서 설치한 다음에 사용할 수 있음
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

#pip list
#pip show 이름
#pip install --upgrade

#내장함수 - 내장되어 있기 때문에 import 없이 그냥 사용할 수 있음
input() : 사용자 입력을 받는 함수

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표현
print(dir())        #['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
import random       #['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'random']
print(dir())

print(dir(random))      #random 모듈 안에서 쓸 수 있는 함수가 나옴

lst = [1, 2, 3]
print(dir(lst))     #리스트에서 사용할 수 있는 내용들이 나옴

name = "jim"
print(dir(name))        #name 변수에서 사용할 수 있는 내용들이 나옴

외장 함수 - 직접 import를 해서 써야 되는 함수

#glob : 경로 내의 폴더 / 파일 목록 조회

import glob
print(glob.glob("*.py"))    #확장자가 py인 모든 파일 조회. 해당 워크스페이스에서 py로 끝나는 모든 파일을 조회할 수 있음

#os : 운영체제에서 제공하는 기본 기능
#현재 디렉토리 위치 표시
import os
print(os.getcwd())

folder = "sample_dir"

if os.path.exists(folder):      #해당 이름의 폴더가 존재하는지 검사
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)   #폴더 삭제
    print(folder, "폴더를 삭제하였습니다")
else:
    os.makedirs(folder)     #폴더 생성
    print(folder, "폴더를 생성하였습니다")

#time : 시간 관련 함수 호출
import time
print(time.localtime())     #time.struct_time(tm_year=2021, tm_mon=7, tm_mday=24, tm_hour=2, tm_min=12, tm_sec=8, tm_wday=5, tm_yday=205, tm_isdst=0)
print(time.strftime("%Y-%m-%d %H:%M:%S")) # 2021-07-24 02:14:10

import datetime
print("오늘 날짜는", datetime.date.today())     #오늘 날짜는 2021-07-24

#timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은", today + td) #오늘 날짜의 100일뒤 날짜 출력

#퀴즈 10
import byme
byme.sign()