""" False 包括：
    1) None 
    2) 数值中的0(包括0.0) 
    3) 空序列，包括空字符串("")，空元组(())，空列表[]
    4) 空字典{} """
# and - 与，or - 或，not - 非
user_gender = input("请输入您的性别(F/M): ")
user_is_student = input("您是学生吗？(Y/N): ")

if user_gender == 'F':
    if user_is_student == 'Y':
        print("你是萌妹子学生")
    elif user_is_student == 'N':
        print('你是萌妹子')
    else:
        print("输入不正确")
elif user_gender == 'M':
    print("你是糙汉子")
else:
    print("输入不正确，请输入F或M")