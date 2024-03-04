import random

com_list = ['가위', '바위', '보']
win_num = 0
lose_num = 0
draw_num = 0

while True:
    player = input("가위, 바위, 보 중 하나를 선택하세요: ")
    if player in com_list:
        com_num = random.randint(0, 2)  # 각 반복에서 컴퓨터의 선택을 생성
        print("컴퓨터:", com_list[com_num], "사용자:", player)

        if player == com_list[com_num]:
            print("비겼습니다")
            draw_num += 1
        elif (player == '가위' and com_list[com_num] == '바위') or \
             (player == '바위' and com_list[com_num] == '보') or \
             (player == '보' and com_list[com_num] == '가위'):
            print("컴퓨터 승리")
            lose_num += 1
        else:
            print("사용자 승리")
            win_num += 1
        rpt = input("게임을 계속하시겠습니까? (y/n): ")
        if rpt != 'y':
            break
    else:
        print("올바른 입력이 아닙니다.")

print("게임 종료")
print("승리 횟수:", win_num)
print("패배 횟수:", lose_num)
print("무승부 횟수:", draw_num)

