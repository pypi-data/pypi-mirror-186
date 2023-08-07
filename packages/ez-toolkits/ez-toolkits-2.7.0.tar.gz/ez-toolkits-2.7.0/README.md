# Python Toolkits

代码规范:

- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PEP8 翻译](https://www.jianshu.com/p/78d76f85bd82)
- [PEP 8 -- Python 代码风格指南](https://github.com/kernellmd/Knowledge/blob/master/Translation/PEP%208%20%E4%B8%AD%E6%96%87%E7%BF%BB%E8%AF%91.md)

Boolen (False)

| Types | False |
| ---   | ---   |
| bool  | False |
| int   | 0     |
| float | 0.0   |
| str   | ''    |
| list  | []    |
| tuple | ()    |
| dict  | {}    |
| set   | {\*()} {\*[]} {\*{}} |

list/tuple/dict/set 初始化和类型转换:

- 变量初始化推荐使用 `[]/()/{}/{*()}/{*[]}/{*{}}` (性能更好)
- 类型转换则使用具体函数 `list()/tuple()/dict()/set()`

list/tuple/set 的区别:

- list 元素可以改变且可以不唯一
- tuple 元素不能改变且可以不唯一
- set 元素可以改变但唯一

变量类型

- 查看变量类型 type(x)
- 判断变量类型 isinstance(x, str)

函数

- 必须检查变量类型
- 必须有返回
    - 有内容返回内容
    - 无内容返回None
    - 仅执行则返回True或False

函数变量

- 建议定义为 None
- 没有定义变量初始值, 添加 *args, **kwargs
- 定义了变量初始值, 添加 **kwargs
- 其它情况 *args, x=None, **kwargs
- 检查变量类型

配置文件用 JSON, 简单高效, 还能保持数据类型

```py
logger.info('配置文件解析...')

config_file = os.path.realpath(argument_config)
config_dict = utils.json_file_parser(config_file)

exit(1) if config_dict == None else next

print(config_dict)
```

## Exit

如果要编译脚本, 代码中有使用 exit 退出脚本时, 将 `exit()` 改为 `sys.exit()`, 否则编译的文件调用 `exit()` 会失败
