def gPrint(score):
    if score>=90: print('A')
    elif score >=80: print('B')
    elif score >=70: print('C')
    else: print('D')

student=[90,89,95]
for score in student:
    gPrint(score)
