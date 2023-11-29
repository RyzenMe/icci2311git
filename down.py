import os
import requests
from urllib.parse import urlparse

def download_resource(url, folder='web'):
    # 解析 URL 获取文件名
    parsed_url = urlparse(url)
    filename = os.path.join(folder, os.path.basename(parsed_url.path))

    # 发送 HTTP 请求下载资源
    response = requests.get(url)
    if response.status_code == 200:
        # 确保目标文件夹存在
        os.makedirs(folder, exist_ok=True)

        # 保存文件
        with open(filename, 'wb') as file:
            file.write(response.content)
            print(f'Downloaded: {url}')

if __name__ == "__main__":
    # 所有资源链接
    resource_urls = [
        "https://template-1253409072.cos.ap-guangzhou.myqcloud.com/html-template/template-company-00002/css/bootstrap.min.css",
        "https://template-1253409072.cos.ap-guangzhou.myqcloud.com/html-template/template-company-00002/css/magnific-popup.css",
        "https://template-1253409072.cos.ap-guangzhou.myqcloud.com/html-template/template-company-00002/css/font-awesome.min.css",
        "https://template-1253409072.cos.ap-guangzhou.myqcloud.com/html-template/template-company-00002/css/templatemo-style.css",
        "https://template-1253409072.cos.ap-guangzhou.myqcloud.com/html-template/template-company-00002/js/jquery.js",
        "https://template-1253409072.cos.ap-guangzhou.myqcloud.com/html-template/template-company-00002/js/bootstrap.min.js",
        "https://template-1253409072.cos.ap-guangzhou.myqcloud.com/html-template/template-company-00002/js/jquery.stellar.min.js",
        "https://template-1253409072.cos.ap-guangzhou.myqcloud.com/html-template/template-company-00002/js/jquery.magnific-popup.min.js",
        "https://template-1253409072.cos.ap-guangzhou.myqcloud.com/html-template/template-company-00002/js/smoothscroll.js",
        "https://template-1253409072.cos.ap-guangzhou.myqcloud.com/html-template/template-company-00002/js/custom.js",
        "https://template-1253409072.cos.ap-guangzhou.myqcloud.com/user-upload-images/4527/28000042wz6o.png",
        "https://template-1253409072.cos.ap-guangzhou.myqcloud.com/user-upload-images/4527/Snipaste_2023-11-06_17-21-21.png",
        "https://template-1253409072.cos.ap-guangzhou.myqcloud.com/user-upload-images/4527/Snipaste_2023-11-05_20-51-28.png",
        "https://template-1253409072.cos.ap-guangzhou.myqcloud.com/user-upload-images/4527/Snipaste_2023-11-05_20-13-34.png",
        "https://template-1253409072.cos.ap-guangzhou.myqcloud.com/user-upload-images/4527/Snipaste_2023-11-06_17-20-20.png",
        "https://template-1253409072.cos.ap-guangzhou.myqcloud.com/user-upload-images/4527/01d04d58d4c275a801219c77efef4a.jpg@1280w_1l_2o_100sh.jpg"
    ]

    # 下载所有资源
    for url in resource_urls:
        download_resource(url)
