#20191820 김형준
students = [ [90,90,88], [100,92,90], [80,90,90], [85,80,90] ]

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

print('** 리스트 변수 출력')
print(students)
for i in range(len(students)):
    List = students[i]
    List.append(avg(List))
print('** 반복문(평균계산함수 호출) 실행 후')
print(students)
for i in range(len(students)):
    List = students[i]
    List.append(grade(List[-1]))
print('** 반복문(Grade계산함수 호출) 실행 후')
print(students)
