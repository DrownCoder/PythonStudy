import fileinput
# 没有进单品页的购物车路径，下一级页面
num = 0
d = {}
for line in fileinput.input("no1010path_201908"):
    # android
    if "android" in line:
        # 包含购物车
        index = line.find("1023~6000(购物车页~页面曝光)->")
        if index != -1:
            key = line[index + 22:index + 26]
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
