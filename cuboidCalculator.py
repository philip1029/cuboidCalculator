##직육면체의 부피와 겉넓이 구하는 계산기##
def miner(함수):
    if 함수 != abs(함수):
        sp()
        print("마이너스 부호는 입력할 수 없습니다.")
        quit()
    if 함수 == float(0):
        sp()
        print("숫자 0은 입력할 수 없습니다.")
        quit()
def sp():
    print()
def real(변수, 성질):
    if 변수 == int(변수):
        if 성질 == 1:
            print("직육면체의 부피는  %fcm³ 입니다." %w)
        else:
            print("직육면체의 겉넓이는 %fcm² 입니다." %s)
    else:
        if 성질 == 1:
            print("직육면체의 부피는  %scm³ 입니다." %w)
        else:
            print("직육면체의 겉넓이는 %scm² 입니다." %s)
sp()
print("직육면체의 부피와 겉넓이 계산기")
input("[계산을 시작하려면 Enter를 누르세요.]")
sp()
sp()
x = float(input("가로의 길이(cm)는?: "))
miner(x)
sp()
y = float(input("세로의 길이(cm)는?: "))
miner(y)
sp()
z = float(input("높이의 길이(cm)는?: "))
miner(z)
sp()
w = x * y * z
s_1 = x * y * 2
s_2 = y * z * 2
s_3 = z * x * 2
s = s_1 + s_2 + s_3
sp()
print("======================================")
sp()
real(w, 1)
real(s, 2)
