import random

def guess_number():
    number_to_guess = random.randint(1, 230)
    attempts = 0

    print("欢迎来到猜数字游戏！")
    print("请猜一个1到230之间的数字")
    print("输入 'q' 随时退出游戏")

    while True:
        try:
            user_input = input("请输入你猜的数字: ").lower()
            
            if user_input == 'q':
                print(f"游戏结束！正确答案是 {number_to_guess}")
                break
                
            guess = int(user_input)
            
            if guess < 1 or guess > 230:
                print("请输入1到230之间的数字！")
                continue
                
            attempts += 1

            if guess < number_to_guess:
                print("太小了！再试一次！")
            elif guess > number_to_guess:
                print("太大了！再试一次！")
            else:
                print(f"恭喜你！用了 {attempts} 次就猜对了！")
                break
                
        except ValueError:
            print("请输入有效的数字或 'q' 退出游戏！")

if __name__ == '__main__':
    guess_number()
