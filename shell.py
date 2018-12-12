import os
print("输入排除的分支名：（【空格隔开】默认排除mastar和remote）")
exceptBranch = input()
exceptBranchs = exceptBranch.split(" ")
exceptBranchs.append("master")
branchSource = os.popen("git branch -a").read()
branchs = branchSource.split("\n")
for branch in branchs:
    if "remotes" not in branch :
        for exceptItem in exceptBranchs:
            if branch not in exceptItem:
                print("git branch -d "+branch)
                result = os.popen("git branch -d"+branch)
