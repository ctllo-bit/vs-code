#!/bin/sh

# 添加 HTTP 响应头
echo "Content-Type: text/html; charset=utf-8"
echo ""

echo "<h2>Hello world!</h2>"
echo "<h3>`date '+%H:%M:%S' `</h3>"


# # 定义要读取的 index.html 路径
# INDEX_PATH="/var/apps/all.editor/target/server/dist/index.html"

# # 检查文件是否存在
# if [ ! -f "$INDEX_PATH" ]; then
#     echo "<h1>错误：index.html 不存在</h1>"
#     echo "<p>路径: $INDEX_PATH</p>"
#     exit 1
# fi

# # 读取并输出文件内容
# cat "$INDEX_PATH"
