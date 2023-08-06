import os
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import unquote, urlparse

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from loguru import logger
from retrying import retry
from tqdm import tqdm

headers = {'User-Agent': UserAgent().random}


def set_proxy():
    logger.error('请求失败，正在以代理访问')
    os.environ["https_proxy"] = "http://127.0.0.1:7890"


@retry(stop_func=set_proxy)
def get_img_src(url: str):
    res = requests.get(url, headers=headers, timeout=5)
    logger.info(f'{res.status_code} {unquote(res.request.url)}')
    page = BeautifulSoup(res.text, 'html.parser')
    # 获取 img 标签
    imgs = page.find_all('img')
    # 获取标签中的 src
    img_urls = [img.get('src') for img in imgs]
    return img_urls


def file_name_in_url(url):
    return os.path.basename(urlparse(url).path)


def remote_file_size(url):
    size = int(requests.head(url).headers['Content-Length'])
    return size


class Download:
    def __init__(self, urls: list, folder: str, thread=16):
        self.urls = urls
        # 创建下载目录
        if not os.path.exists(folder):
            os.mkdir(folder)
        # 保证下载目录以斜杆结尾
        if not (folder.endswith('/') or folder.endswith('\\')):
            self.dir = folder + '/'
        self.s = requests.session()
        self.thread = thread

    @retry(stop_func=set_proxy, wait_fixed=100)
    def normal(self):
        for url in tqdm(self.urls, colour='green'):
            file_name = file_name_in_url(url)
            with open(self.dir + file_name, 'wb') as f:
                r = self.s.get(url, headers=headers,
                               timeout=5, allow_redirects=True)
                f.write(r.content)

    @retry(wait_fixed=100)
    def _streamed_download(urls, dir, s):
        for url in tqdm(urls, colour='green'):
            file_name = file_name_in_url(url)
            with open(dir + file_name, 'wb') as f:
                r = s.get(url, headers=headers, stream=True, timeout=5)
                # copyfileobj 函数实现了数据分块
                shutil.copyfileobj(r.raw, f)

    def concurrent(self):
        """
        多线程
        """
        with ThreadPoolExecutor(max_workers=self.thread) as executor:
            futures = [executor.submit(
                self._streamed_download, self.urls, self.dir, self.s)]
            as_completed(futures)


def github_releases_latest_version(owner: str, repo: str) -> str:
    """
    获取 release 最新版本
    """
    api = f'https://api.github.com/repos/{owner}/{repo}/releases/latest'
    latest_dict = requests.get(api, headers=headers).json()
    version = latest_dict['tag_name']
    return version


def ip2deciaml(ip):
    decimal = 0
    parts = ip.split('.')[::-1]
    parts = [eval(i) for i in parts]
    for i, part in enumerate(parts):
        result = part * 256 ** i
        decimal += result
    return decimal


def ip2octal(ip):
    decimal = ip2deciaml(ip)
    # 去掉八进制的标记 o
    octal = '0' + oct(decimal)[2:]
    return octal


def ip2hexadecimal(ip):
    decimal = ip2deciaml(ip)
    hexadecimal = hex(decimal)
    return hexadecimal


if __name__ == '__main__':
    Download(
        [
            'https://download.vulnhub.com/matrix-breakout/matrix-breakout-2-morpheus.ova'],
        folder="C:/Users/24172/Desktop").concurrent()
