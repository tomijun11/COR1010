#20191820 김형준
s1 = [90,90,88]
s2 = [90,95,85,90,90]

def avg(L):
    total = 0
    for i in range(len(L)):
        total+=L[i]
    return int(total/len(L))

def grade(n):
    if n>=90: return 'A'
    elif n>=80: return 'B'
    elif n>=70: return 'C'
    else: return 'D'

s1.append(avg(s1))
s2.append(avg(s2))

s1.append(grade(s1[len(s1)-1]))
s2.append(grade(s2[len(s2)-1]))

print(s1)
print(s2)
