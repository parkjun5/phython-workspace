class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕 파타야 여행 야시장투어 50만원")

## 내부에서 모듈을 가져오는것과 외부에서 사용되는 것 차이을 구분해서 
## 코드를 작동시키는법
if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 문장을 직접 실행하러때문 실행되요")
    trip_to = ThailandPackage()
    trip_to.detail()

else:
    print("외부에서 Thailand 외부에서 모듈 호출")