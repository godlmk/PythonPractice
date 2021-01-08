fo = open("D:/PythonProject/chapter7/price2016.csv", 'r', encoding="utf-8")
ls = []
for line in fo:
    line.replace("\n", "")
    ls.append(line.split(","))
print(ls)
fo.close()