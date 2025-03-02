import os
import json
import logging
from typing import List, Dict

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s'
)
def process_word_file(file_path: str) -> None:
    with open(file_path, "r", encoding="utf-8") as f:
        data_words = json.load(f)["words"]
    
    for word_info in data_words:
        word = word_info.get("word")
        if not word:
            continue
        
        first_letter = word[0].lower()
        #if first_letter != "b":
        #    continue
        img_dir = os.path.join("result", "word_imgs", first_letter)
        
        # 确保目录存在
        if not os.path.exists(img_dir):
            os.makedirs(img_dir, exist_ok=True)
        
        img_file = f"{word}.jpg" if word[0].islower() else f"{word}2.jpg"
        img_path = os.path.join(img_dir, img_file)
        
        # 检查文件是否存在
        if os.path.exists(img_path):
            logging.info(f"Skipping {word} as image already exists.")
            continue

        word_ana_file = f"{word}.json" if word[0].islower() else f"{word}2.json"
        word_ana_path = os.path.join("result", "all", first_letter, word_ana_file)
        if not os.path.exists(word_ana_path):
            logging.error(f"File not found: {word_ana_path}")
            continue

        with open(word_ana_path, "r", encoding="utf-8") as f:
            word_ana = json.load(f)
        
        # 调用replicate接口生成图片
        from provider_replicate import replicate_run
        try:
            output, cost_second = replicate_run(word_ana["draw_prompt"])
            if not output:
                raise ValueError("Failed to generate image")
            
            with open(img_path, "wb") as f:
                f.write(output[0].read())
            logging.info(f"Generated image for {word} saved at {img_path}")
        except Exception as e:
            logging.error(f"Error generating image for {word}: {str(e)}")

def main() -> None:
    process_word_file("data/all/global-words.json")
    
if __name__ == "__main__":
    main()
