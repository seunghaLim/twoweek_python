#정규식

import re
# 네 자리 문자로 구성된 암호
# ca?e 물음표 안에는 아무거나 들어올 수 있음
# caae, cabe 등 들어올 수 있는 경우의 수 모두 검사

p = re.compile("ca.e") #정규식을 컴파일했고 패턴값을 받아왔음

# . : 하나의 문자를 의미 (하나의 문자 단위의 와일드 카드와 비슷)
# ^ : 문자열의 시작 ^de -> desk, destination과 같은 de로 시작하는 단어들과 모두 매칭
# $ : se로 끝나는 모든 문자열 se$ -> base, case....

m = p.match("caffe") #비교하려는 값과 패턴이 매칭되는지 비교
print(m.group())    #case 출력. 패턴값과 비교했고 매칭이 되어서 출력됨 매치 안되면 에러가 발생 매치 되면 비교값 출력

#if문을 사용해도 비교 가능. 이렇게 하면 매칭되지 않았을 경우에 오류가 안나고 출력문이 출력됨
if m: 
    print(m.group())
else:
    print("매칭되지 않음")

#함수로 만듦
def print_match(m):
    if m: 
        print("m.group: {} ".format(m.group()))    #매치할 경우 일치하는 문자열 반환 care
        print("m.string: {} ".format(m.string))     #매치할 경우 입력받은 문자열 반환. 변수라서 괄호 없어야 됨 careless
        print("m.start: {}".format(m.start()))      #매치할 경우 일치하는 문자열의 시작 인덱스 반환 0
        print("m.end: {}".format(m.end()))         #매치할 경우 일치하는 문자열의 끝(+1) 인덱스 반환 4
        print("m.span: {}".format(m.span()))       #매치할 경우 일치하는 문자열의 시작과 끝 인덱스 반환 (0, 4)
    else:
        print("매칭되지 않음")

m = p.match("good") #매칭되지 않는다고 뜸.  match함수는 주어진 문자열의 처음부터 일치하는지 확인하기 때문에 이렇게 출력됨
print_match(m)

m = p.search("good care")    #care이라고 뜸. search : 주어진 문자열 중에 일치하는게 있는지 확인하는 함수. 일치하면 정규식 형식에 맞춰서 출력됨
print_match(m)

lst = p.findall("care cafe")
print(lst)

# 1. 원하는 형태의 정규식을 re.compile 함수에 넣어서 정규식 패턴을 받음
# p = re.compile("정규식 형태")
# 2.  match 함수를 사용해서 비교할 문자열과 정규식 패턴이 매치하는지 안하는지 결과를 변수에 받음
# m = p.match("비교할 문자열")
# or search 함수를 사용해서 비교할 문자열 안에 정규식 패턴이 있는지 없는기 결과를 변수에 넣음
# m = search("비교할 문자열")
# 3. 다양한 함수를 사용해서 m과 p가 매치하는지 안하는지를 출력
# +findall 함수로 일치하는 모든 것을 리스트 형태로 반환 가능함
# lst = p.findall("비교할 문자열")

