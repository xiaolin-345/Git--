# 导入操作系统模块，用于文件路径检查等操作
import os

# 文件路径 
wen_jian_ming = r"D:\VS py测试\VS文本文件\xue_sheng_cheng_ji_guan_li_xi_tong.txt"

# 保存所有学生数据到文件
def bao_cun_shu_ju(xue_sheng_shu_ju):
   
    try:
        # 以写入模式打开文件，
        # "w"模式会清空文件原有内容，然后写入新内容
        with open(wen_jian_ming, "w", encoding="utf-8") as f:
            
            # 遍历每个学生信息
            for i in xue_sheng_shu_ju:
                
                # 将学生信息格式化为CSV格式：姓名,语文成绩,数学成绩,英语成绩
                cun_fang = f"姓名：{i['name']} \t 语文：{i['yu_wen']} \t 数学：{i['shu_xue']} \t 英语：{i['ying_yu']}\n"
                
                # 将格式化后的行写入文件
                f.write(cun_fang)
                
        # 保存成功提示
        print(f"学生数据已保存到:{wen_jian_ming}")
        
    except Exception as f:
        # 如果保存过程中出现任何错误，捕获并显示错误信息
        print(f"保存失败: {f}")


def jia_zai_shu_ju():
    """
    从文件加载学生数据
    返回值: 包含所有学生信息的列表，如果文件不存在则返回空列表
    """
    
    # 初始化空列表，用于存储加载的学生数据
    xue_sheng_shu_ju = []

    # 检查数据文件是否存在，如果不存在直接返回空列表
    if not os.path.exists(wen_jian_ming):
        return xue_sheng_shu_ju

    try:
        # 以只读模式打开文件
        with open(wen_jian_ming, "r", encoding="utf-8") as f:
            
            # 逐行读取文件内容
            for i in f:
                
                # 去除每行首尾的空白字符
                jian_cha = i.strip()
                
                # 检查是否为空行
                if jian_cha:
                    
                    # 使用逗号分割每行数据，得到各个字段
                    parts = jian_cha.split(",")
                    
                    # 确保每行有4个字段（姓名,语文,数学,英语）
                    if len(parts) == 4:
                        
                        # 创建学生字典对象
                        xue_sheng = {
                            "name": parts[0],      # 学生姓名
                            "yu_wen": int(parts[1]),  # 语文成绩（转换为整数）
                            "shu_xue": int(parts[2]), # 数学成绩（转换为整数）
                            "ying_yu": int(parts[3])  # 英语成绩（转换为整数）
                        }
                        
                        # 将学生信息添加到列表中
                        xue_sheng_shu_ju.append(xue_sheng)
                        
        # 显示成功加载的学生数量
        print(f"从文件加载了 {len(xue_sheng_shu_ju)} 个学生数据")
        
    except Exception as f:
        # 如果加载过程中出现任何错误，捕获并显示错误信息
        print(f"加载失败: {f}")

    # 返回加载的学生数据列表
    return xue_sheng_shu_ju

# 学生成绩管理系统主函数
def student_management_system():
   
    # 自动从文件加载学生数据
    xue_sheng_shu_ju = jia_zai_shu_ju()

    # 如果文件不存在或文件为空，使用默认的学生数据
    if not xue_sheng_shu_ju:
        # 默认学生数据（6个学生）
        xue_sheng_shu_ju = [
            {"name": "小陈", "yu_wen": 85, "shu_xue": 92, "ying_yu": 78},
            {"name": "小林", "yu_wen": 76, "shu_xue": 88, "ying_yu": 90},
            {"name": "小徐", "yu_wen": 85, "shu_xue": 91, "ying_yu": 76},
            {"name": "小富", "yu_wen": 73, "shu_xue": 92, "ying_yu": 87},
            {"name": "小兵", "yu_wen": 84, "shu_xue": 95, "ying_yu": 74},
            {"name": "小胡", "yu_wen": 78, "shu_xue": 89, "ying_yu": 94}
        ]
        # 提示用户使用的是默认数据
        print("默认学生数据")

    # 主程序循环，持续显示菜单直到用户选择退出
    while True:
        
        # 显示系统标题
        print("=" * 30, "学生成绩管理系统", "=" * 30)

        # 显示功能菜单
        print("请选择功能：")
        print("1.显示所有学生成绩")    
        print("2.添加新学生")         
        print("3.删除学生")          
        print("4.修改成绩")         
        print("5.查找学生成绩")      
        print("6.计算平均分排名")      
        print("7.学科统计")           
        print("8.保存数据在文件")     
        print("9.退出系统")          

        try:
            # 获取用户选择并转换为整数
            yong_hu = int(input("请输入选择(1-9)："))

            # 根据用户选择调用相应的功能
            if yong_hu == 1:
                xian_shi_suo_you_xue_sheng(xue_sheng_shu_ju)
            elif yong_hu == 2:
                zeng_jia_xin_xue_sheng(xue_sheng_shu_ju)
            elif yong_hu == 3:
                zhi_ding_shan_chu(xue_sheng_shu_ju)
            elif yong_hu == 4:
                xiu_gai_xue_sheng(xue_sheng_shu_ju)
            elif yong_hu == 5:
                cha_zhao_xue_sheng(xue_sheng_shu_ju)
            elif yong_hu == 6:
                xian_shi_pai_ming(xue_sheng_shu_ju)
            elif yong_hu == 7:
                ke_mu_tong_ji(xue_sheng_shu_ju)
                
            elif yong_hu == 8:
                # 手动保存数据到文件
                bao_cun_shu_ju(xue_sheng_shu_ju)
                
            elif yong_hu == 9:
                # 退出前的保存选项
                print("=" * 20 ,"1：退出(保存) 0：不保存", "=" * 20)
                
                shi_hou_ban_cun = int(input("是否保存学生数据(1/0):"))
                
                if shi_hou_ban_cun == 1:
                    bao_cun_shu_ju(xue_sheng_shu_ju)
                print("谢谢使用！再见")
                
                break  # 退出主循环，结束程序
            else:
                print("无效选择，请重新输入！")

        except ValueError:
            # 处理用户输入非数字
            print("请输入1-9的选择")

# 显示所有学生的姓名和各科成绩
def xian_shi_suo_you_xue_sheng(xue_sheng_shu_ju):
   
    # 遍历每个学生并显示其信息
    for i in xue_sheng_shu_ju:
        print(f"姓名：{i['name']} , 语文：{i['yu_wen']} , 数学：{i['shu_xue']} , 英语：{i['ying_yu']}")

# 添加新学生到系统
def zeng_jia_xin_xue_sheng(xue_sheng_shu_ju):
   
    # 循环直到成功添加学生或取消
    while True:
        try:
            # 获取新学生信息
            name = input("请输入姓名：")
            yu_wen = int(input("请输入语文成绩："))
            shu_xue = int(input("请输入数学成绩："))
            ying_yu = int(input("请输入英语成绩："))
            
            # 验证成绩范围（0-100分）
            if 0 <= yu_wen <= 100 and 0 <= shu_xue <= 100 and 0 <= ying_yu <= 100:
                
                # 创建新学生字典
                shu_ju = {
                    "name": name,
                    "yu_wen": yu_wen,
                    "shu_xue": shu_xue,
                    "ying_yu": ying_yu
                }
                
            else:
                # 成绩超出范围，提示重新输入
                print("成绩0-100之间，请重新输入")
                continue  # 跳过本次循环剩余部分，重新开始

            # 将新学生添加到列表
            xue_sheng_shu_ju.append(shu_ju)

            # 显示添加成功信息
            print(f"成功添加新学生：姓名：{name} --- 语文：{yu_wen} --- 数学：{shu_xue} --- 英语：{ying_yu}")

            #  自动保存数据到文件
            bao_cun_shu_ju(xue_sheng_shu_ju)
            print("学生数据保存成功")
            
            break  # 添加成功，退出循环

        except ValueError:
            # 处理成绩输入非数字的情况
            print("请输入语文、数学、英语成绩")

# 删除指定学生
def zhi_ding_shan_chu(xue_sheng_shu_ju):

    # 获取要删除的学生姓名
    shan_chu = input("请输入要删除的学生姓名：")

    # 标记是否找到并删除的学生
    biao_ji = False

    # 遍历查找要删除的学生
    for i in xue_sheng_shu_ju:
        if i["name"] == shan_chu:
            
            # 找到学生，从列表中删除
            xue_sheng_shu_ju.remove(i)
            print(f"成功删除学生：{shan_chu}")
            
            biao_ji = True  # 设置标记为True

            #  自动保存数据到文件
            bao_cun_shu_ju(xue_sheng_shu_ju)
            print("学生数据保存成功")
            
            break  # 找到并删除后立即退出循环
    
    # 如果循环结束都没有找到学生
    if not biao_ji:
        print(f"没有找到该学生：{shan_chu} 无法删除")

# 修改学生信息
def xiu_gai_xue_sheng(xue_sheng_shu_ju):
  
    # 获取要修改的学生姓名
    yun_ming_zi = input("请输入要修改的学生姓名：")
    biao_ji = False
    
    # 遍历查找要修改的学生
    for i in xue_sheng_shu_ju:
        if i["name"] == yun_ming_zi:
            biao_ji = True  # 找到学生，设置标记

            # 显示修改选项菜单
            print("=" * 10 ,"1：修改学生姓名 2：修改学生的语文 3：修改学生的数学 4：修改学生的英语 5：退出", "=" * 10)

            # 获取用户要修改的内容
            xiu_gai = int(input("请输入要修改学生的成绩(1-5):"))
            
            # 根据选择执行相应的修改操作
            if xiu_gai == 1:
                xing_ming_xiu_gai = input("请输入学生新姓名：")
                i["name"] = xing_ming_xiu_gai
                print(f"修改成功 当前学生信息：{i}")

            elif xiu_gai == 2:
                yu_wen_xiu_gai = int(input("请输入学生语文成绩："))
                i["yu_wen"] = yu_wen_xiu_gai
                print(f"修改成功 当前学生信息：{i}")

            elif xiu_gai == 3:
                shu_xue_xiu_gai = int(input("请输入学生数学成绩："))
                i["shu_xue"] = shu_xue_xiu_gai
                print(f"修改成功 当前学生信息：{i}")

            elif xiu_gai == 4:
                ying_yu_xiu_gai = int(input("请输入学生英语成绩："))
                i["ying_yu"] = ying_yu_xiu_gai
                print(f"修改成功 当前学生信息：{i}")

            elif xiu_gai == 5:
                print("修改程序 已退出")
                return  # 直接退出，不保存

            # 自动保存数据到文件
            bao_cun_shu_ju(xue_sheng_shu_ju)
            print("学生数据保存成功")
            
            break  # 修改完成后退出循环

    # 如果循环结束都没有找到学生
    if not biao_ji:
        print(f"没有找到该学生：{yun_ming_zi} 无法修改")

# 根据姓名查找学生信息
def cha_zhao_xue_sheng(xue_sheng_shu_ju):
   
    # 获取要查找的学生姓名
    cha_zhao_xue_sheng = input("请输入要查找哪位学生：")

    # 标记是否找到学生
    biao_ji = False

    # 遍历查找学生
    for i in xue_sheng_shu_ju:
        if i["name"] == cha_zhao_xue_sheng:
            
            # 找到学生，显示详细信息
            print(f"找到学生：姓名：{i['name']} --- 语文：{i['yu_wen']} --- 数学：{i['shu_xue']} --- 英语：{i['ying_yu']}")
            
            biao_ji = True  # 设置标记为True
            
            break  # 找到后立即退出循环
    
    # 如果循环结束都没有找到学生
    if not biao_ji:
        print(f"学生不存在：{cha_zhao_xue_sheng}")

# 计算并显示学生平均分排名
def xian_shi_pai_ming(xue_sheng_shu_ju):
   
    # 创建新列表存储学生平均分信息
    xue_sheng_ping_jun_fen = []

    # 计算每个学生的平均分
    for xue_sheng in xue_sheng_shu_ju:
        
        # 计算总分
        zong_fen = xue_sheng["yu_wen"] + xue_sheng["shu_xue"] + xue_sheng["ying_yu"]
        
        # 计算平均分（保留小数）
        ping_jun_fen = zong_fen / 3
        
        # 将学生信息和平均分存储到新列表
        xue_sheng_ping_jun_fen.append({
            "name": xue_sheng["name"],
            "ping_jun_fen": ping_jun_fen,
            "yu_wen": xue_sheng["yu_wen"],
            "shu_xue": xue_sheng["shu_xue"],
            "ying_yu": xue_sheng["ying_yu"]
        })

    # 按平均分从高到低排序
    # sorted()：函数返回新列表，不修改原列表
    # key=lambda x: x["ping_jun_fen"] 指定按平均分排序
    # reverse=True 表示降序排列（从高到低）
    pai_xu = sorted(xue_sheng_ping_jun_fen, key=lambda x: x["ping_jun_fen"], reverse=True)

    # 显示排名结果
    # enumerate()函数同时获取索引和元素，start=1表示从1开始计数
    for pai_ming, xue_sheng in enumerate(pai_xu, 1):
        
        # 显示名次、姓名和平均分（保留1位小数）
        print(f"第{pai_ming}名：{xue_sheng['name']} | 平均分：{xue_sheng['ping_jun_fen']:.1f}")

# 统计各学科的成绩
def ke_mu_tong_ji(xue_sheng_shu_ju):
  
    # 初始化各科成绩列表
    yu_wen_list = []   # 存储所有语文成绩
    shu_xue_list = []  # 存储所有数学成绩
    ying_yu_list = []  # 存储所有英语成绩

    # 收集各科成绩数据
    for xue_sheng in xue_sheng_shu_ju:
        yu_wen_list.append(xue_sheng["yu_wen"])
        shu_xue_list.append(xue_sheng["shu_xue"])
        ying_yu_list.append(xue_sheng["ying_yu"])

    # 计算语文科目统计信息
    yu_wen_tongji = {
        "科目": "语文",
        "平均分": f"{sum(yu_wen_list) / len(yu_wen_list):.1f}",  # 计算平均分并保留1位小数
        "最高分": max(yu_wen_list),  # 最高分
        "最低分": min(yu_wen_list)   # 最低分
    }

    # 计算数学科目统计信息
    shu_xue_tongji = {
        "科目": "数学",
        "平均分": f"{sum(shu_xue_list) / len(shu_xue_list):.1f}",
        "最高分": max(shu_xue_list),
        "最低分": min(shu_xue_list)
    }

    # 计算英语科目统计信息
    ying_yu_tongji = {
        "科目": "英语",
        "平均分": f"{sum(ying_yu_list) / len(ying_yu_list):.1f}",
        "最高分": max(ying_yu_list),
        "最低分": min(ying_yu_list)
    }

    # 显示各科统计结果
    print("成绩统计：", yu_wen_tongji)
    print("成绩统计：", shu_xue_tongji)
    print("成绩统计：", ying_yu_tongji)

if __name__ == "__main__":
    student_management_system()