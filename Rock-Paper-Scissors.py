# 随机模块
import random

# 函数
def diao_yong_random():
    
    # 游戏规则
    print("=" * 20, "石头剪刀布游戏开始", "=" * 20)
    print("游戏规则：\n"
          "\t1:石头  2:剪刀  3:布\n"
          "\t石头赢剪刀\n"
          "\t剪刀赢布\n"
          "\t布赢石头\n"
          "\t相同就是平局\n"
          )
    
    # 无限循环
    while True:
        # 异常处理
        try:
            # 记录（用户、电脑、平局的次数）
            yong_hu_ci_shu = 0
            dian_nao_ci_shu = 0
            ping_ju_ci_shu = 0
            
            # 随机数
            dian_nao = random.randint(1, 3)
            # 用户输入
            yong_hu = input("请输入石头剪刀布(1/2/3):")
            # 将用户输入的数字 转换为 整数
            zheng_shu = int(yong_hu)

            # 检查输入是否在有效范围内
            if zheng_shu not in [1, 2, 3]:
                print(f"输入:{zheng_shu} 请输入1-3的数字")
                
                # 跳出当前的循环剩余的代码 继续循环下一次循环
                continue

            # 游戏逻辑判断
            if zheng_shu == 1:  
                if dian_nao == 1:   # 石头
                    print(f"电脑出：石头({dian_nao})")
                    
                    # 平局 +1
                    ping_ju_ci_shu += 1
                    
                    print("平局")
                    
                elif dian_nao == 2:
                    print(f"电脑出：剪刀({dian_nao})")
                    
                    # 用户 +1
                    yong_hu_ci_shu += 1
                    
                    print("我赢了")
                    
                else:
                    print(f"电脑出：布({dian_nao})")
                    print("电脑赢了")
                    
                    # 电脑 +1
                    dian_nao_ci_shu += 1
              

            elif zheng_shu == 2:  # 剪刀
                if dian_nao == 2:
                    print(f"电脑出：剪刀({dian_nao})")
                    
                    # 平局 +1
                    ping_ju_ci_shu += 1
                    
                    print("平局")
                    
                elif dian_nao == 3:
                    print(f"电脑出：布({dian_nao})")
                    
                    # 用户 +1
                    yong_hu_ci_shu += 1
                    
                    print("我赢了")
                    
                else:
                    print(f"电脑出：石头({dian_nao})")
                    print("电脑赢了")
                    
                    # 电脑 +1
                    dian_nao_ci_shu += 1

            elif zheng_shu == 3:  # 布
                if dian_nao == 3:
                    print(f"电脑出：布({dian_nao})")
                    
                    # 平局 +1
                    ping_ju_ci_shu += 1
                    
                    print("平局")
                    
                elif dian_nao == 1:
                    print(f"电脑出：石头({dian_nao})")
                    
                    # 用户 +1
                    yong_hu_ci_shu += 1
                    
                    print("我赢了")
                else:
                    print(f"电脑出：剪刀({dian_nao})")
                    
                    
                    print("电脑赢了")
                    
                    # 电脑 +1
                    dian_nao_ci_shu += 1
            # 用户、电脑、平局的次数 打印出来       
            print(f"当前比分:玩家:{yong_hu_ci_shu} 电脑:{dian_nao_ci_shu} 平局:{ping_ju_ci_shu}")

        # 捕获异常（整数了类型）
        except ValueError:
            print("输入的不是数字，请重新输入")
            
            # 跳出当前的循环剩余的代码 继续循环下一次循环
            continue

        # 询问是否继续
        while True:
            try:
                # 用户输入 是否继续 游玩
                shi_fou_ji_xu = int(input("是否继续(1继续/0退出):"))
                # 用户输入0 将退出程序
                if shi_fou_ji_xu == 0:
                    print("=" * 20, "游戏结束", "=" * 20)
                    print("感谢游玩")
                    return  # 直接退出函数
                
                # 用户输入1 程序将重新执行
                elif shi_fou_ji_xu == 1:
                    print("开始新游戏...")
                    break  # 跳出内层循环，继续外层循环
                
                else:
                    print(f"输入：{shi_fou_ji_xu}，请输入1或0")
            # 捕获异常
            except ValueError:
                print("请输入数字1或0")

if __name__ == "__main__":
    diao_yong_random()