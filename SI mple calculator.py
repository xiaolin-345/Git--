def ji_suan_qi():

    print("=" * 20 ,"欢迎使用简单计算器","=" * 20)
    print("可使用运算符：+、-、*、/、%、**")




    try:
        while True:

            yong_hu01 = int(input("请输入整数："))
            ji_suan = input("请输入运算符：")
            yong_hu02 = int(input("请输入整数："))

            if ji_suan == "+":
                quan_bu = yong_hu01 + yong_hu02
                print(f"用户输入：{yong_hu01} {ji_suan} {yong_hu02} = {quan_bu}")

                print("=" * 30)


            elif ji_suan == "-":
                quan_bu = yong_hu01 - yong_hu02
                print(f"用户输入：{yong_hu01} {ji_suan} {yong_hu02} = {quan_bu}")

                print("=" * 30)


            elif ji_suan == "*":
                quan_bu = yong_hu01 * yong_hu02
                print(f"用户输入：{yong_hu01} {ji_suan} {yong_hu02} = {quan_bu}")

                print("=" * 30)


            elif ji_suan == "/":
                quan_bu = yong_hu01 / yong_hu02
                print(f"用户输入：{yong_hu01} {ji_suan} {yong_hu02} = {quan_bu}")

                print("=" * 30)

            elif ji_suan == "%":
                quan_bu = yong_hu01 % yong_hu02
                print(f"用户输入：{yong_hu01} {ji_suan} {yong_hu02} = {quan_bu}")

                print("=" * 30)


            elif ji_suan == "**":
                quan_bu = yong_hu01 ** yong_hu02
                print(f"用户输入：{yong_hu01} {ji_suan} {yong_hu02} = {quan_bu}")

                print("=" * 30)

            else:
                print("重新输入")
                continue

            a = input("是否继续：(1/0):")
            if a == "1":
                print("程序结束")
                break
    except ValueError:
        print("请输入符号")

if __name__  == "__main__":
    ji_suan_qi()