##직육면체의 부피와 겉넓이 구하는 계산기##
def check(string):
    while True:
        try:
            f = float(input(string + "의 길이(cm)는?: "))

            if f < 0:
                print("마이너스 부호는 입력할 수 없습니다.")
                sp()
            elif f == 0:
                print("정수 0은 입력할 수 없습니다.")
                sp()
            else:
                sp()
                if f == int(f):
                    f = int(f)
                return f
        except:
            print("수 이외의 문자등은 입력할 수 없습니다.")
            sp()

def sp():
    print()

print("직육면체의 부피와 겉넓이 계산기")
input("[계산을 시작하려면 Enter를 누르세요.]")
sp()
sp()
x = check("가로")
y = check("세로")
z = check("높이")

w = x * y * z

s_1 = x * y * 2
s_2 = y * z * 2
s_3 = z * x * 2
s = s_1 + s_2 + s_3

sp()
sp()
print("직육면체의 부피는 " + str(w) + "cm³ 입니다.")
print("직육면체의 겉넓이는 " + str(s) + "cm² 입니다.")