import os
import re
import urllib.parse
import requests

# Vue 文件路径
vue_file_path = "src/App.vue"
# 下载图片保存目录
public_dir = "public"

# 读取 Vue 文件内容
with open(vue_file_path, "r", encoding="utf-8") as file:
    vue_content = file.read()

# 匹配所有外部图片链接 (以 http 或 https 开头)
img_urls = re.findall(r'https?://[^\s"\'()]+', vue_content)

# 过滤掉重复的 URL
unique_img_urls = list(set(img_urls))

print(len(unique_img_urls))
# 下载图片并替换链接
url_to_local = {}
os.makedirs(public_dir, exist_ok=True)

for index, url in enumerate(unique_img_urls):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            ext = os.path.splitext(urllib.parse.urlparse(url).path)[-1]
            ext = ext if ext else ".jpg"
            local_filename = f"img_{index}{ext}"
            local_path = os.path.join(public_dir, local_filename)
            with open(local_path, "wb") as img_file:
                img_file.write(response.content)
            url_to_local[url] = f"/{local_filename}"
    except Exception as e:
        print(f"下载失败: {url}, 错误: {e}")

# 替换 Vue 文件中的链接
for url, local_path in url_to_local.items():
    vue_content = vue_content.replace(url, local_path)

# 输出修改后的内容
modified_vue_path = "src/App2.vue"
with open(modified_vue_path, "w", encoding="utf-8") as file:
    file.write(vue_content)

modified_vue_path, list(url_to_local.values())
