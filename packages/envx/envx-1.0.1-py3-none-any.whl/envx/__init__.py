#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
import configparser
import platform
import os


def make_env_dir(
        file_name: str
):
    """
    根据环境生成默认的环境文件路径信息，返回一个dict,其中file_dir为环境文件的绝对路径
    此处为固定预设路径
    :param file_name: 需要读取的环境文件名
    """
    inner_file_name = file_name.lower()  # 不区分大小写
    if platform.system() == 'Windows':  # Windows
        basic_return = {
            'sys_support': True,
            'path_separator': '\\',
            'env_path': 'C:\\env\\',
            'file_dir': 'C:\\env\\%s' % inner_file_name
        }
        return basic_return
    elif platform.system() == 'Darwin':  # macOS
        basic_return = {
            'sys_support': True,
            'path_separator': '/',
            'env_path': '/Users/env/',
            'file_dir': '/Users/env/%s' % inner_file_name
        }
        return basic_return
    elif platform.system() == 'Linux':  # Linux
        basic_return = {
            'sys_support': True,
            'path_separator': '/',
            'env_path': '/env/',
            'file_dir': '/env/%s' % inner_file_name
        }
        return basic_return
    else:  # unknown
        basic_return = {
            'sys_support': False,
            'path_separator': '',
            'env_path': '',
            'file_dir': ''
        }
        return basic_return


def read_env_file(
        env_file_dir: str,
        line_split: str = '\n',
        key_split: str = '='
):
    """
    读取并处理环境文件的内容为dict，这里输入的是文件的绝对路径
    :param env_file_dir: 需要读取的环境文件绝对路径
    :param line_split: 换行字符
    :param key_split: 键值区分字符
    """
    env_dict = dict()
    f = open(env_file_dir, encoding='utf-8')
    file_read = f.read()
    lines = file_read.split(line_split)  # 按行拆分
    for each_line in lines:
        if key_split in each_line:
            each_line_split = each_line.split(sep=key_split, maxsplit=1)  # 对每行按拆分符号拆分且只拆分一次，防止有多个拆分符影响
            env_dict[each_line_split[0]] = each_line_split[1]  # 组装结果
        else:
            continue
    return env_dict


def read(
        file_name: str = None,
        file_dir: str = None,
        line_split: str = '\n',
        key_split: str = '='
):
    """
    环境文件的内容是以行区分，以=拆分键值对，例如：HOST=192.168.0.1，读取的结果是一个dict，将原来的行按照=符号组成键值对，例如：{"HOST": "192.168.0.1"}
    :param file_name: 环境文件名，不区分大小写，例如：mysql.env、mongo.env、redis.env，其路径将使用默认路径
    :param file_dir: 环境文件绝对路径，例如：/env/mysql.env，如果指定，将优先使用
    :param line_split: 行拆分依据，默认为\n（换行）
    :param key_split: 关键字拆分依据，默认为=

    环境文件路径支持：
        Windows：
            C:\
        macOS:
            /Users/env/
        Linux:
            /env/
    """
    file_name_lower = file_name.lower()
    make_env_dir_res = make_env_dir(file_name=file_name)
    if file_dir:
        # 如果输入的详细的文件路径，就直接读取文件
        return read_env_file(
            env_file_dir=file_dir,
            line_split=line_split,
            key_split=key_split
        )
    elif file_name:
        # 如果输入的是相对文件名，则按照默认规则读取
        env_path = make_env_dir_res['env_path']
        env_file_list = os.listdir(env_path)
        for each_env_file in env_file_list:
            if file_name_lower == each_env_file.lower():
                env_file_dir = '%s%s' % (env_path, each_env_file)
                return read_env_file(
                    env_file_dir=env_file_dir,
                    line_split=line_split,
                    key_split=key_split
                )
            else:
                continue
    else:
        # 如果都未输入，则不读取
        return {}


def get_default_env():
    """
    读取默认环境信息
    存在返回：{'ENV': 'DEV', 'MSG': '开发环境'}
    不存在返回：{'ENV': None, 'MSG': None}
    """
    default_env = read(file_name='DEFAULT_ENV.env')
    if default_env is None:
        return {'ENV': None, 'MSG': None}
    else:
        return default_env
