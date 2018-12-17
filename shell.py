# -*- coding: UTF-8 -*-
import os

print("输入排除的分支名：（【空格隔开】默认排除mastar和remote）")
exceptBranch = input()
exceptBranchs = []
if len(str(exceptBranch).strip()) > 0:
    exceptBranchs = exceptBranch.split(" ")


# 判断是否需要排除这个分支
def showExcept(branchTemp):
    if "remotes" in branchTemp:
        return True
    elif "master" == str(branchTemp).strip():
        return True
    else:
        if len(exceptBranchs) > 0:
            for exceptItem in exceptBranchs:
                if exceptItem in branchTemp:
                    return True
    return False
    pass


# 删除分支
def deleteBranch():
    branchSource = os.popen("git branch -a").read()
    branchs = branchSource.split("\n")
    for branch in branchs:
        if not showExcept(branch):
            print("git branch -d" + branch)
            os.popen("git branch -D " + str(branch).strip())


deleteBranch()
path = os.popen("ls").read()
projectPaths = path.split("\n")
for project in projectPaths:
    print("清理" + project + "目录下的分支...")
    os.popen("cd " + project)
    deleteBranch()
    print("清理完成")
    os.popen("cd..")
