import os
import json
import logging
from typing import List, Dict

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s'
)

def get_word_files() -> List[str]:
    word_dir = os.path.join("result", "cet4")
    if not os.path.exists(word_dir):
        raise FileNotFoundError(f"Directory {word_dir} not found.")
    
    file_list: List[str] = []
    for filename in os.listdir(word_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(word_dir, filename)
            file_list.append(file_path)
    return file_list

def process_word_file(file_path: str) -> None:
    with open(file_path, "r", encoding="utf-8") as f:
        data_words = json.load(f)
    
    for word_info in data_words:
        word = word_info.get("word")
        if not word:
            continue
        
        first_letter = word[0].lower()
        img_dir = os.path.join("result", "cet4_imgs", first_letter)
        
        # 确保目录存在
        if not os.path.exists(img_dir):
            os.makedirs(img_dir, exist_ok=True)
        
        img_path = os.path.join(img_dir, f"{word}.jpg")
        
        # 检查文件是否存在
        if os.path.exists(img_path):
            logging.info(f"Skipping {word} as image already exists.")
            continue
        
        # 调用replicate接口生成图片
        from provider_replicate import replicate_run
        try:
            output, cost_second = replicate_run(word_info["draw_prompt"])
            if not output:
                raise ValueError("Failed to generate image")
            
            with open(img_path, "wb") as f:
                f.write(output[0].read())
            logging.info(f"Generated image for {word} saved at {img_path}")
        except Exception as e:
            logging.error(f"Error generating image for {word}: {str(e)}")

def main() -> None:
    word_files = get_word_files()
    if not word_files:
        logging.error("No JSON files found in result/cet4/")
        return
    
    for file_path in word_files:
        logging.info(f"Processing file: {file_path}")
        process_word_file(file_path)
    
if __name__ == "__main__":
    main()
