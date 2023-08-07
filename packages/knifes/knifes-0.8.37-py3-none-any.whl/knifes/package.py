import pkgutil
from os import path


def get_all_module_name(pkg_path, prefix=''):
    """How To Use?
    import xx.abc
    get_all_module_name(os.path.dirname(xx.abc.__file__), prefix=xx.abc.__name__ + '.')
    """
    module_name_list = []
    for m in pkgutil.iter_modules([pkg_path], prefix=prefix):
        if m.ispkg:
            name = m.name.removeprefix(prefix)
            module_name_list.extend(get_all_module_name(path.join(pkg_path, name), prefix=prefix + name + '.'))
        else:
            module_name_list.append(m.name)
    return module_name_list
