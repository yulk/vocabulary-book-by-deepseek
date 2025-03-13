#!/bin/bash

PNG_FILES=`find ./result/word_imgs -name "*.png"`
for file in $PNG_FILES
do
  convert $file -background white -quality 85 -flatten ${file}.tmp.jpg
  convert ${file}.tmp.jpg -font Arial -pointsize 28 -fill "rgba(255,0,255,0.5)" -gravity southeast -annotate +20+10 "word.vxiaozhi.com" ${file%.png}.jpg
done

#find ./result/word_imgs -name "*.tmp.jpg" -exec rm -v {} \; 

#find ./result/word_imgs -name "*.png" -exec rm -v {} \; 

 