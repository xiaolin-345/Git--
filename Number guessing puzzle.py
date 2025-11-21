import random

def mi_ti():
    print("=" * 20, "游戏开始", "=" * 20)

    # 记录游戏数据
    yi_gong_wan_l = 0      # 总共玩了多少局
    yi_gong_ying_l = 0     # 总共赢了多少局

    while True:
        # 每开始新的一局
        yi_gong_wan_l += 1
        ben_lun_ci_shu = 0  # 重置本局猜测次数
        sui_ji = random.randint(1, 10)  # 每局生成新的随机数
        
        print(f"\n第{yi_gong_wan_l}局开始！")
        
        # 单局游戏循环
        while True:
            try:
                yong_hu = int(input("请猜1-10的数："))
                ben_lun_ci_shu += 1  # 每次猜测增加

                # 范围检查
                if yong_hu < 1 or yong_hu > 10:
                    print("请输入1-10的数字")
                    continue

                # 判断胜负
                if yong_hu == sui_ji:
                    print(f"猜对了！正确数字：{sui_ji}")
                    yi_gong_ying_l += 1
                    break
                else:
                    print("猜错了，再试试！")
                    
            except ValueError:
                print("请输入1-10的数字")

        # 询问是否继续
        while True:
            try:
                jixu = int(input("是否继续游戏？(1/0): "))
                
                if jixu in [1, 0]:
                    break
                else:
                    print("请输入 1 或 0")
            except:
                print("输入错误")
        
        if jixu == 1:
            break

    # 游戏结束统计
    print("=" * 20, "游戏结束", "=" * 20)
    print(f"游戏统计：")
    print(f"\t总共玩了：{yi_gong_wan_l}局")
    print(f"\t总共赢了：{yi_gong_ying_l}局")
    if yi_gong_wan_l > 0:
        shenglv = (yi_gong_ying_l / yi_gong_wan_l) * 100
        print(f"\t胜率：{shenglv:.1f}%")

if __name__ == "__main__":
    mi_ti()