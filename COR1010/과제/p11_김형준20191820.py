#20191820 김형준

menu = {'쥬스':4000,'모카라떼':3500,'아메리카노':2000,'카페라떼':3000}
print(menu) #출력1

mlist = list(menu)
print("모든 메뉴 ",mlist) #출력2

#출력3
name = input("원하는 음료는? ")
if name in menu:
    print('**',name,"메뉴에 있음!")
else:
    print('**',name,"메뉴에 없음!")

menu['카푸치노']=3000
del menu['모카라떼']
menu['카페라떼']=3500
print('\n',menu) #출력4


    

