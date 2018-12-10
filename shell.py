import os

str = os.popen("git branch -a").read()
print(str)
