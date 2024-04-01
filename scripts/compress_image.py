import os
from PIL import Image

def compress_images(directory, max_size):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".JPG"):
            filepath = os.path.join(directory, filename)
            image = Image.open(filepath)
            image.save(filepath, "JPEG", optimize=True, quality=50)

# 指定目录和最大文件大小
directory = "F:\\OneDrive\\日常coding\\yunfei.github.io\\assets\\images\\shanghai"
max_size = 2 * 1024 * 1024  # 2MB

# 压缩图片
compress_images(directory, max_size)