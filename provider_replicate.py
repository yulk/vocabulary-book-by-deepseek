import time
import json
import sys
import os
import replicate
import logging


DEPLOYMENT_NAME = "black-forest-labs/flux-schnell",

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s'
)

model_styles = {
    "NoStyle": "(No style)",
    "Cinematic": "Cinematic",
    "DisneyCharactor": "Disney Charactor",
    "DigitalArt": "Digital Art",
    "PhotographicDefault": "Photographic (Default)",
    "FantasyArt": "Fantasy art",
    "Neonpunk": "Neonpunk",
    "Enhance": "Enhance",
    "Comicbook": "Comic book",
    "Lowpoly": "Lowpoly",
    "Lineart": "Line art"
}

class Model():
    def __init__(self, deployment_name=DEPLOYMENT_NAME, debug=False):
        self._deployment = replicate.deployments.get(deployment_name)
        self._deployment_name = deployment_name
        self._debug = debug
        
    def get_deployment_name(self):
        return self._deployment_name
    
    def predict(self, image, prompt, style, neg_prompt):
        if self._debug == True:
            return ['https://www.nxiaozhi.com/tmp/data/test-imgs/101.jpg'], 0, None
        
        logging.info(f"start to predict {image} {prompt} {style} {neg_prompt}")
        start_time = time.time()
        prediction = self._deployment.predictions.create(
            input={
                "prompt": "black forest gateau cake spelling out the words \"FLUX SCHNELL\", tasty, food photography, dynamic shot",
                "go_fast": True,
                "megapixels": "1",
                "num_outputs": 1,
                "aspect_ratio": "1:1",
                "output_format": "webp",
                "output_quality": 80,
                "num_inference_steps": 4
            }
        )
        prediction.wait()
        cost_second = int(time.time() - start_time)
        print(f"cost time: {cost_second}s")
        print(prediction)
        return prediction.output, cost_second, prediction

                
def main():
    model = Model()
    model.predict("https://www.nxiaozhi.com/tmp/data/test-imgs/101.jpg", "a photo of a cat", "NoStyle", "")

if __name__ == "__main__":
    main()
