# 购物车程序：
#     数据结构：
#     goods = [
#     {"name": "电脑", "price": 1999},
#     {"name": "鼠标", "price": 10},
#     {"name": "游艇", "price": 20},
#     {"name": "美女", "price": 998},
#     ......
#     ]
#
#     功能要求：
#     基础要求：
#
#     1、启动程序后，输入用户名密码后，让用户输入工资，然后打印商品列表
#  
#     2、允许用户根据商品编号购买商品
#
#     3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
#
#     4、可随时退出，退出时，打印已购买商品和余额
#
#     5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示
#
#
#     扩展需求：
#
#     1、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
#
#     2、允许查询之前的消费记录

# 用户信息
user_info = {
    'bo': 'bo123',
}

# 商品列表
product_list = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
    {"name": "iPhone", "price": 600},
    {"name": "书", "price": 8},
    {"name": "汽车", "price": 2998},
    {"name": "房", "price": 9999},
]

shopping_list = []  # 定义一个空列表，用于存放要购买的商品
count = 0

while True:
    count += 1
    username = input("用户名 >>: ")
    password = input("密码 >>: ")
    if user_info.get(username, None) == password:
        while True:
            salary = input("请输入你的工资 >>：")
            if salary.isdigit():  # 检测输入的字符串是否全为数字，是则返回Ture, 反之返回False
                salary = int(salary)
                while True:
                    print("------商品列表------")
                    for index, i in enumerate(product_list):
                        print((int(index) + 1), i["name"] + ":", i["price"])
                    print("------商品列表------")
                    user_choice = input("请输入你要购买的商品编号(按q退出) >>：").strip()
                    if user_choice.isdigit():
                        user_choice = int(user_choice)
                        if user_choice <= len(product_list):
                            product_choice = product_list[user_choice - 1]
                            if product_choice["price"] < salary:
                                shopping_list.append(product_choice)  # 可以购买的商品，添加到购物车
                                salary -= product_choice["price"]     # 扣除已选商品的价格的余额
                                print("已添加商品 \033[31;1m%s\033[0m 到购物车, 目前你的账户余额为：\033[31;1m%s\033[0m" %
                                      (product_choice["name"], salary))
                            else:
                                print("\033[31;1m很抱歉，你的余额只剩下%s，不足以购买该商品！\033[0m" % salary)
                        else:
                            print("输入错误，无该商品！")
                    elif user_choice == "q":
                        print("------已购商品-----")
                        for s_index, s in enumerate(shopping_list):
                            print((int(s_index) + 1), s['name'] + ":", s['price'])
                        print("------已购商品-----")
                        print("目前的余额为：\033[31;1m%s\033[0m" % salary)
                        exit()
                    else:
                        print("输入错误！")
            else:
                print("输入错误，请重试！")
    elif count >= 3 and user_info.get(username, None) != password:
        print("你已经错了3次了!不能再试了!")
        exit()
    else:
        print("用户名或密码输入错误，请重新输入!")
        continue