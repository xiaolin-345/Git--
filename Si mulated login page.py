# 模拟一个简单的登录验证（输入用户名和密码，判断是否正确）
# 输入账号和密码只有6次机会
zui_da_ci_shu = 6  
#  初始值
chu_shi_zhi = 0

kong_lie_biao = []


def zhang_hao_he_mi_ma():
    print("=" * 20, "欢迎进入709-909宿舍", "=" * 20)
    print("=" * 11, "请登录个人账号和密码(密码默认:123456)","=" * 11)

    # 存储数据
    shu_ju = {
        "陈蛋蛋":
            {
                "mi_ma": 123456,
                "外号": "老徐",
                "年龄": "20以上",
                
                "职业": "学生",
                "喜欢": "打羽毛球",
                "床位": "进门的第一个"
            },

        "小林":
            {
                "mi_ma": 123456,
                "外号": "笑笑",
                "年龄": "18",
             
                "职业": "学生",
                "喜欢": "跑步",
                "床位": "进门的第二个"
            },
        "小徐":
            {
                "mi_ma": 123456,
                "年龄": "19",
                "外号": "徐老大",
              
                "职业": "学生",
                "喜欢": "玩手机",
                "床位": "进门的第三个"
            },
        "富贵":
            {
                "mi_ma": 123456,
                "外号": "太阴了",
                "年龄": "20以上",
              
                "职业": "学生",
                "喜欢": "帮助别人",
                "床位": "进门的第四个"
            },
        "兵王":
            {
                "mi_ma": 123456,
                "外号": "小兵王",
                "年龄": "20以上",
               
                "职业": "学生",
                "喜欢": "打三角洲别人",
                "床位": "进门后面的第一个",

            },
        "小胡":
            {
                "mi_ma": 123456,
                "年龄": "20以上",
                "外号": "健身狂魔",
               
                "职业": "学生",
                "喜欢": "健身",
                "床位": "进门后面的第二个"

            }
    }

    # 存储当前的用户
    cun_chu_dang_qian_deng_lu_yong_hu = None
    # 初始值
    chi_shi_zhi = 0  

    # 无限循环
    while chi_shi_zhi < zui_da_ci_shu:  
        # 异常处理
        try:
            
            # 用户输入（账号和密码）
            zhang_hao = input("请输入账号：").strip()
            mi_ma = int(input("请输入密码："))

            # 检查账号是否存在（密码正确）
            if zhang_hao in shu_ju and mi_ma == shu_ju[zhang_hao]["mi_ma"]:
                
                cun_chu_dang_qian_deng_lu_yong_hu = zhang_hao
                
                print(f"\n登录成功 {shu_ju[zhang_hao]['外号']}")  

                # 登录成功就退出循环（登录不成功就进入循环直到登陆成功）
                break
            
            else:
                """初始值 +1"""
                chi_shi_zhi += 1
                
                # 每次输入的都会记录 直到6次机会都用完
                sheng_yu_ci_shu = zui_da_ci_shu - chi_shi_zhi  

                if zhang_hao not in shu_ju:
                    
                    # 用户6次都没有输对就执行
                    print(f"账号不存在", end=" ")
                else:
                    print(f"密码错误", end=" ")

                # 用户输入的过程也会返回你还有多少机会（可使用）
                if sheng_yu_ci_shu > 0:
                    print(f"还剩{sheng_yu_ci_shu}次机会")
                else:
                    print(f"机会已用完 请在看看密码 稍后再试")
                    
        # 如果出现异常就会捕获给try
        except ValueError:
            # 异常 +1
            chi_shi_zhi += 1
            # 密码不是数字 则会执行
            sheng_yu_ci_shu = zui_da_ci_shu - chi_shi_zhi  
            if sheng_yu_ci_shu > 0:
                print(f"密码必须是数字！还剩{sheng_yu_ci_shu}次机会")
            else:
                print(f"机会已用尽，请好好想想账号和密码")


    if cun_chu_dang_qian_deng_lu_yong_hu:
        # 无限循环
        while True:
            print("\n" + "=" * 30)

            # 登录成功 就可以选择下来的选项
            print("请选择要操作的功能：")
            print("                 1. 查看个人信息")
            print("                 2. 修改密码")
            print("                 3. 退出系统")

            print("=" * 30)

            # 我发现用户输入可能出现"空格"所以加了strip() 不管用户输入有没有空格都会排除
            xuan_zhi = input("请输入你的选项(1-3):").strip()


            if xuan_zhi == "1":
                print("\n 个人信息：")
                print(f"            账号:{cun_chu_dang_qian_deng_lu_yong_hu}")
                print(f"            外号:{shu_ju[cun_chu_dang_qian_deng_lu_yong_hu]['外号']}")  
                print(f"            年龄:{shu_ju[cun_chu_dang_qian_deng_lu_yong_hu]['年龄']}")
         
                print(f"            职业:{shu_ju[cun_chu_dang_qian_deng_lu_yong_hu]['职业']}")
                print(f"            喜欢:{shu_ju[cun_chu_dang_qian_deng_lu_yong_hu]['喜欢']}")
                print(f"            床位:{shu_ju[cun_chu_dang_qian_deng_lu_yong_hu]['床位']}")

            elif xuan_zhi == "2":
                print("=" * 30, "修改密码", "=" * 30)

                # 异常处理
                try:
                    # 修改密码就要先输入旧密码
                    jiu_mi_ma = int(input("请输入原来的密码：")) 
                    if jiu_mi_ma == shu_ju[cun_chu_dang_qian_deng_lu_yong_hu]["mi_ma"]:
                        
                        # 用户输入新密码
                        xin_mi_ma = int(input("请输入新密码:"))
                        zai_shi_yi_ci = int(input("请在次输入新密码:"))

                        if xin_mi_ma == zai_shi_yi_ci:
                            shu_ju[cun_chu_dang_qian_deng_lu_yong_hu]["mi_ma"] = xin_mi_ma
                            print("密码修改成功")
                        else:
                            print("两次输入的新密码不一致 请重新输入")
                    else:
                        print("原密码错误")
                
                # 可能会出现异常（用户输入的不是我的代码要求的 就会去捕抓）
                except ValueError:
                    print("密码必须是数字")
            
            # 也是退出整个程序的代码
            elif xuan_zhi == "3":
                print(f"\n再见,{shu_ju[cun_chu_dang_qian_deng_lu_yong_hu]['外号']}！欢迎下次回来！")
                break
            
            # 用户没有按要求输入（选项就会执行）
            else:
                print("无效选择，请输入 1-3 之间的数字！")

if __name__ == "__main__":
    zhang_hao_he_mi_ma()