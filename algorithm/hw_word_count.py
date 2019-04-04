# 统计词频

words = []

#定义方法统计词频
def find_word_count(words):
    word_count = {}
    for word in words:
        #判断key是否已经存在
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

#打开文件
with open('./article.txt', 'r') as f:
    #返回一个列表, 一行为一个元素
    lines = f.readlines()
    for line in lines:
        line = line.replace(',',' ')
        line = line.replace('.',' ')
        line = line.replace('?',' ')
        line = line.replace('!',' ')
        line = line.replace('-',' ')
        line = line.replace('”',' ')
        line = line.replace('“',' ')
        line = line.replace("'",' ')
        line = line.replace('\n',' ')
        line = line.replace(':',' ')

        for word in line.split(' '):
            if word:
                words.append(word)

print(len(words))
word_set = set(words)
print(len(word_set))
print(find_word_count(words))