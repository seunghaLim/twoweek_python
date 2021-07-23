class VietnamPackage:
    def detail(self):
        print("[베트남 패키지 3박 5일] 다낭 효도 여행 60만원")

if __name__ == "__main__":      #vietnam 파일 안에서 모듈을 직접 실행했을 때 출력됨
    print("Vietnam 모듈 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    trip_to = VietnamPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")    #vietnam 파일 밖에서 모듈을 실행했을 때 출력됨