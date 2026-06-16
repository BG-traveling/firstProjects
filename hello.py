from datetime import datetime

print('hello github!')
# git repository 생성

now = datetime.now()

while True:
    try:
        user_chat = int(input('(1)현재시간, (2)제작자, (3)종료\n'))
        if user_chat == 1:
            print(f'현재 시각 : {now.strftime("%Y-%m-%d, %H:%M:%S")}')
            continue
        elif user_chat == 2:
            print('제작자: 김동현')
            continue
        elif user_chat == 3:
            print("종료하겠습니다!")
            break
        else:
            print('1 ~ 3 번 중에 입력해주세요.')
    except:
        print('잘못된 입력입니다.')