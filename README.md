# vocabulary-book-by-deepseek

使用 DeepSeek 开发实现的四六级、考研、托福 单词词库手册， 提供单词的词义、词根、例句、辅助记忆、助记图像等信息。

本项目 80% 以上代码采用 Cline + DeepSeek-R1-16b(本地部署) 自动编码完成。

生成的词库手册最终效果如下：

- [四级词汇-a开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-a/)
- [四级词汇-b开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-b/)
- [四级词汇-c开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-c/)
- [四级词汇-d开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-d/)
- [四级词汇-e开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-e/)
- [四级词汇-f开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-f/)
- [四级词汇-g开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-g/)
- [四级词汇-h开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-h/)
- [四级词汇-i开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-i/)
- [四级词汇-j开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-j/)
- [四级词汇-k开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-k/)
- [四级词汇-l开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-l/)
- [四级词汇-m开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-m/)
- [四级词汇-n开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-n/)
- [四级词汇-o开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-o/)
- [四级词汇-p开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-p/)
- [四级词汇-q开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-q/)
- [四级词汇-r开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-r/)
- [四级词汇-s开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-s/)
- [四级词汇-t开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-t/)
- [四级词汇-u开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-u/)
- [四级词汇-v开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-v/)
- [四级词汇-w开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-w/)
- [四级词汇-x开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-x/)
- [四级词汇-y开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-y/)
- [四级词汇-z开头单词](https://www.vxiaozhi.com/2025/02/11/cet4-z/)


## 功能规划

- ✅ 英语四级词库
- 英语六级词库
- 考研
- 托福
- anki卡片

## Run

**cet4 原始单词数据路径：**

```
data/cet4/
```

**调用DeepSeek生成单词解释信息**

- 串行处理

```
./prun.sh process_cet4_words.py
```

- 只处理一个文件

```
./prun.sh process_cet4_words.py A.json
```

- 并发处理所有文件

```bash
for letter in {A..Z}; do 
    ./prun.sh process_cet4_words.py ${letter}.json &
    sleep 10
done
```

**生成每个单词的助记图像**

```
./prun.sh gen_words_img.py
```

**生成文章**

```
./prun.sh gen_articles.py
```

## Cline任务

本项目 80% 以上代码采用 Cline + DeepSeek-R1-16b(本地部署) 自动编码完成。

-  [Cline 任务提示词记录在此](docs/cline_tasks.md)

## 数据来源

- [四级单词库](https://github.com/cuttlin/Vocabulary-of-CET-4)
- [六级单词库](https://github.com/KyleBing/english-vocabulary)

## 赞赏

作为一个独立开发者，除了日常的代码开发工作外，项目运行所需的各项成本（包括调用大模型的费用）均由我个人承担。

如果您觉得我的项目对您有所帮助，请通过下方式支持我：

- **捐赠支持：** 若有意向提供捐助，感谢您的鼓励与支持！
- **扫码交流群：** 欢迎加入我们的讨论社群，共同探讨如何更高效地学习英语、记忆单词，以及AI在语言学习中的应用。


|![mp](imgs/mp.png)|![赞赏](imgs/qr.png)|
|:-:|:-:|
|后台回复 `AI助记` 加群交流|捐赠支持作者|

