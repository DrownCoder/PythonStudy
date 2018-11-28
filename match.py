import re

file = open("Action.java")
resultFile = open("Result.java", 'w')
line = file.readline()
count = 0
while line:
    matchObj = re.match(r'[\D]*[a-z]*[_][a-z]*[://]', line)
    if matchObj:
        # count = count+1
        # print(line)
        resultFile.writelines(line)
    line = file.readline()
print(count)
file.close()
resultFile.close()
