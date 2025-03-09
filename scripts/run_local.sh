#!/bin/bash

mkdir -p web/imgs/word_imgs/ && cp -r result/word_imgs/* web/imgs/word_imgs/ && cp -r imgs/*.png web/imgs/
cp -r result/articles/* web/_posts/zh/
docker run -it --rm -p 4000:4000 -v $PWD/web:/app -w /app ruby:3.2.0 bash