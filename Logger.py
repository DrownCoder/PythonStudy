f = open("foo.txt")               # 返回一个文件对象
line = f.readline()               # 调用文件的 readline()方法
while line:
    line = f.readline()
    print(line)

f.close()