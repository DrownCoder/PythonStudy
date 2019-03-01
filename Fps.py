file = open("test.data")


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


count = 0
kcount = 0
for line in file:
    count = count + 1
    tempLine = line[-4:-1]
    if len(tempLine) > 0:
        if is_number(tempLine) and int(tempLine) > 16:
            kcount = kcount + 1
        print(tempLine)

print(kcount)
print(count)
