import os
import json
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s'
)

# 确定CET4单词数据的路径
word_data_dir = 'data/cet4'
word_analysis_dir = 'result/cet4'
article_dir = 'result/cet4_articles'

for letter in [chr(ord('a') + i) for i in range(26)]:
    upper_letter = letter.upper()
    json_path = os.path.join(word_analysis_dir, f'{upper_letter}.json')
    word_data_path = os.path.join(word_data_dir, f'{upper_letter}.json')

    
    if not os.path.exists(json_path):
        continue
    
    # 读取单词原始数据
    words_data_map = {}
    with open(word_data_path, 'r', encoding='utf-8') as f:
        words_data = json.load(f)
        for word in words_data:
            words_data_map[word['word']] = word
    # 读取单词分析数据
    with open(json_path, 'r', encoding='utf-8') as f:
        words_ana_data = json.load(f)
    
    # 准备Markdown内容
    content = f"""---
layout:     post
title:      "四级词汇-{letter}开头单词"
subtitle:   "四级词汇-{letter}开头单词"
date:       2025-02-11
author:     "vxiaozhi"
catalog: true
tags:
    - english
    - cet4
---
"""
    content += "\n"

    for i in range(0, len(words_ana_data)):
        word = words_ana_data[i]
        word_org_data = words_data_map.get(word['word'], {})
        analysis = word.get('analysis', '')
        content += f"""## {i+1}. {word['word']}

**音标**：{word_org_data['phonetic_symbol']}

**释义**：{word_org_data['mean']}

{analysis}

### 助记图像

{word['draw_explain']}

![{word['word']}](../cet4_imgs/{letter}/{word['word']}.jpg)

"""

    # 生成文件路径
    file_name = f'2025-02-11-cet4-{letter}.md'
    article_path = os.path.join(article_dir, file_name)
    
    # 写入文件
    with open(article_path, 'w', encoding='utf-8') as f:
        f.write(content)

    logging.info(f'Generate article: {article_path}')
