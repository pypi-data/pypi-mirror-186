import pathlib

import pyzipper
from gqf.time import timeit
from loguru import logger


@timeit
def get_files(path: str, ext=''):
    """
    递归获取路径所有文件
    支持过滤后缀
    """
    pattern = '*.*' if ext == '' else f'*.{ext}'
    # rglob 相当于在 pattern 前加上了 “**/”，启用了递归
    l = list(pathlib.Path(path).rglob(pattern))
    logger.info(f'获取文件完成，共 {len(l)} 个')
    return l


def extract_zip(zip_file: str, password: str):
    """
    解压 zip
    支持 AES256 加密的 zip
    问题：中文文件乱码
    """
    with pyzipper.AESZipFile(zip_file, 'r', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as f:
        f.setpassword(password.encode())
        try:
            f.extractall()  # 使用密码尝试解压
            logger.info("找到密码：" + password)
        except RuntimeError:
            pass
