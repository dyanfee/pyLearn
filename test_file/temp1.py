"""--- 第一个小游戏 ---"""
temp = input("不妨猜一下老王现在心里想的数字:")

guess = int(temp)

while guess != 8:

    temp = input("哎呀,猜错了,请重新输入吧:")

    guess = int(temp)

    string = ""

    print(string)
