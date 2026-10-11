import random

secret = random.randint(1, 100)
attempts = 0

print("=== 猜数字游戏 ===")
print("我已经想好了一个 1~100 之间的数字，来猜猜看！")

while True:
    try:
        guess = int(input("请输入你猜的数字: "))
    except ValueError:
        print("请输入有效的整数！")
        continue

    attempts += 1

    if guess < secret:
        print("太小了，再大一点！")
    elif guess > secret:
        print("太大了，再小一点！")
    else:
        print(f"恭喜你猜对了！答案就是 {secret}")
        print(f"你一共猜了 {attempts} 次")
        break
