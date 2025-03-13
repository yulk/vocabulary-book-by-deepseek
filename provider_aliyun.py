import time
import json
import sys
import os
import logging

# API参考：https://bailian.console.aliyun.com/?spm=5176.29597918.J__Xz0dtrgG-8e2H7vxPlPy.8.67b67ca0NBXQtk&accounttraceid=17e5111bcf0b4c2cb0df6a86d3056ef5pgnf#/model-market/detail/flux-schnell?tabKey=sdk


MODEL_NAME = "flux-schnell"

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s'
)

from http import HTTPStatus
from urllib.parse import urlparse, unquote
from pathlib import PurePosixPath
import requests
from dashscope import ImageSynthesis

model = "flux-schnell"
prompt = "Eagle flying freely in the blue sky and white clouds"

def image_gen(input_prompt, dst_path):
    if not dst_path.endswith('.png'):
        raise ValueError("Only support .png file")
    dst_dir = os.path.dirname(dst_path)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    rsp = ImageSynthesis.call(model=model,
                              prompt=input_prompt,
                              size='1024*576',
                              steps=4)
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output)
        print(rsp.usage)
        # save file to current directory
        for result in rsp.output.results:
            #file_name = PurePosixPath(unquote(urlparse(result.url).path)).parts[-1]
            with open(dst_path, 'wb+') as f:
                f.write(requests.get(result.url).content)
                break
        return rsp.output, rsp.usage
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))
        return None, None


def image_async_gen(input_prompt):
    rsp = ImageSynthesis.async_call(model=model,
                                    prompt=input_prompt,
                                    size='1024*1024')
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output)
        print(rsp.usage)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))
    status = ImageSynthesis.fetch(rsp)
    if status.status_code == HTTPStatus.OK:
        print(status.output.task_status)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (status.status_code, status.code, status.message))

    rsp = ImageSynthesis.wait(rsp)
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))


if __name__ == '__main__':
    image_gen(prompt, "./tmp/output.png")
    #image_async_gen(prompt)