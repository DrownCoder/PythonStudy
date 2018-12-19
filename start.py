# -*- coding: UTF-8 -*-
fileArr = ["un1713_android_17", "un1713_android_18", "un1713_android_19", "un1713_android_21"]


def printFile(fileTemp):
    f = open(fileTemp)  # 返回一个文件对象
    starIndex = len('2b332696ca23369a4e528f1a3555a87e') + 1
    line = f.readline()  # 调用文件的 readline()方法
    count = 0
    printCount = 0
    while line:
        line = str(f.readline())[starIndex:]
        if not line.startswith('3998~9995'):
            # print(line)
            count = count + 1

    print(count)
    f.close()


for fileName in fileArr:
	# print(fileName)
    printFile(fileName)
