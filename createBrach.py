import os

for i in range(0, 5):
    os.popen("git checkout -b create" + str(i))

print(os.popen("git branch -a").read())
