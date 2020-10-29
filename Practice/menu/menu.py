# 三级菜单

# 字典
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车站': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

level = []
while True:
    for key in menu:
        print(key)           # 输出菜单
    choice = input("请选择 >>（按q退出，按r返回）:").strip()
    if choice == "q":
        break                # 可在任意位置退出程序
    elif choice == "r":
        if len(level) == 0:
            choice_2 = input("此为一级菜单，无法再返回，若继续按r则会退出程序，是否继续?（y|n）:").strip()
            if choice_2 == "y":
                break
            else:
                continue
        menu = level[-1]
        level.pop()          # 删除列表最后一个元素
    elif choice in menu:
        level.append(menu)   # 向列表追加当前菜单作为最后一个元素
        menu = menu[choice]  # 获取对应的下一级菜单
    else:
        continue
