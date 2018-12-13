import os

print("输入排除的分支名：（【空格隔开】默认排除mastar和remote）")
exceptBranch = input()
exceptBranchs = exceptBranch.split(" ")
exceptBranchs.append("master")
branchSource = os.popen("git branch -a").read()
branchs = branchSource.split("\n")


# 判断是否需要排除这个分支
def showExcept(branchTemp):
    if "remotes" in branchTemp:
        return True
    else:
        for exceptItem in exceptBranchs:
            if exceptItem in branchTemp:
                return True
    return False

    pass


for branch in branchs:
    if not showExcept(branch):
        os.popen("git branch -d" + branch)
