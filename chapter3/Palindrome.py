num = input("请输入五个数字：")
ifPalindrome = True
if len(num) == 5:
    for i in range(0, 1):
        if num[i] != num[4 - i]:
            ifPalindrome = False
    if ifPalindrome:
        print("该数字是回文")
    else:
        print("该数字不是回文")
else:
    print("输入数字非法")
