# 1、创建一个空列表，命名为names，往里面添加old_driver,rain,jack,shanshan,peiqi,black_girl元素
names = []
names = ["old_driver", "rain", "jack", "shanshan", "peiqi", "black_girl"]
# print(names)

# 2、往names列表里的black_girl前面插入一个alex
names.insert(-1, "alex")
# print(names)

# 3、把shanshan的名字改成中文，姗姗
names[3] = '姗姗'
# print(names)

# 4、往names列表里rain的后面插入一个子列表，[oldboy, oldgirl]
names.insert(2, ['oldboy', 'oldgirl'])
# print(names)

# 5、返回peiqi的索引值
peiqi_index = names.index("peiqi")
# print(peiqi_index)

# 6、创建新列表[1, 2, 3, 4, 5, 6, 2]，合并入names列表
newlist = [1, 2, 3, 4, 5, 6, 2]
names.extend(newlist)  # extand方法，在列表末尾一次性追加另一序列的多个值（列表扩展）
# print(names)

# 7、取出names列表中索引4——7的元素
# print(names[4:7])

# 8、取出names列表中索引2——10的元素，步长为2
# print(names[2:10:2])

# 9、取出names列表中最后3个元素
# print(names[-3:])

# 10、循环names列表，打印每个元素的索引值，和元素
# for index, i in enumerate(names):
#     print(index, i)

# 11、循环names列表，打印每个元素的索引值，和元素，当索引值为偶数时，把对应的元素改为-1
# for index, i in enumerate(names):
#     if (index % 2) == 0:
#         i = '-1'
#     print(index, i)

# 12、names列表里有3个2，请返回第2个2的索引值。不要人肉数，要动态找（提示：找到第1个2的位置，在此基础上再找第2个）
# names.append("2")
# print(names)
# count = 0
# for index, i in enumerate(names):
#     if i == 2:
#         count += 1
#     if count == 3:
#         print(index, i)
#         break


# 13、现有商品列表如下：
products = [['Iphone8', 6888], ['MacPro', 14800], ['小米6', 2499], ['Coffee', 30], ['Book', 80], ['Nike Shoes', 799]]
    # 需要打印出这样的格式：

    # --------商品列表--------
    # 0.Iphone8 6888
    # 1.MacPro 14800
    # 2.小米6 2499
    # 3.Coffee 31
    # 4.Book 80
    # 5.Nike Shoes 799

print("-------商品列表------")
for index, i in enumerate(products):
    print(str(index) + ".", i[0], i[1])

# 14、写一个循环，不断的问用户想买什么，用户选择一个商品编号，就把对应的商品添加到购物车里，最终用户输入q退出时，打印购物车里的商品列表
shopping_cart = []
while True:
    user_choice = input("请输入商品编号 (按q退出)>>：")
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice < len(products):
            shopping_cart.append(products[user_choice])
            print("已添加商品 \033[31;1m%s\033[0m 到购物车" % products[user_choice][0])
        else:
            print("无该商品！")
    elif user_choice == 'q':
        if len(shopping_cart) != 0:
            print("------购物车-----")
            tatal = 0
            for s_index, s in enumerate(shopping_cart):
                print(s_index, s[0] + ":", s[1])
                tatal += int(s[1])
                if s_index == len(shopping_cart) - 1:
                    print("总计：\033[31;1m%s\033[0m" % tatal)
            print("----- -The End------")
        else:
            print("程序已终止。")
        exit()
    else:
        print("输入错误，请重新输入！")
