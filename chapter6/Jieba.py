import jieba

print(jieba.lcut("中华人民共和国是一个伟大的国家"))
print(list(jieba.cut("中华人民共和国是一个伟大的国家", cut_all=True)))
