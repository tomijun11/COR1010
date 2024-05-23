import keyword as k
plist = k.kwlist

breakflag = 0
vname = input('사용할 변수 이름은?')
for i in range(10):
    if breakflag == 0:
        if not(vname):
            breakflag=1
        elif vname in plist:
            print('예약어라서 사용할 수 없음!')
        elif ' ' in vname:
            print('공백 포함해서 사용할 수 없음!')
        elif vname[0].isnumeric() == True:
            print('숫자로 시작해서 사용할 수 없음!')
        elif ('!' in vname) or ('@' in vname) or ('#' in vname) or ('$' in vname) or\
             ('%' in vname) or ('^' in vname) or ('&' in vname) or ('*' in vname): 
            print('특수문자 포함해서 사용할 수 없음!')
        else:
            print('사용 가능 합니다!')
        if breakflag == 0:
            print('-'*25)
            vname = input('사용할 변수 이름은?')

print('종료합니다!')
