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
            logging.error(f"word field not found in {word_info}")
            continue
        
        first_letter = word[0].lower()
        #if first_letter != "b":
        #    continue
        img_dir = os.path.join("result", "word_imgs", first_letter)
        
        # 确保目录存在
        if not os.path.exists(img_dir):
            os.makedirs(img_dir, exist_ok=True)
        
        img_file_without_ext = f"{word}" if word[0].islower() else f"{word}2"
        img_path_png = os.path.join(img_dir, img_file_without_ext) + ".png"
        img_path_jpg = os.path.join(img_dir, img_file_without_ext) + ".jpg"
        
        # 检查文件是否存在
        if os.path.exists(img_path_png) or os.path.exists(img_path_jpg):
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
        provider = os.environ.get("IMAGE_PROVIDER", "replicate")
        logging.info(f"Generating image for {word} using {provider}")
        
        if provider == "replicate":
            from provider_replicate import image_gen
        elif provider == "dashscope":
            from provider_aliyun import image_gen
        else:
            logging.error(f"Unknown provider: {provider}")
            raise ValueError(f"Unknown provider: {provider}")

        try:
            output, cost = image_gen(word_ana["draw_prompt"], img_path_png)
            if not output:
                raise ValueError("Failed to generate image")
            
            logging.info(f"Generated image for {word} saved at {img_path_png}")
        except Exception as e:
            logging.error(f"Error generating image for {word}: {str(e)}")

def main() -> None:
    process_word_file("data/all/global-words.json")
    
if __name__ == "__main__":
    main()
