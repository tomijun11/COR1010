num = input('주민등록번호:')
vaild = 0 # 1이면 error



ret = ''
if not(len(num) == 14): # 길이 확인 (14자)
    vaild = 1
elif num[6] != '-': # 중간에 - 있는지 확인
    vaild = 1
else:
    for c in num[0:6]:
        if c not in '0123456789':
            vaild = 1
    for c in num[7:14]:
        if c not in '0123456789':
            vaild = 1
    if num[7] == '1' or num[7] == '3':
        ret = '[\'남 '+num[0:7]+'*'*7+'\']'
    elif num[7] == '2' or num[7] =='4':
        ret = '[\'여 '+num[0:7]+'*'*7+'\']'
    else:
        vaild = 1
if vaild == 1:
    print('다시 입력해주세요')
else:
    print(ret)
    
