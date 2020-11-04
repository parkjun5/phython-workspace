
#함수는 def로 시작 그휴ㅜ ()와 :fh 마무리
def open_account():
    print("계좌 생ㄱ성!")

open_account()

def deposit( balance, money):
    print("입금이 완료되었스빈다. {0}잔액 확인".format(balance+money))
    return balance + money

def withdraw(balance, money):
    if money > balance :
        print("잔액이 부족합니다.")
        return balance
    else: 
        print("출금이 완료되었습니다. 잔액은 {0}입니다".format(balance-money))
        return balance -money

def withdraw_nigth(balance,money):
    commission = 100 # 수수료 100원

    return commission, balance-money-commission


balance =0
balance =deposit(balance, 5000+555)
# balance= withdraw(balance, 2000)
commission, balance = withdraw_nigth(balance,500)
print("수수료는 {0}원이고 잔액은 {1}원입니다.".format(commission,balance))
print(balance)