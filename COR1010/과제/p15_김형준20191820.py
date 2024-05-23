#20191820 김형준
text = input('입력하세요\n')

print('** 특수문자를 공백으로 바꾼 새 문자열')
ntext = ''
for c in text:
    if c in '~!@#$%^&*-_+=(){}[]:;?.,<>':
        c = ' '
    ntext+=c
print(ntext)
print('** 단어별 빈도수')
nlist = ntext.split()

ndict = {}
for v in nlist:
    if v not in ndict:
        ndict[v] = 1
    else:
        ndict[v]+=1

for k, v in ndict.items():
    print('{:10}{:3}'.format(k,v))
