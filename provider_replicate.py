import time
import json
import sys
import os
import replicate
import logging


DEPLOYMENT_NAME = "black-forest-labs/flux-schnell"

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s'
)
    
def replicate_run( prompt):
    logging.info(f"start to predict:  {prompt}")
    start_time = time.time()
    output = replicate.run(
        DEPLOYMENT_NAME,
        input={
            "prompt": prompt,
            "go_fast": True,
            "megapixels": "1",
            "num_outputs": 1,
            "aspect_ratio": "16:9",
            "output_format": "jpg",
            "output_quality": 80,
            "num_inference_steps": 4
        }
    )
    cost_second = int(time.time() - start_time)
    print(f"cost time: {cost_second}s")
    return output, cost_second


if __name__ == "__main__":
    output, cost_second = replicate_run( "a photo of a cat")
        # Save the generated image
    with open('./tmp/output.png', 'wb') as f:
        f.write(output[0].read())
    
    print(f"Image saved as output.png")
