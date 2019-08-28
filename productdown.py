import fileinput

num = 0
d = {}
for line in fileinput.input("no1010path_201905"):
    # android
    if "android" in line:
        # 包含购物车
        if "1023~6000" in line:
            index = line.rindex("~6000")
            index2 = line.rindex("~页面曝光)")
            key = line[index - 4:index2]
            print(key)
            if key in d:
                d[key] = d.get(key) + 1
            else:
                d[key] = 1
print("-----------------------")
for key in d.keys():
    print(key)
print("-----------------------")
for value in d.values():
    print(value)