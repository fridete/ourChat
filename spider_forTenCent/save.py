import os
import datetime
import shutil
base_dir = os.path.dirname(__file__)   # 获取当前文件目录
outfile1 = 'downloads'
outfile2 ='temporary_file'
path = os.path.join(base_dir, outfile1) # path是需要把文件复制到的指定位置
# 我这儿达到的目的是：在py脚本的文件夹下新建try_file文件夹，并把图片改名保存到try_file文件下
# path也可以写成
# path = r'D:\try_file'
old_path=os.path.join(base_dir, outfile2)
date_now = datetime.date.today()

if os.path.exists(path):
    pass
else:
    os.mkdir(path)
    #if mod==1
origin_path = old_path+"\\"+input("请输入文件名：")    # 原始文件完整目录
#else 
new_file_name = r'%s\\%s_%s_%s_.mp4' % (path,"my", "视频", date_now)  # 文件新名字
print("是否修改名字？")
answer=input("y or n: ")
if answer=='y':
    new_name=input("请输入新名称: ")
    new_file_name=path+"\\"+new_name
    print("已完成")
else:
    print("已完成")    
shutil.copyfile(origin_path, new_file_name)