""" 共同分担
小明和小红是一对龙凤胎。一天，他们的妈妈给了一张清单让他们去超市买东西。买完东西出来后小明和小红发现这些东西非常多可能需要两个人都提一个袋子才能带走
为了尽可能让双方提的袋子重量差不多，作为刚开始学习算法的小明和小红决定思考一下如何分配两个袋子里的商品使得他们之间的重量差最小 """

def sum(array):
    result = 0
    for i in array:
        result += i
    return result

def calculation(array, left, right):
    

products = input()
weight_list = products.split(' ')
array = [int(i) for i in weight_list]
array.






    