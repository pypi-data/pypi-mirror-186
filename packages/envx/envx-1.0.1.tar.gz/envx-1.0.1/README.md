# envx
![](https://img.shields.io/badge/Python-3.8.6-green.svg)

#### 介绍

环境信息管理模块，适用于跨设备区分环境类型的情况

#### 安装教程

1.  pip安装
```shell script
pip3 install envx
```

2.  pip安装（使用淘宝镜像加速）
```shell script
pip3 install envx -i https://mirrors.aliyun.com/pypi/simple
```

#### 使用说明

1. 环境文件目录（如果没有对应目录，请创建对应的目录）
- Windows 系统
  ```text
  使用目录：C:\env\
  ```
    
- macOS 系统
  ```text
  使用目录：/Users/env/
  ```
    
- Linux 系统
  ```text
  使用目录：/env/
  ```
  
2. 环境文件案例
- 文件名：local.any.env
- 文件内容：
  ```text
  HOST=192.168.0.1
  PORT=6379
  ```
- 读取结果：
  ```json
  {
    "HOST": "192.168.0.1", 
    "PORT": "6379"
  }
  ```

3. 项目中使用代码
```python
import envx
local_any_env = envx.read('local.any.env')
```

- 建议使用环境类型标记文件：DEFAULT_ENV.env
```text
一般用来描述当前的环境信息，可以用来标记当前的环境类型，
然后后续使用时先去读当前默认的环境类型，再根据设定选取不同的环境文件，
即，会先从当前环境中读取DEFAULT_ENV.env中设定的环境类型，再读取settings.ini的具体设定，
然后根据当前环境类型取对应的环境文件；
注意：settings.ini文件必须和使用此代码的文件在同一目录，若为其他目录，需修改文件路径
```

- settings.ini
```text
[DEFAULT]
env=DEV
msg=在这里的env中设置将要使用哪个具体的环境

[DEV]
env_name=DEV-开发
env_file_name_mysql=dev.mysql.env
env_file_name_mongo=dev.mongo.env
silence_mysql=False

[TEST]
env_name=TEST-测试
env_file_name_mysql=test.mysql.env
env_file_name_mongo=test.mongo.env
silence_mysql=False

[PROD]
env_name=PROD-生产
env_file_name_mysql=prod.mysql.env
env_file_name_mongo=prod.mongo.env
silence_mysql=False
```

- 项目代码
```python
# ----------------- 读取配置信息 -----------------
import configparser
import platform
import os

if platform.system() == 'Windows':
    path_separator = '\\'
else:
    path_separator = '/'
config_dir = (os.path.dirname(os.path.realpath(__file__))) + path_separator + 'settings.ini'

config = configparser.ConfigParser()  # 类实例化
config.read(config_dir, encoding='utf-8')
default_config = config['DEFAULT']
default_env = default_config['env']
config_config = config[default_env]

# 从这里开始写需要读取为内容
env_file_name_mysql = config_config['env_file_name_mysql']
env_file_name_mongo = config_config['env_file_name_mongo']
silence_mysql = eval(config_config['silence_mysql'])
# ----------------- 读取配置信息 -----------------
```
