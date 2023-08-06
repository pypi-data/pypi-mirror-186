#!/usr/bin/env python
"""yaml and OrderedDict transfermation"""
from collections import OrderedDict
import yaml

MAX_LINE_WIDTH = 9999

class OrderedLoader(yaml.Loader):
    pass

def construct_mapping(loader, node):
    loader.flatten_mapping(node)
    return OrderedDict(loader.construct_pairs(node))

class OrderedDumper(yaml.SafeDumper):
    pass

def _dict_representer(dumper, data):
    return dumper.represent_mapping(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        data.items())

def ordered_yaml_load(stream):
    """load yaml to orderedDict"""
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)

def ordered_yaml_dump(data, stream=None, **kwds):
    """dump orderedDict to yaml"""
    OrderedDumper.add_representer(OrderedDict, _dict_representer)
    # width 拉到9999避免输出无故断行,默认值是80
    return yaml.dump(data, stream, OrderedDumper, allow_unicode=True, indent=2, width=MAX_LINE_WIDTH, **kwds)

if __name__=='__main__':
    yaml_str = '''
a: aaaa
b: bbbb
c:   #kdfkdfj
    - dddd
    - eeee
    - ffff
z:
    x: xxxxx
    y: yyyyy
    z: zzzzz
    '''
    od = ordered_yaml_load(yaml_str)
    print(od)

    ss = ordered_yaml_dump(od)
    print(ss)

    with open("../test.yml", encoding='utf8') as f:
        od = ordered_yaml_load(f)
        print(od)

