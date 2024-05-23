A, B, C = input("Enter three integers : ").split()
A = int(A)
B = int(B)
C = int(C)
Sum = A+B+C
avg = Sum/3
print()

# 1번
print("sum :",Sum)
print("average : %.2f" %(avg))
print()

# 2번
print("♥"*Sum)
print("★"*round(avg))
