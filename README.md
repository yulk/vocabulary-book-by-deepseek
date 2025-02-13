# vocabulary-book-by-deepseek

使用 DeepSeek 开发实现的四级单词词汇库， 提供单词的词义、词根、例句、辅助记忆、助记图像等信息。

本项目 80% 以上代码采用 Cline + DeepSeek-R1-16b(本地部署) 自动编码完成。

## Run

**串行处理**
```
./prun.sh process_cet4_words.py
```

**只处理一个文件**
```
./prun.sh process_cet4_words.py A.json
```

**并发处理所有文件**

```bash
for letter in {A..Z}; do 
    ./prun.sh process_cet4_words.py ${letter}.json &
    sleep 10
done
```

## 需求

Cline 提示次如下：

### Task1

```
用 Python 写一个 cet4 单词助记工具，对单词进行词义词根分析、例举例句、并提供一些高效的记忆技巧和窍门。 详细需求如下：
1. 单词已经按照字母归类存储在data/cet4/目录下，分别为： A.json B.json ... Z.json
2. 读取每一个 data/cet4/目录下 每个JSON文件中的所有单词，对每个单词调用OpenAI的接口生成该单词的词义、词根、例句、记忆技巧信息。
3. 生成的单词信息保存到 result/cet4/目录下，分别为： A.json B.json ... Z.json
```

### Task2

```
用 Python3.8 写一个单词助记图片生成工具gen_words_img.py， 详细需求如下：
1. 读取每一个 result/cet4/目录下 每个JSON文件中的所有单词信息，每个单词信息包括word、analysis、draw_explain、draw_prompt 4个字段。
2. 对每个单词调用replicate的接口(接口具体实现在provider_replicate.py:replicate_run)生成该单词的图片。
3. 生成的图片文件保存到 result/cet4_imgs/目录下，文件名称格式为：{first_letter_of_word}/{word}.jpg。如果对应图片文件已存在，则跳过本图片文件的生成。
4. 假设所有依赖库已经安装。
```

### Task3

```
用 Python3.8 写一个文章生成工具gen_articles.py， 为26个英文字母各生成一个文件，共26个文件，文件名格式为：2025-02-11-cet4-{letter}.md, 每个文件的内容组成如下：
"""
---
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

{{ for all word begin with letter}}
## word
{word.analysis}
{{end}}
"""

其中 word.analysis 通过读取 result/cet4/{letter}.json 获得，result/cet4/{letter}.json存储了{letter}开头的全部单词的信息，如果result/cet4/{letter}.json 不存在，则跳过该letter对应文件的生成。

更多约束如下：
1、2025-02-11-cet4-{letter}.md 保存到 result/cet4_articles 目录下。
2、Python 使用 3.8 版本。
3、假设所有Python依赖库已经安装。
```

