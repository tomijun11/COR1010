fruit = {'배':[2,1000], '자몽' : [1,2000], '메론' : [1,8000], '감' : [6,800]}

name = input('먹고 싶은 과일은? : ')

if name not in fruit:
    print(name,' 준비 되어 있지 않습니다')
else:
    print(name,'맛있게 드세요')
    fruit[name][0] -= 1

print()
mlist = fruit.values()
val = 0
for i in mlist:
    if i[0] < 5:
        val  += i[1]*(5-i[0])

msg = ' 각 과일 당 최소 5개는 되도록 구입합니다\n 구입에 필요한 총 금액은 :'
print(msg,val,'원 입니다')
