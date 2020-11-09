class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
       ## __str이 toString s느낌? 
    def __str__(self):
        return self.msg


try:
    print("한자리 숫자 나누기 전용 계산기")
    num1 =int(input("첫번째"))
    num2 =int(input("두번째"))
    if num1>=10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1,num2))
    print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))

except BigNumberError as err:
    print("10이상의 수입력gktuTtmqslek.")
    print(err)
## 오류가 발생하여도 무조건 실행하는 구문
finally:
   
    print("이용하셔서 감사합니다.")