import  re

file = open("Action.java")
line = file.readline()
while line:
    if re.match(r'[a-z]*[_][a-z]*[://]', line):
        print(line)
    line = file.readline()
file.close()
