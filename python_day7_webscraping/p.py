import re

p = re.compile("ca.e") #정규식을 컴파일했고 패턴값을 받아왔음


def print_match(m):
    if m: 
        print("m.group: {} ".format(m.group()))    #매치할 경우 일치하는 문자열 반환 care
        print("m.string: {} ".format(m.string))     #매치할 경우 입력받은 문자열 반환. 변수라서 괄호 없어야 됨 careless
        print("m.start: {}".format(m.start()))      #매치할 경우 일치하는 문자열의 시작 인덱스 반환 0
        print("m.end: {}".format(m.end()))         #매치할 경우 일치하는 문자열의 끝(+1) 인덱스 반환 4
        print("m.span: {}".format(m.span()))       #매치할 경우 일치하는 문자열의 시작과 끝 인덱스 반환 (0, 4)
    else:
        print("매칭되지 않음")

m = p.match("good care") #매칭되지 않는다고 뜸.  match함수는 주어진 문자열의 처음부터 일치하는지 확인하기 때문에 이렇게 출력됨
print(m.group(m))

m = p.search("good care")    #care이라고 뜸. search : 주어진 문자열 중에 일치하는게 있는지 확인하는 함수. 일치하면 정규식 형식에 맞춰서 출력됨
print_match(m)

lst = p.findall("care cafe")
print(lst)