gender = input("请输入您的性别(F/M): ")
while gender != 'M' and gender != "F":
    gender = input("您输入的性别有误，请重新输入(F/M): ")

age = input("请输入您的年龄: ")
while not age.isnumeric() or int(age) < 0 or int(age) > 100:
    age = input("您输入的年龄有误，请重新输入: ")


print("***您今年的运势***")
age_num = int(age)
if age_num >= 0 and age_num < 18:
    print("您会健康成长")
elif age_num == 18:
    print("您会考上好的大学")
elif age_num > 18 and age_num <=23:
    if gender == 'F':
        print("您会交上高富帅")
    else:
        print("您会交上白富美")
elif age_num > 23 and age_num < 40:
    print("您会财运亨通")
else:
    print("您会身体健康")

