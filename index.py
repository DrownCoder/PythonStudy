# -*- coding: UTF-8 -*-
f = open("un1713_android_17")  # 返回一个文件对象
starIndex = len('2b332696ca23369a4e528f1a3555a87e') + 1


# 统计路径长度
def sizeOfPath(userPath):
    return userPath.count('->')


line = f.readline()  # 调用文件的 readline()方法
count = 0
printCount = 0
while line:
    line = str(f.readline())[starIndex:]
    if '1842~4200' in line and '2002' not in line:
    	count = count + 1
    printCount = printCount+1

print(count)
f.close()
