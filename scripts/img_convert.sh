#!/bin/bash

PNG_FILES=`find ./result/word_imgs -name "*.png"`
for file in $PNG_FILES
do
  echo "Processing: $file"
  convert $file -background white -quality 85 -flatten ${file}.tmp.jpg
  convert ${file}.tmp.jpg  imgs/vxiaozhi-watermark2.png -gravity southeast -geometry +10+10 -composite ${file%.png}.jpg
done

#find ./result/word_imgs -name "*.tmp.jpg" -exec rm -v {} \; 

#find ./result/word_imgs -name "*.png" -exec rm -v {} \; 

 