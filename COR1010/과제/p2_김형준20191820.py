#20191820 김형준
A = int(input("아메리카노 판매 개수? "))
B = int(input("카페라떼 판매 개수? "))
C = int(input("카푸치노 판매 개수? "))
Cdc = float(input("카푸치노 할인률(%)? "))
print("총 매출은",round(2000*A+3000*B+3500*C*(1-Cdc/100)),"원 입니다")
