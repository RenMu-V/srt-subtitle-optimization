import os
import re
from tqdm import tqdm

def replace_punctuation_with_spaces(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 遍历每一行，替换行中的中英文逗号和句号，并删除冒号及其前的所有文字，删除方括号及其内容，删除*符号，删除♪符号，删除破折号-，以及删除括号及其内容
    for i in range(len(lines)):
        # 判断是否为时间戳行，如果是则跳过
        if re.match(r'\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+', lines[i]):
            continue
        # 替换中英文逗号和句号为空格
        lines[i] = re.sub(r'[，,。.]', ' ', lines[i])
        # 删除冒号及其前的所有文字
        lines[i] = re.sub(r'.*?：', '', lines[i])
        # 删除方括号及其内容
        lines[i] = re.sub(r'\[.*?\]', '', lines[i])
        # 删除*符号
        lines[i] = re.sub(r'\*', '', lines[i])
        # 判断行中是否只有♪符号，如果是则删除该行
        if re.match(r'^\s*♪\s*$', lines[i]):
            lines[i] = ''
        # 判断♪符号中间或者后面是否有文字，如果有则不删除♪符号
        elif re.search(r'♪\s*\S', lines[i]):
            lines[i] = re.sub(r'♪', '', lines[i])
        # 删除破折号-
        lines[i] = re.sub(r'-', '', lines[i])
        # 删除括号及其内容
        lines[i] = re.sub(r'[\(\（].*?[\)\）]', '', lines[i])

    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def batch_replace_punctuation_with_spaces():
    # 获取当前目录下的所有SRT文件
    srt_files = [file for file in os.listdir() if file.endswith('.srt')]

    # 遍历每个SRT文件并进行替换
    for file in tqdm(srt_files, desc="进度", unit="文件"):
        replace_punctuation_with_spaces(file)

    print("标点替换、冒号及其前文字删除、方括号删除、*符号删除、♪符号删除、破折号-删除和括号删除完成！")

# 执行批量替换
batch_replace_punctuation_with_spaces()
