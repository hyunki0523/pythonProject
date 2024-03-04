import random

random_int = random.randint(1, 100)
cnt = 0

while True:
    print("1~100 의 숫자를 입력하세요")
    aws = int(input())
    if 0 < aws <101 :
        cnt += 1
        if aws == random_int:
            print(random_int, "정답입니다. 시도회수 : ",cnt,"회")

            while True:
                Rpt = str(input("다시 하겠습니까?(y/n)  "))
                if Rpt == 'n':
                        print("게임을 종료합니다.")
                        break

                elif Rpt == 'y':
                        random_int = random.randint(1, 100)
                        cnt = 0
                        break
                else :
                        print("y/n 으로 입력해주세요")
            break
        elif aws < random_int:
            print("UP!")

        else:
            print("Down!")
    else: print("유효한숫자를 입력하세요")