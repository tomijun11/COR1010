#20191820 김형준
medals= [ ['Austria',0,2,1], ['Canada',4,8,5], ['China',5,0,1],
 ['France',0,4,5], [ 'Germany',1,1,2], ['Japan',1,1,0],
 ['Korea',5,3,1], ['Norway',4,4,7], ['Russia',4,6,4],
 ['Viet Nam',1,1,5] ]

for v in medals:
    v.append(v[1]+v[2]+v[3])
for v in medals:
    print(v)
print()
print(medals)

    
