#20191820 김형준
# 1번 
print(int(123.456789), float(123.456789))
print()

# 2번
Num = 3.14
Num=str(Num)
print(Num,type(Num))
Num=int(float(Num))
print(Num,type(Num))
Num=float(Num)
print(Num,type(Num))
print()

# 3번
name = input("이름 : ")
stdid = input("학번 : ")
age = input("나이 : ")
print("당신의 이름은 "+name+"이며,학번은 "+stdid+"입니다.")
print()

# 4번
print("♥"*int(age))
