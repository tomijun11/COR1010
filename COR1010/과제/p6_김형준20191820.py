# 20191820 김형준
import keyword as k
klist = k.kwlist

vname = input("사용할 변수 이름??")
if not(vname): # 입력값 없음 처리
    print("이름을 입력하세요!")
elif vname in klist: # 4번조건 
    print("사용할 수 없음!")
elif vname[0:1].isnumeric(): # 3번조건
    print("사용할 수 없음!")
elif ' ' in vname: # 2번조건
    print("사용할 수 없음!")
# 1번조건 -----
elif ('!' in vname) or ('@' in vname) or ('#' in vname) or ('$' in vname) \
or ('%' in vname) or ('&' in vname) or  ('*' in vname): 
    print("사용할 수 없음!")
# ------------
else:
    print("사용가능!")

    
    
