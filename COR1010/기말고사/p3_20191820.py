s1 = input('입력하세요\n')

for c in s1:
    if c.isalnum() == False:
        s1 = s1.replace(c,' ')

s1=s1.split()
sdict = {}
for c in s1:
    c = c.lower()
    if sdict.get(c,-1) == -1:
        sdict[c] = 1
    else:
        sdict[c] +=1
print('** 단어별 빈도수')
for k, v in sdict.items():
    print("{:14s}{}".format(k,v))
print()

maxfreq = max(sdict.values())

cnt=0
for k, v in sdict.items():
    if v == maxfreq:
        cnt +=1

cur=0
print('** 최다빈도단어')
for k, v in sdict.items():
    if v == maxfreq:
        if cur == cnt-1:
            print('{}'.format(k),end='')
        else:
            print('{}'.format(k),end=', ')
        cur+=1
