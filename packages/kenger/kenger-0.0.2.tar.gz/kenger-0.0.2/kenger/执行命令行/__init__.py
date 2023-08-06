# coding: GB2312
import os, re

# execute command, and return the output
def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text


# 获取计算机MAC地址和IP地址
if __name__ == '__main__':
    cmd = "ifconfig"
    result = execCmd(cmd)
    result = result.split('/n')
    for i in result:
        print(i)