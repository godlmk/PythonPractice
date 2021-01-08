fname = input()
fo = open(fname, "r")
for line in fo.readlines():
    print(line)
fo.close()