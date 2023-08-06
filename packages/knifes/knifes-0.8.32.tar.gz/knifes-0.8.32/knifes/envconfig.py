from decouple import config as c
from knifes._settings import settings


# 结合decouple和django的settings
def config(key, default=None, cast=None):
    if default is None and hasattr(settings, 'DEFAULT_ENV_CONFIG_DICT'):
        default = settings.DEFAULT_ENV_CONFIG_DICT.get(key)
    return c(key, default=default, cast=cast) if cast else c(key, default=default)
