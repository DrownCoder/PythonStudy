# -*- coding: UTF-8 -*-
f = open("un1713_android_19")  # 返回一个文件对象
starIndex = len('2b332696ca23369a4e528f1a3555a87e') + 1


# 统计路径长度
def sizeOfPath(userPath):
    return userPath.count('->')


line = f.readline()  # 调用文件的 readline()方法
count = 0
printCount = 0
while line:
    line = str(f.readline())[starIndex:]
    pathSize = sizeOfPath(line)
    if pathSize <= 6:
        # print(line)
        count = count+1
    # if printCount > 10:
    #     break
    printCount = printCount+1

print(count)
f.close()
