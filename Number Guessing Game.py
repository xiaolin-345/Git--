
"""模块 随机数"""
import random
import os

wen_ben_wen_jian = r"D:\VS py测试\VS文本文件\cai_shu_zi_you_xi.txt.txt"

def diao_yong_os():
    if os.path.exists(wen_ben_wen_jian):
        with open(wen_ben_wen_jian,"r",encoding="utf-8") as f:
            for i in f:
                
                return i
            
def xie_ru_cheng_ji(ming_zi,nan_du,ci_shu,cheng_gong):
    with open(wen_ben_wen_jian,"a",encoding="utf-8") as f:
        if cheng_gong:
            shu_ju = f"玩家名字:{ming_zi} \t 次数:{ci_shu} \t 难度:{nan_du}\n"
        else:
            shu_ju = f"玩家名字:{ming_zi} \t 次数:{ci_shu} \t 难度:{nan_du}\n"
        f.write(shu_ju)
    print("成绩保存成功")
    print("=" * 20)
            
# 函数名（没有参数）
def xuan_zhe_nan_du():
    print("=" * 20 ,"游戏开始","=" * 20)
    
    # 无限循环
    while True:
       
        # 异常处理
        try:
            # 用户输入难度(等级)来判断
            
             # 用户输入难度（等级）
            qing_xuan_zhe_nan_du = int(input("请输入难度:1、简单 2、中等 3、困难:"))
            
            if qing_xuan_zhe_nan_du == 1:
                
                a = 50
                """ a : 在1-50之间的数猜 b : 1-50 为简单 """
                b = "简单"
                
                # 跳出循环体 执行后面的代码
                break
                
            
            elif qing_xuan_zhe_nan_du == 2:
                
                a = 100
                """ a : 在1-100之间的数猜 b : 1-100 为中等 """
                b = "中等"
                
                # 跳出循环体 执行后面的代码
                break
            
            elif qing_xuan_zhe_nan_du == 3:
                
                a = 500
                """ a : 在1-500之间的数猜 b : 1-500 为困难 """
                b = "困难"
                
                # 跳出循环体 执行后面的代码
                break
            
            # 如果用户输入的不是数字 则执行 else
            else:
                print(f"输入的不是难度选项：{qing_xuan_zhe_nan_du} 请重新输入！！！")    
                
        # 捕获异常（返回给 try）           
        except:
            print("请输入正确的选项！！！")
             
    # 用户输入难度（选项执行这行代码）   
    print("=" * 20 ,f"1-{a} 难度：{b}","=" * 20)
    
    # 返回值 a,b
    return a,b

# 函数名（没有参数）
def diao_yong_random():
    
    """获取第一个函数名的所有元素"""
    huo_qu_nan_du_xuan_xiang = xuan_zhe_nan_du()
    
    # 调用 random （难度由自己来定）
    sheng_cheng = random.randint(1,huo_qu_nan_du_xuan_xiang[0])
    
    # 初始数 0
    chu_shi_shu_zi = 0
    
    # 循环 不能超过10 (10次都没有猜出来就 执行 else)
    while chu_shi_shu_zi < 10:
        
        # 用户输入（数字）
        yong_hu = input("请输入你猜的数字：")
        
        # 异常处理
        try:
            
            # 将字符串转换为整数
            yong_hu = int(yong_hu)
        
        # 捕获异常（返回 try）    
        except ValueError:
            print(f"输入的不是数字：{yong_hu} 请重心新输入")
            
            """跳过当前循环的剩余代码"""
            continue
        
        # 初始数 （每次输入的时候都 +1）
        chu_shi_shu_zi += 1
        
        # 用户输入的（数字） 判断：大和小
        if yong_hu < sheng_cheng:
            
            """每次输入的时候 都会记录 输入多少次"""
            print(f"你猜的数字：{yong_hu} 太小了 再试试 你还有{10-chu_shi_shu_zi}次")
            
        elif yong_hu > sheng_cheng:
            
            """每次输入的时候 都会记录 输入多少次"""
            print(f"你猜的数字：{yong_hu} 太大了 再试试 你还有{10-chu_shi_shu_zi}次")
            
        # 猜对了就执行这行代码
        else:
            print("恭喜你猜对了")
            print(f"你一共用了：{chu_shi_shu_zi}")
            
            # 用户猜对了 并输入名字（返回：xie_ru_cheng_ji）
            qing_shu_ru_ming_zi = input("请输入参赛名字：")
            xie_ru_cheng_ji(qing_shu_ru_ming_zi,huo_qu_nan_du_xuan_xiang[1],chu_shi_shu_zi,cheng_gong="成功")
            
            # 跳出循环体 执行后面的代码
            break
    
        """10次都没有猜对 执行这行代码"""
    else:
        print("=" * 20 ,"游戏结束", "=" * 20)
        
        # 用户输入真实名字
        qing_shu_ru_ming_zi = input("请输入参赛名字：")
        
        # 显示（名字、正确数字）
        print(f"很遗憾：{qing_shu_ru_ming_zi} 没有猜中 正确答案：{sheng_cheng}")
        
        # 用户猜不对了 并输入名字（返回：xie_ru_cheng_ji）
        xie_ru_cheng_ji(qing_shu_ru_ming_zi,huo_qu_nan_du_xuan_xiang[1],chu_shi_shu_zi,cheng_gong="失败")
                
if __name__ == "__main__":
    diao_yong_random()
    
    

        
    
    
        
        
    
    
    
    
    