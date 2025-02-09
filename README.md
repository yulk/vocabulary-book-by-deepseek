# vocabulary-book-by-deepseek

## 需求

用 Python 写一个 cet4 单词助记工具，对单词进行词义词根分析、例举例句、并提供一些高效的记忆技巧和窍门。 详细需求如下：
1、 单词已经按照字母归类存储在data/cet4/目录下，分别为： A.json B.json ... Z.json
2、 读取每一个 data/cet4/目录下 每个JSON文件中的所有单词，对每个单词调用OpenAI的接口生成该单词的词义、词根、例句、记忆技巧信息。
3、 生成的单词信息保存到 result/cet4/目录下，分别为： A.json B.json ... Z.json