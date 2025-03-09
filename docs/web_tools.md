## 生成 .min.css 文件的常用方法

```
# 安装 css-minify
npm install -g css-minify

# 压缩单个文件
css-minify -f input.css -o ./

# 压缩整个目录
css-minify -d src/css
```