# coding=utf8
# 上述标签定义了本文档的编码，与Python 2.x兼容。

import re


# 读文件   把文件全部内容一次性读到一个字符串中。
# with open('filepath','r') as f:
#     ff=f.read()

# 读取2.txt文件的全部内容赋值为test_str
with open('/Users/andrew/Downloads/Downie下载/2.txt','r') as f:
    test_str=f.read()

# 一行有多张图片时,换行
regex = r"\)!\[\]\("
subst = ")\\n![]("
# 您可以通过改变第4个参数来手动指定替换的数量
test_str = re.sub(regex, subst, test_str, 0, re.MULTILINE)

# 文本替换-使用捕获组
regex = r"(.+)w\%3D580\/sign(.+?)\/(.+)"
subst = "\\g<1>pic/item/\\g<3>\\n"
# 您可以通过改变第4个参数来手动指定替换的数量
result = re.sub(regex, subst, test_str, 0, re.MULTILINE)
if result:
    print (result)

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.