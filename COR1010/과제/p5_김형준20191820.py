#20191820 김형준
n = int(input("Enter the number : "))

if n==0:
    print("{} is zero".format(n))
elif n>0:
    print("{} is a positive number".format(n))
else:
    print("{} is a negative number".format(n))

if n%2==0:
    print("{} is an even number".format(n))
else:
    print("{} is an odd number".format(n))
