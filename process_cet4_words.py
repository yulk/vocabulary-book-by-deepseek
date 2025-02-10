import os
import sys
import json
from provider_siliconflow import call_siliconflow_chat

word_system_prompt = """
# 角色

你是一名中英文双语教育专家，拥有帮助将中文视为母语的用户理解和记忆英语单词的专长，请根据用户提供的英语单词完成下列任务。

## 任务

### 分析词义

- 系统地分析用户提供的英文单词，并以简单易懂的方式解答；

### 列举例句

- 根据所需，为该单词提供至少 3 个不同场景下的使用方法和例句。并且附上中文翻译，以帮助用户更深入地理解单词意义。

### 词根分析

- 分析并展示单词的词根；
- 列出由词根衍生出来的其他单词；

### 词缀分析

- 分析并展示单词的词缀，例如：单词 individual，前缀 in- 表示否定，-divid- 是词根，-u- 是中缀，用于连接和辅助发音，-al 是后缀，表示形容词；
- 列出相同词缀的的其他单词；

### 发展历史和文化背景

- 详细介绍单词的造词来源和发展历史，以及在欧美文化中的内涵

### 单词变形

- 列出单词对应的名词、单复数、动词、不同时态、形容词、副词等的变形以及对应的中文翻译。
- 列出单词对应的固定搭配、组词以及对应的中文翻译。

### 记忆辅助

- 提供一些高效的记忆技巧和窍门，以更好地记住英文单词。

### 小故事

- 用英文撰写一个有画面感的场景故事，包含用户提供的单词。
- 要求使用简单的词汇，100 个单词以内。
- 英文故事后面附带对应的中文翻译。
"""
word_draw_system = "You are a helpful assistant designed to output JSON."
word_draw_prompt = """
根据以下对单词 "{word}" 的定义和示例，创建一个用于生成有助于记忆该单词的prompt。
```
{word}	 {mean}
```

这个prompt必须仅使用视觉线索来生成图像，因此请专注于独特的、易于与单词含义相关联的事物。
你可以忽略不太重要或难以想象的定义，并添加一些单字特征描述场景和图片风格的视觉外观。保持简洁准确的同时坚持完整的句子。解释你的答案并只生成一个prompt。以以下JSON格式提供你的回答(使用单引号在JSON值中，explanation字段的值用中文，prompt字段的值用英文):
```json
{json_format}
```

"""


word_draw_json_format = """
{
    "explanation": "explain why proposed prompt is suitable for remembering the word '%s'",
    "prompt": "your prompt here",
}
"""



def process_word(word, word_mean):
    #print(word_draw_prompt.format(word=word, mean=word_mean, json_format=word_draw_json_format % word))
    #sys.exit()
    res_text = call_siliconflow_chat(word, system=word_system_prompt)
    while res_text == None:
        print(f"ERROR:  res_text({word}) is None, retrying...")
        res_text = call_siliconflow_chat(word, system=word_system_prompt)

    while True:  
        draw_res_text = call_siliconflow_chat(word_draw_prompt.format(word=word, mean=word_mean, json_format=word_draw_json_format % word), system=word_draw_system, format="json_object")
        if draw_res_text == None:
            print(f"ERROR:  draw_res_text({word}) is None, retrying...")
            continue
        try:
            draw_res = json.loads(draw_res_text)
            return res_text, draw_res['explanation'] , draw_res['prompt']
        except Exception as e:
            print(f"ERROR:  draw_res_text({word}) is not valid json, retrying...")
            continue
    
    return None, None, None

def main():
    # 确保结果目录存在
    result_dir = os.path.join(os.getcwd(), 'result', 'cet4')
    if not os.path.exists(result_dir):
        os.makedirs(result_dir, exist_ok=True)
    
    data_dir = os.path.join(os.getcwd(), 'data', 'cet4')
    for filename in os.listdir(data_dir):
        if filename.endswith('.json'):
            # 读取源文件
            word_list_path = os.path.join(data_dir, filename)
            print(f"正在处理文件：{word_list_path}")
            with open(word_list_path, 'r', encoding='utf-8') as f:
                words = json.load(f)
            
            processed_words = []
            for word in words:
                word_name = word['word']
                word_mean = word['mean']
                word_phonetic_symbol = word['phonetic_symbol']
                analysis, draw_explain, draw_prompt = process_word(word_name, word_mean)
               
                processed_words.append({
                    "word": word_name,
                    "analysis": analysis,
                    "draw_explain": draw_explain,
                    "draw_prompt": draw_prompt
                })

                if len(processed_words) >=2:
                    break
            
                
            
            # 保存结果到对应字母目录
            result_path = os.path.join(result_dir, filename)
            with open(result_path, 'w', encoding='utf-8') as f:
                json.dump(processed_words, f, ensure_ascii=False, indent=2)
            print(f"处理完成：{result_path}")
    
    print("处理完成！")

if __name__ == "__main__":
    main()
