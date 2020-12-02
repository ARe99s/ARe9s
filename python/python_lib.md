# PYTHON 常用库

## 日期时间处理

### `time`

```python
In [1]: import time

In [2]: time.time()
Out[2]: 1606916552.3138678

In [3]: time.localtime()
Out[3]: time.struct_time(tm_year=2020, tm_mon=12, tm_mday=2, tm_hour=21, tm_min=44, tm_sec=1, tm_wday=2, tm_yday=337, tm_isdst=0)
    
In [4]: time.strftime('%Y-%m-%d', time.localtime())
Out[4]: '2020-12-02'

In [5]: time.strptime('2020-12-02', '%Y-%m-%d')
Out[5]: time.struct_time(tm_year=2020, tm_mon=12, tm_mday=2, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=337, tm_isdst=-1)
```

### `datetime `是对`time`的第二次封装

```python
In [6]: from datetime import datetime

In [7]: datetime.now
Out[7]: <function datetime.now(tz=None)>

In [8]: datetime.now()
Out[8]: datetime.datetime(2020, 12, 2, 21, 47, 36, 163779)

In [9]: from datetime import *

In [10]: datetime.now() - timedelta(days=1)
Out[10]: datetime.datetime(2020, 12, 1, 21, 51, 17, 144882)
```

## 日志处理

`logging`

线程安全， 可以用在多线程应用中

多级别 `info` `warning` `error` `critical` `debug` 

`info` 级别记录系统正常信息

`warning` 出现不影响正常使用的情况

`error` 出现影响正常使用的情况

默认配置的级别`debug`和`info` 不会被打印

 `basicConfig` 配置日志参数

常用：`filename`设置存放路径；`level`设置日志级别；`datefmt` 设置日期格式；`format` 设置日志格式

## 随机数

`random.random()`基于 时间戳生成的伪随机数

`randrange(0,100,2)` 范围内生成随机数

`choice([1,2,3])` 列表内随机选

`sample([1,2,3,4,5], k=4)` 列表随机选定数量

## JSON

`import json`

`json.loads()`解码

`json.dumps()`编码

## 路径处理

```python
from pathlib import Path # 推荐使用

p = Path()
p.resolve() # 显示当前路径

path = '/user/a.txt'
p = Path(path)
p.name # 显示文件名
p.stem # 显示前缀
p.suffix # 显示文件扩展名
p.suffixes # 显示多重文件扩展名
p.parent # 显示路径
p.parents # 返回路径的迭代器
p.aprts # 返回路径的组成 形式是元组
p.exists # 判断文件是否存在
```

```python
import os
os.path.abspath('a.txt') # 返回路径
```

## 实现daemon进程

daemon进程：随开机一起启动，还可以脱离终端，关闭终端也可以运行 类似与windows的服务

## 正则表达式

`import re` 

用途：

- 验证用户输入
- 分析文本
- 处理文本