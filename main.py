#-------------------------
#作者：@Jeffery Hu
#日期：10/02/25
#功能：猜数字游戏
#-------------------------

import random

def guess_num():
    #-------------------------
    #变量解释：
    #   count(次数统计),
    #   limit(随机数字上限),
    #   number(随机生成数字),
    #   guess(玩家猜测数字)
    #-------------------------
    
    print('欢迎来到猜数字游戏！')
    count = 0

    try:
        limit = int(input('请输入数字范围（0~N）：'))
    except:
        print('请输入正确的数字！')
        input('按任意键重新开始...')
        guess_num()

    number = random.randint(0,limit)
    print('现在游戏开始！')

    while True:
        try:
            print('-'*30)
            guess = int(input('请输入你的猜测：'))
            count += 1
        except:
            print('请输入正确的数字！')
            continue
        if guess == number:
            print('恭喜你，猜中了！')
            break
        elif guess < number:
            print('猜小了，或许大胆一些比较好！')
        else:
            print('猜大了，或许谨慎一些比较好！')

    print('-'*30)
    print(f'游戏结束,本轮猜数次数为{count}次！')
    input('按任意键退出...')

guess_num()

            
