#20191820 김형준
time=int(input("초를 입력하시오:"))
hour = time//3600
minute = ((time%3600)//60)
sec = time%60
print("입력한 시간",time,"은",hour,"시간",minute,"분",sec,"초입니다.")
