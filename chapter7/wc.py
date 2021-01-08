import jieba
import wordcloud

'''这个函数把传入的列表并排除长度为1的文字'''


def get_text(words):
    conuts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            conuts[word] = conuts.get(word, 0) + 1
    return conuts


'''打开一个文件，可以用绝对路径。'''
f = open("D:/Text Files/红楼梦.txt", "r", encoding="utf-8")
t = f.read()
f.close()
'''通过jieba库进行分词，'''
ls = get_text(jieba.lcut(t))
'''用join函数对每个ls中的元素用空格分割'''
txt = " ".join(ls)
'''调用jieba库进行处理'''
w = wordcloud.WordCloud(width=2000, height=1600, background_color="white", font_path="msyh.ttc", )
w.generate(txt)
'''输出到指定路径'''
w.to_file("D:/Picture/红楼梦wc.jpg")
