#20191820 김형준
# 1번 문제
str1 = "Computer 4"; str2 = "Science#5"
s1 = str1[0:len(str1)-2]
n1 = int(str1[len(str1)-1])
s2 = str2[0:len(str2)-2]
n2 = int(str2[len(str2)-1])
print(s1*n1)
print(s2*n2)

print() # 문제 구분용

# 2번 문제
s1 = "Sogang University"
s2 = s1[0:6]
s3 = s1[7:len(s1)]
s4 = s1[5:-len(s1)-1:-1]
print("s1은",s1)
print("s2는",s2)
print("s3은",s3)
print("s4는",s4)
