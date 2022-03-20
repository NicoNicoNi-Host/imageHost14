#!/bin/zsh

# 将剪切板内容输出到文件
pbpaste > /Users/andrew/Downloads/Downie下载/1.txt

# 提取匹配行
sed -r -n -e '/forum|3D580/p' /Users/andrew/Downloads/Downie下载/1.txt > /Users/andrew/Downloads/Downie下载/2.txt
# 正则表达式
python /Users/andrew/Downloads/Downie下载/1.py > /Users/andrew/Downloads/Downie下载/3.txt

# 将文件内容复制到剪切板
pbcopy < /Users/andrew/Downloads/Downie下载/3.txt