#!/usr/bin/env python
# demo: python .\generate_post_md.py --title 测试title --category 分类1 --tag Tag1 --urls url1 url2 --column 2
import argparse
import datetime

def generate_markdown_file(title, category, tag, urls, column):
    # 根据当前日期和标题生成文件名
    file_name_date = datetime.date.today().strftime("%Y-%m-%d")
    filename = f"../_posts/{file_name_date}-{title}.md"

    post_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 构建Markdown文件内容
    content = f"""---
title: {title}
date: {post_time} +/-TTTT
categories: {category}
tags: {tag}
---

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .gallery {{
            column-count: {column}; /* 设置列数 */
            column-gap: 10px; /* 设置列之间的间隙 */
        }}
        .gallery img {{
            width: 100%;
            break-inside: avoid; /* 避免图片跨列显示 */
            margin-bottom: 10px; /* 设置图片之间的间隙 */
        }}
    </style>
</head>
<body>

<div class="gallery">
"""

    # 添加图片URL
    for url in urls:
        content += f'    <img src="{url}" alt="Photo">\n'

    content += """
    <!-- 更多图片 -->
</div>

</body>
"""
    print(content)
    # 将内容写入文件
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Markdown文件已生成：{filename}")

if __name__ == '__main__':
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description="生成Markdown文件")
    parser.add_argument("--title", help="标题")
    parser.add_argument("--category", help="分类（多个分类请用逗号分隔）")
    parser.add_argument("--tag", help="标签（多个标签请用逗号分隔）")
    parser.add_argument("--urls", nargs="+", help="图片URL（多个URL请用空格分隔）")
    parser.add_argument("--column", type=int, default=2, help="瀑布流排版列数")

    # 解析命令行参数
    args = parser.parse_args()
    print(args.urls)
    # 生成Markdown文件
    generate_markdown_file(args.title, args.category.split(","), args.tag.split(","), args.urls, args.column)