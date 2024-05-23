#20191820 김형준
hap = 0
i = 1
for i in range(1,101):
    if i%3 == 0:
        continue
    hap=hap+i
print('합계는 {}입니다.'.format(hap))
