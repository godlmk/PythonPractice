def show_str_information(s):
    counts = {}
    for word in s:
        counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(items)):
        word, count = items[i]
        print("{0:<6}{1:>3}".format(word, count))


def main():
    s = input("请输入一串字符：")
    show_str_information(s)


main()
