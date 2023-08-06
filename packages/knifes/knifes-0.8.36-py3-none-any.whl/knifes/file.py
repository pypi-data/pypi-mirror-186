import io
import os
from .digests import md5
from typing import Callable


# 读文件
def read_file(filename, mode='r'):
    if not os.path.exists(filename):
        return ''
    with open(filename, mode) as f:
        return f.read()


# 装饰器
def disk_cache(cache_dir: str, ignore_error: bool = False, gen_filename: Callable = lambda args: md5(str(args[0]))):
    """适用于小文件的磁盘缓存
    装饰的func第1个参数是cache key
    """
    def outer_wrapper(func):
        def wrapper(*args, **kwargs) -> str:
            if not args:  # 参数校验
                raise ValueError('missing cache key')
            cache_path = os.path.join(cache_dir, gen_filename(args))
            if os.path.exists(cache_path):
                return cache_path
            try:
                result = func(*args, **kwargs)  # func return (bytes、str、io.BytesIO)
                if isinstance(result, bytes):
                    cache_bytes = result
                elif isinstance(result, str):
                    with open(result, 'rb') as f:
                        cache_bytes = f.read()
                elif isinstance(result, io.BytesIO):
                    cache_bytes = result.getvalue()
                    result.close()
                else:
                    raise RuntimeError('unsupported data type')

                os.makedirs(cache_dir, exist_ok=True)
                with open(cache_path, 'wb') as f:
                    f.write(cache_bytes)
                return cache_path
            except:
                if not ignore_error:
                    raise
        return wrapper
    return outer_wrapper

