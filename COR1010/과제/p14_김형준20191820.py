#20191820 김형준
print('정수를 입력하세요. 0입력시 종료!')
count = 0; total = 0;

num = int(input())
while num != 0:
    count+=1; total+=num
    num = int(input())
if count != 0: # 처음부터 0 입력시 예외처리
    print('평균 %.1f' %(total/count))
