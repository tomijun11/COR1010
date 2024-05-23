
def check(pwd) :
    if len(pwd) < 8:
        print('error! 8 글자 이상이어야 함')
        return False
    if pwd.isalnum() == False:
        print('error! 영문자, 숫자로만 구성되어야 함')
        return False
    if pwd.isalpha() == True:
        print('error! 숫자도 포함되어야 함')
        return False
    if pwd.isnumeric() == True:
        print('error! 영문도 포함되어야 함')
        return False

    cnt = 0
    for c in pwd:
        if c in '0123456789':
            cnt+=1
    if cnt < 2:
        print('error! 최소한 2개의 숫자를 포함해야 함')
        return False
    
    return True

# main
for i in range(5):
    pwd = input('Enter password: ')

    if check(pwd) == True:
        print('Vaild password')
        break
    else:
        print('Invaild password')
