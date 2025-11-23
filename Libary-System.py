import os
import json

# 常量定义 - 数据文件名
WEN_JIAN_MING = r"D:\VS py测试\VS文本文件\tu_shu_guan_li_xi_tong.json"

# 保存图书数据到JSON文件
def bao_cun_shu_ju(du_shu_shu_ju):

    try:
        # 以写入模式打开文件
        with open(WEN_JIAN_MING, "w", encoding="utf-8") as f:
            # 将数据转换为JSON格式保存
            # ensure_ascii=False: 确保中文正常显示
            # indent=2: 格式化输出，便于阅读
            json.dump(du_shu_shu_ju, f, ensure_ascii=False, indent=2)
        print(f"图书数据已保存到：{WEN_JIAN_MING}")
    except Exception as e:
        # 异常处理：保存失败时提示用户
        print(f"保存失败：{e}")
# 从JSON文件加载图书数据
def jia_zai_shu_ju():
    """
    返回：图书数据列表，如果文件不存在或加载失败返回空列表
    """
    # 检查文件是否存在
    if not os.path.exists(WEN_JIAN_MING):
        return []  # 文件不存在，返回空列表
    try:
        # 以读取模式打开文件
        with open(WEN_JIAN_MING, "r", encoding="utf-8") as f:
            shu_ju = json.load(f)  # 解析JSON数据
        return shu_ju
    except Exception as e:
        # 文件存在但加载失败（可能是格式错误）
        print(f"文件加载失败：{e}")
        return []  # 返回空列表

# 动保存数据功能
def shou_dong_bao_cun_shu_ju(du_shu_shu_ju):
    bao_cun_shu_ju(du_shu_shu_ju)  # 调用保存函数

# 图书管理系统入口
def tu_shu_guan():

    # 从文件加载数据
    du_shu_shu_ju = jia_zai_shu_ju()

    # 判断是否有数据
    if not du_shu_shu_ju:
        # 没有数据，使用默认数据
        du_shu_shu_ju = [
            {
                "shu_ming": "三位一体",
                "zuo_zhe": "小陈",
                "yue_du_jin_du": 90,
                "fen_lei": "科幻"
            }, {
                "shu_ming": "python入门",
                "zuo_zhe": "小林",
                "yue_du_jin_du": 95,
                "fen_lei": "编程"
            }, {
                "shu_ming": "人类简史",
                "zuo_zhe": "小徐",
                "yue_du_jin_du": 80,
                "fen_lei": "历史"
            }
        ]
        print("使用默认图书数据")

        # 将默认数据保存到文件，便于下次使用
        bao_cun_shu_ju(du_shu_shu_ju)
    else:
        # 有数据，显示加载信息
        print(f"文件加载：{len(du_shu_shu_ju)} 本图书")

    #主循环 显示菜单和处理用户输入
    while True:
        # 显示系统标题
        print("=" * 30, "图书管理系统", "=" * 30)

        # 显示功能菜单
        print("请选择功能：")
        print("1. 显示所有图书")
        print("2. 添加一本书")
        print("3. 删除一本书")
        print("4. 修改一本书")
        print("5. 查找一本书")
        print("6. 手动保存数据")
        print("7. 退出系统")

        print("=" * 30)

        try:
            # 获取用户输入并转换为整数
            yong_hu = int(input("请输入选项："))

            # 根据用户选择调用相应功能
            if yong_hu == 1:
                xian_shi_suo_you_tu_shu(du_shu_shu_ju)  # 显示所有图书
            elif yong_hu == 2:
                tian_jia_yi_ben_shu(du_shu_shu_ju)  # 添加图书
            elif yong_hu == 3:
                shan_chu_yi_ben_shu(du_shu_shu_ju)  # 删除图书
            elif yong_hu == 4:
                xiu_gai_yi_ben_shu(du_shu_shu_ju)  # 修改图书
            elif yong_hu == 5:
                cha_zhao_yi_ben_shu(du_shu_shu_ju)  # 查找图书
            elif yong_hu == 6:
                shou_dong_bao_cun_shu_ju(du_shu_shu_ju)  # 手动保存
            elif yong_hu == 7:
                # 退出系统前的处理
                print("=" * 20, "退出选项", "=" * 20)
                print("1：保存并退出 | 0：不保存退出")

                # 用户是否保存数据
                bao_cun_xuan_ze = int(input("是否保存数据(1/0)："))
                if bao_cun_xuan_ze == 1:
                    bao_cun_shu_ju(du_shu_shu_ju)  # 保存数据

                print("谢谢使用，下次再见！")
                break  # 退出循环，结束程序
            else:
                # 输入超出范围提示
                print("请输入1-7之间的选项")

        except ValueError:
            # 输入非数字时的异常处理
            print("请输入数字！")

# 显示所有图书信息
def xian_shi_suo_you_tu_shu(du_shu_shu_ju):

    # 是否有数据
    if not du_shu_shu_ju:
        print("书架上还没有书呢！")
        return

    # 显示标题
    print("=" * 30, "所有图书列表", "=" * 30)

    # 遍历并显示每本书的信息
    for i in du_shu_shu_ju:
        print(f"书名：{i['shu_ming']} \t 作者：{i['zuo_zhe']} \t 阅读进度：{i['yue_du_jin_du']} \t 分类：{i['fen_lei']}")

# 添加新图书
def tian_jia_yi_ben_shu(du_shu_shu_ju):

    while True:  # 循环直到输入正确
        try:
            # 获取图书信息
            shu_ming = input("请输入书名：")
            zuo_zhe = input("请输入作者：")
            yue_du_jin_du = int(input("请输入阅读进度："))
            fen_lei = input("请输入分类：")

            # 阅读进度范围
            if yue_du_jin_du < 0 or yue_du_jin_du > 100:
                print("阅读进度必须是0-100之间，请重新输入")
                continue  # 重新输入

            # 创建新图书字典
            zeng_ji_shu_ju = {
                "shu_ming": shu_ming,
                "zuo_zhe": zuo_zhe,
                "yue_du_jin_du": yue_du_jin_du,
                "fen_lei": fen_lei
            }

            # 添加到数据列表
            du_shu_shu_ju.append(zeng_ji_shu_ju)

            # 显示成功信息
            print(f"成功添加新图书："
                  f"书名：《{shu_ming}》 | "
                  f"作者：{zuo_zhe} | "
                  f"阅读进度：{yue_du_jin_du}% | "
                  f"分类：{fen_lei}")

            # 是否保存
            bao_cun_xuan_ze = input("是否保存到文件(1/0): ")
            if bao_cun_xuan_ze == "1":
                bao_cun_shu_ju(du_shu_shu_ju)
                print("增加数据保存成功")
            else:
                print("数据仅在内存中，退出将丢失")

            break  # 添加成功，退出循环

        except ValueError:
            # 阅读进度输入非数字时的处理
            print("阅读进度必须是数字！")

# 删除指定图书
def shan_chu_yi_ben_shu(du_shu_shu_ju):

    # 是否有数据可删除
    if not du_shu_shu_ju:
        print("书架上没有书可以删除")
        return

    # 获取要删除的书名
    shan_chu = input("请输入要删除的书名：")

    biao_ji = False  # 标记是否找到并删除

    # 遍历查找要删除的图书
    for i in du_shu_shu_ju:
        if i["shu_ming"] == shan_chu:

            # 找到图书，执行删除
            du_shu_shu_ju.remove(i)
            print(f"删除一本书：《{shan_chu}》删除成功")

            biao_ji = True  # 标记已删除

            # 是否保存
            bao_cun_xuan_ze = input("是否保存到文件(1/0): ")
            if bao_cun_xuan_ze == "1":
                bao_cun_shu_ju(du_shu_shu_ju)
                print("删除数据保存成功")
            else:
                print("删除仅在内存中，退出将恢复")

            break  # 找到并删除后退出循环

    # 未找到图书的处理
    if not biao_ji:
        print(f"没有这本书：《{shan_chu}》无法删除")

# 修改图书信息
def xiu_gai_yi_ben_shu(du_shu_shu_ju):

    # 是否有数据可修改
    if not du_shu_shu_ju:
        print("书架上没有书可以修改")
        return

    # 获取要修改的书名
    quna_tu_shu = input("请输入要修改的书名：")

    biao_ji = False  # 标记是否找到图书

    # 遍历查找要修改的图书
    for i in du_shu_shu_ju:
        if i["shu_ming"] == quna_tu_shu:
            biao_ji = True  # 标记已找到

            # 修改菜单（循环）
            while True:
                print("=" * 20, "修改选项", "=" * 20)
                print("1. 修改书名")
                print("2. 修改作者")
                print("3. 修改阅读进度")
                print("4. 修改分类")
                print("5. 退出修改")
                print("=" * 40)

                try:
                    # 获取用户输入
                    xin_du_shu = int(input("请输入选项(1-5)："))

                    # 修改书名
                    if xin_du_shu == 1:
                        xiu_gai_shu_ming = input("请输入新书名：")
                        i["shu_ming"] = xiu_gai_shu_ming
                        print(f"书名修改为：《{xiu_gai_shu_ming}》")

                    # 修改作者
                    elif xin_du_shu == 2:
                        xiu_gai_zuo_zhe = input("请输入新作者：")
                        i["zuo_zhe"] = xiu_gai_zuo_zhe
                        print(f"作者修改为：{xiu_gai_zuo_zhe}")

                    # 修改阅读进度
                    elif xin_du_shu == 3:
                        xiu_gai_yue_du_jin_du = int(input("请输入阅读进度："))
                        if 0 <= xiu_gai_yue_du_jin_du <= 100:
                            i["yue_du_jin_du"] = xiu_gai_yue_du_jin_du
                            print(f"阅读进度修改为：{xiu_gai_yue_du_jin_du}%")
                        else:
                            print("阅读进度必须是0-100之间")

                    # 修改分类
                    elif xin_du_shu == 4:
                        xiu_gai_fen_lei = input("请输入分类：")
                        i["fen_lei"] = xiu_gai_fen_lei
                        print(f"分类修改为：{xiu_gai_fen_lei}")

                    # 退出修改
                    elif xin_du_shu == 5:
                        print("✅ 修改完成，谢谢！")
                        break  # 退出修改循环
                    else:
                        print("请输入1-5之间的选项")

                    # 每次修改后询问是否保存
                    bao_cun_xuan_ze = input("是否保存到文件(1/0): ")
                    if bao_cun_xuan_ze == "1":
                        bao_cun_shu_ju(du_shu_shu_ju)
                        print("修改数据保存成功")

                except ValueError:
                    # 输入非数字时的处理
                    print("请输入数字选项(1-5)")

            break  # 找到图书并处理完成后退出循环

    # 未找到图书的处理
    if not biao_ji:
        print(f"没有这本书：《{quna_tu_shu}》无法修改")

# 查找图书
def cha_zhao_yi_ben_shu(du_shu_shu_ju):

    # 是否有数据可查找
    if not du_shu_shu_ju:
        print("书架上没有书可以查找")
        return

    # 获取要查找的书名
    cha_zhao = input("请输入要查找的书名：")

    biao_ji = False  # 标记是否找到

    # 遍历查找图书
    for i in du_shu_shu_ju:
        if i["shu_ming"] == cha_zhao:

            # 找到图书，显示信息
            print(f"找到这本书："
                  f"书名：《{i['shu_ming']}》 | "
                  f"作者：{i['zuo_zhe']} | "
                  f"阅读进度：{i['yue_du_jin_du']}% | "
                  f"分类：{i['fen_lei']}")

            biao_ji = True

            break  # 找到后退出循环

    # 未找到图书的处理
    if not biao_ji:
        print(f"没有这本书：《{cha_zhao}》无法查找")

if __name__ == "__main__":
    tu_shu_guan()