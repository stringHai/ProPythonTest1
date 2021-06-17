# ！
# encoding: utf-8
'''
@author: String
@softwore: pycharm
@file: 
@desc:
'''


sales = [
    ["雅诗兰黛", "OLAY", "相宜本草", "Keith"],
    [8731, 4209, 10239, 422],
    [1099, 675, 516, 1349]
]

# print(sales[0],sales[1],sales[2])


list_sale = []
dict_sale = {}

def get_key(dict,value):
    for (k,v) in dict.items():
        # print(k,v)
        # print(type(v))
        if v == value:
            # print(k)
            return k


for (a,b) in zip(sales[1],sales[2]):
    # print(a,"*",b)
    sum_sale = a * b
    list_sale.append(sum_sale)


for (name,sum_sale) in zip(sales[0],list_sale):
    print(name,"销售总额为：",sum_sale)
    dict_sale [name] = sum_sale
    max_sales = max(list_sale)

max_name = get_key(dict_sale,max_sales)

print("---------------------------------------------")
print("销售最大额是：",max_name,max_sales)




# print("销售总额最高为：", max(list_sale))






