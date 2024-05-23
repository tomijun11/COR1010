# 20191820 김형준
import turtle as t
import math

# 펜로즈 타일링을 그리는 코드
def CSMakeTile(Level) : # Level = 깊이
	Size = 1
	TileArr =[["K",[math.cos(math.radians(36)),math.sin(math.radians(36))],[0,0],[1,0]],["K",[math.cos(math.radians(36)),-math.sin(math.radians(36))],[0,0],[1,0]]]
	b = 1-0.25/(math.sin(math.radians(54))**2)
	a = 0.5/(math.cos(math.radians(36)))

	for i in range(Level+1):
		Size = Size*b
		TempArr = []
		for k in range(len(TileArr)):
			v = TileArr[k]
			if v[0] == "K":
				XLoc = v[2][0]
				YLoc = v[2][1]
				Pa = [(v[3][0]-XLoc)*a+XLoc,(v[3][1]-YLoc)*a+YLoc]
				TempArr.append(["K",[v[3][0],v[3][1]],[v[1][0],v[1][1]],[Pa[0],Pa[1]]])
				TempArr.append(["D",[Pa[0],Pa[1]],[v[1][0],v[1][1]],[v[2][0],v[2][1]]])
			else: # v[0] == "D"
				XLoc = v[2][0]
				YLoc = v[2][1]
				Pb = [(v[3][0]-XLoc)*b+XLoc,(v[3][1]-YLoc)*b+YLoc]
				Pc = [(v[1][0]-XLoc)*b+XLoc,(v[1][1]-YLoc)*b+YLoc]
				TempArr.append(["K",[v[1][0],v[1][1]],[Pb[0],Pb[1]],[Pc[0],Pc[1]]])
				TempArr.append(["D",[Pb[0],Pb[1]],[v[3][0],v[3][1]],[v[1][0],v[1][1]]])
				TempArr.append(["D",[Pc[0],Pc[1]],[Pb[0],Pb[1]],[v[2][0],v[2][1]]])
		TileArr = TempArr
		
	return TileArr

def ConvertRA(NX,NY):
	PR = math.sqrt(NX**2+NY**2)
	if NX>=0 and NY>=0:
		PA = abs(math.atan2(NY,NX))
	elif NX<0 and NY>=0:
		PA = math.pi - abs(math.atan2(NY,NX))
	elif NX<0 and NY<0:
		PA = math.pi + abs(math.atan2(NY,NX))
	elif NX>=0 and NY<0:
		PA = 2*math.pi - abs(math.atan2(NY,NX))
	return PR, PA

def ConvertXY(PR,PA):
	NX = PR*math.cos(PA)
	NY = PR*math.sin(PA)
	return NX, NY

def RotateLoc(X,Y,Size,index):
	NR, NA = ConvertRA(X*Size,Y*Size)
	NX, NY = ConvertXY(NR,NA+math.radians(72*index+54))
	return NX, NY

def DrawTriangle(Data,Size): # 5각 대칭으로 그림
	for i in range(5):
		if Data[0] == "K": # Kite
			t.fillcolor('#4E9A06')
			t.goto(RotateLoc(Data[1][0],Data[1][1],Size,i))
			t.pendown()
			t.begin_fill()
			t.goto(RotateLoc(Data[2][0],Data[2][1],Size,i))
			t.goto(RotateLoc(Data[3][0],Data[3][1],Size,i))
			t.end_fill()
			t.penup()
		else: # Dart
			t.fillcolor('#739FD0')
			t.goto(RotateLoc(Data[3][0],Data[3][1],Size,i))
			t.pendown()
			t.begin_fill()
			t.goto(RotateLoc(Data[1][0],Data[1][1],Size,i))
			t.goto(RotateLoc(Data[2][0],Data[2][1],Size,i))
			t.end_fill()
			t.penup()

# main code start
t.penup()
t.speed(0)
t.pensize(2)
TileArr = CSMakeTile(3)

for T in TileArr:
	 DrawTriangle(T,300)
