import datetime

# 类 ：个人日记本
class Ge_Ren_Ri_Ji_Ben:

    # 初始化方法 创建日记本实例
    def __init__(self,wen_jian_wen_ben="D:\VS py测试\VS文本文件\Git_ge_ren_ri_ji_ben.txt"):
        """参数:wen_jian_wen_ben 日记存储的文件名 "D:\VS py测试\VS文本文件\Git_ge_ren_ri_ji_ben.txt"""

        # 将文件保存为实例变量 方便其他使用
        self.wen_jian_wen_ben = wen_jian_wen_ben

    """添加进日记到文件 参数：xin_ri_ji 用户输入的日记内容"""
    def append_ri_ji(self,xin_ri_ji):

        # 获取当前日期的时间
        huo_qu_shi_jian = datetime.datetime.now()

        # 将（日期和时间）格式化 为易读的字符串
        ge_shi_hua = huo_qu_shi_jian.strftime("%Y/%m/%d %H:%M:%S")

        # 追加模式打开文件
        with open(self.wen_jian_wen_ben,"a" ,encoding="utf-8") as f:

            # 将格式化后的时间和日记内容写入文件，换行
            f.write(f"{ge_shi_hua} --- {xin_ri_ji}\n")

        """提示保存成功"""
        print("日记保存成功")

    # 读取并显示所有的日记内容
    def xin_append_suo_you_ri_qi(self):

        # 如果文件不存在 提示：还没有日记
        try:
            # 读取模式打开文件
            with open(self.wen_jian_wen_ben, "r", encoding="utf-8") as f1:

                # 读取文件的全部内容
                du_qu = f1.read()

                """检查内容是否为空 （去除首尾空白字符）"""
                if du_qu.strip():
                    # 显示分隔线和标题
                    print("=" * 30 ,"所有日记", "=" * 30)

                    """显示文件重全部日记内容"""
                    print(f"文件内容：{du_qu}")

                else:
                    # 如果文件存在但是内容为空 提示语
                    print("还没有日记")

            """如果文件不存在 捕获异常并提示"""
        except  FileNotFoundError:
            print("还没有日记")
            
    def huo_qu_ri_ji_zong_shu(self):
        """获取日记总数"""
        try:
            with open(self.wen_jian_wen_ben, 'r', encoding='utf-8') as f:
                return len(f.readlines())
        except FileNotFoundError:
            return 0

    def qing_kong_suo_you_ri_ji(self):
        """清空所有日记（谨慎使用）"""
        confirm = input("确定要清空所有日记吗？(y/n): ")
        if confirm.lower() == 'y':
            with open(self.wen_jian_wen_ben, 'w', encoding='utf-8') as f:
                f.write("")
            print("所有日记已清空")        

    def xiao_shi_cai_dan(self):

        """显示菜单"""
        while True:
            try:
                """显示菜单标题和选项"""
                print("=" * 20 ,"个人日记", "=" * 20)
                print("1.写新日记")
                print("2.查看日记")
                print("3.查看日记总数")  
                print("4.清空所有日记")
                print("5.退出")  

                print("=" * 30)

                # 输入转换为 整数
                yong_hu = int(input("请选择："))

                # 选择执行相应的操作
                if yong_hu == 1:

                    """获取日记内容并调用添加的方法"""
                    ri_ji_nei_rong = input("请输入日记内容:")
                    self.append_ri_ji(ri_ji_nei_rong)

                elif yong_hu == 2:
                    """调用方法显示所用日记"""
                    self.xin_append_suo_you_ri_qi()

                elif yong_hu == 3:  # 查看日记总数
                    zong_shu = self.huo_qu_ri_ji_zong_shu()
                    print(f"当前共有 {zong_shu} 篇日记")
                elif yong_hu == 4:  # 清空日记
                    self.qing_kong_suo_you_ri_ji()
                elif yong_hu == 5:  # 退出
                    print("下次再见")
                    break
                
                # 处理无效数字
                else:
                    print("无效选择 请输入1-3选项")
            # 处理非数字
            except ValueError:
                print("请输入数字")

if __name__ == "__main__":
    diao_yong = Ge_Ren_Ri_Ji_Ben()  # 创建日记本实例
    diao_yong.xiao_shi_cai_dan()    # 启动菜单
