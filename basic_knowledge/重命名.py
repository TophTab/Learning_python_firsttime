import os

#查找文件
path="E:\code"
#os.listdir()方法，列出来所有文件
#返回path指定的文件夹包含的文件或文件夹的名字的列表
files=os.listdir(path)

#主逻辑
#对于批量的操作，使用FOR循环
for f in files:
    #调试代码的方法：关键地方打上print语句，判断这一步是不是执行成功
    if f.count('.')>2 and f.endswith(".py"):
        old_file=os.path.join(path,f)
        print("old_file is {}".format(old_file))
        #指定新文件的位置，如果没有使用这个方法，则新文件名生成在本项目的目录中
        new_name=old_file.replace(".","_")
        new_name=new_name.replace("_py",".py")
        print(new_name)
        new_file=os.path.join(path,new_name)
        print("File will be renamed as:{}".format(new_file))
        os.rename(old_file,new_file)