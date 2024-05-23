#20191820 김형준
menu = {'쥬스':4000,'모카라떼':3500,'아메리카노':2000,'카페라떼':3000}

print('* 모든 메뉴:')
for k in menu.keys():
    print(k,end=' ')
print('\n')

print('* 메뉴별 가격:')
for k, v in menu.items():
    print('{} {}원'.format(k,v))
    
