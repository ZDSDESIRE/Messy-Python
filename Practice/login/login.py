# 登录认证程序
import pdb;
count = 0
users = [['bo', 'abc123'], ['zhou', 'abc123'], ['chen', 'abc123']]
exit_flag = False

while not exit_flag and count < 3:
    user_name = input("Name:")
    user_password = input("Password:")
    for index, i in enumerate(users):
        if user_name == i[0] and user_password == i[1]:
            print("Login Success!\nHello, " + user_name + "!")
            exit_flag = True
            break

    count += 1
    if count < 3:
        print("Username or password is wrong, please try again.")
    else:
        print("很抱歉，你的三次机会已用尽，程序终止！")
        exit_flag = True