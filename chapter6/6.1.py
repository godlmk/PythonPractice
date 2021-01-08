from random import randint


def key_word():
    keyword = ''
    for i in range(8):
        u = randint(0, 61)
        if u > 9:
            if u < 36:
                keyword += chr(u + 55)
            else:
                keyword += chr(u + 61)
        else:
            keyword += str(u)
    return keyword


def main():
    print(key_word())


main()
