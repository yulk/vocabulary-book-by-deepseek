import os
import json
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s'
)

# 确定CET4单词数据的路径
word_data_path = 'data/all/global-words.json'
word_analysis_dir = 'result/all'
article_dir = 'result/articles'


def gen_letter_article_content(letter, words_data_map, letter_words, subdir, title_tag):
 # 准备Markdown内容
    content = f"""---
layout:     post
title:      "{title_tag}-{letter}开头单词"
subtitle:   "{title_tag}-{letter}开头单词"
date:       2025-02-11
author:     "vxiaozhi"
catalog: true
tags:
    - 英语词汇
    - {title_tag}
---
    """
    content += "\n## 索引\n\n"
    for le in [chr(ord('a') + i) for i in range(26)]:
        title = f"**{title_tag}-{le}开头单词**" if le == letter else f"{title_tag}-{le}开头单词"
        content += f"- [{title}](/2025/02/11/{subdir}-{le}/)\n"
    content += "\n"

    for i in range(0, len(letter_words)):
        word = letter_words[i]
        word_img_name = f"{word}.jpg" if word[0].islower() else f"{word}2.jpg"
        word_org_data = words_data_map.get(word, None)
        if word_org_data is None:
            logging.error(f"Word not found: {word}")
            continue
        logging.info(f"Processing word: {word}, data: {word_org_data}")
        analysis = word_org_data.get('analysis', '')
        content += f"""## {i+1}. {word}

**释义**：{word_org_data['translations'][0]["translation"]}

{analysis}

### 助记图像

{word_org_data['draw_explain']}

![{word}](/imgs/word_imgs/{letter}/{word_img_name})

"""
    return content
def gen_articles(words_data_map, words_list, subdir, title):
    for letter in [chr(ord('a') + i) for i in range(26)]:
        upper_letter = letter.upper()
        lower_letter = letter.lower()
        letter_words = [word for word in words_list if word[0].lower() == lower_letter]
        # json_path = os.path.join(word_analysis_dir, f'{upper_letter}.json')
       
        content = gen_letter_article_content(letter, words_data_map, letter_words, subdir, title)
        # 生成文件路径
        file_name = f'2025-02-11-{subdir}-{letter}.md'
        dst_dir = os.path.join(article_dir, subdir)
        os.makedirs(dst_dir, exist_ok=True)
        article_path = os.path.join(dst_dir, file_name)
        
        # 写入文件
        with open(article_path, 'w', encoding='utf-8') as f:
            f.write(content)

        logging.info(f'Generate article: {article_path}')

def main():
    # build global words data map
    with open(word_data_path, 'r', encoding='utf-8') as f:
        words_data = json.load(f)
    words_data_map = {}
    for word in words_data["words"]:
       
        # build word analysis data
        first_letter = word['word'][0]
        word_ana_file = f"{word['word']}.json" if first_letter.islower() else f"{word['word']}2.json"
        word_ana_path = os.path.join(word_analysis_dir, first_letter.lower(), word_ana_file)
        if not os.path.exists(word_ana_path):
            logging.error(f"File not found: {word_ana_path}")
            continue

        words_data_map[word['word']] = word
        with open(word_ana_path, "r", encoding="utf-8") as f:
            word_ana = json.load(f)
            words_data_map[word['word']].update(word_ana)
        
    
    #logging.info(f"words_data_map: {words_data_map}")
    all_articles = {
        "junior_words": {"title": "初中词汇", "subdir": "junior"},
        "senior_words": {"title": "高中词汇", "subdir": "senior"},
        "cet4_words": {"title": "四级词汇", "subdir": "cet4"},
        "cet6_words": {"title": "六级词汇", "subdir": "cet6"},
        "postgrad_words": {"title": "考研词汇", "subdir": "postgrad"},
        "toefl_words": {"title": "托福词汇", "subdir": "toefl"}
    }
    for article_name, article_data in all_articles.items():
        gen_articles(words_data_map, words_data[article_name], article_data["subdir"], article_data["title"])

if __name__ == "__main__":
    main()
