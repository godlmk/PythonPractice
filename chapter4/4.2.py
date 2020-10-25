word = input("请输入一段字符：\n")
num = 0
whitespace = 0
chi = 0
alpha = 0
other = 0
for s in word:
    if '0' <= s <= '9':
        num += 1
    elif u'\u4e00' <= s <= u'\u9fa5':
        chi += 1
    elif s == " ":
        whitespace += 1
    elif s.isalpha():
        alpha += 1
    else:
        other += 1
print("你输入的字符串有{}个空格，{}个英文，{}个中文，{}个数字，{}个其他字符".format(whitespace, alpha, chi, num, other))