#20191820 김형준
print('*'*5,"if조건문으로 작성",'*'*5)
Month = int(input('월을 입력하세요: '))
if Month == 1:
    print("1월은 January입니다")
elif Month == 2:
    print("2월은 February입니다")
elif Month == 3:
    print("3월은 March입니다")
elif Month == 4:
    print("4월은 April입니다")
elif Month == 5:
    print("5월은 May입니다")
elif Month == 6:
    print("6월은 June입니다")
elif Month == 7:
    print("7월은 July입니다")
elif Month == 8:
    print("8월은 August입니다")
elif Month == 9:
    print("9월은 September입니다")
elif Month == 10:
    print("10월은 October입니다")
elif Month == 11:
    print("11월은 November입니다")
elif Month == 12:
    print("12월은 December입니다")
    
print('*'*5,"리스트로 작성",'*'*5)
Month = int(input('월을 입력하세요: '))
Mlist = ['January','February','March','April','May','June'\
'July','August','September','October','November','December']
print('{:d}월은 {}입니다'.format(Month,Mlist[Month-1]))
