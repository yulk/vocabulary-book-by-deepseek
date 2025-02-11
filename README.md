# vocabulary-book-by-deepseek

## Run

```
./prun.sh process_cet4_words.py
```

## 需求

### Task1
用 Python 写一个 cet4 单词助记工具，对单词进行词义词根分析、例举例句、并提供一些高效的记忆技巧和窍门。 详细需求如下：
1、 单词已经按照字母归类存储在data/cet4/目录下，分别为： A.json B.json ... Z.json
2、 读取每一个 data/cet4/目录下 每个JSON文件中的所有单词，对每个单词调用OpenAI的接口生成该单词的词义、词根、例句、记忆技巧信息。
3、 生成的单词信息保存到 result/cet4/目录下，分别为： A.json B.json ... Z.json

### Task2
用 Python 写一个 cet4 单词助记图片生成工具， 详细需求如下：
1、 读取每一个 data/cet4/目录下 每个JSON文件中的所有单词，对每个单词调用replicate的接口(接口具体实现在provider_replicate.py:replicate_run)生成该单词的图片。
2、 生成的图片文件保存到 result/cet4_imgs/目录下，文件名称格式为：{first_letter_of_word}/{word}.jpg。如果对应图片文件已存在，则跳过本图片文件的生成。
