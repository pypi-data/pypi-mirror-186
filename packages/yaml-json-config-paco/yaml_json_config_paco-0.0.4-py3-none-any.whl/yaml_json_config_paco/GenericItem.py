"""defined GenericItem for yaml/json <-> object transformation"""
from collections import OrderedDict
from .OrderedDictYaml import ordered_yaml_dump, ordered_yaml_load
import json


class YamlJsonException(Exception):
    pass


class GenericItem(object):
    """定义了一些通用的方法，用于从一个dict构造对象，以及获取子类的属性"""
    @classmethod
    def from_file(cls, filename, loose=False):
        obj = cls()
        obj.load_from_file(filename, loose)
        return obj

    @classmethod
    def from_json_text(cls, json_text, loose=False):
        obj = cls()
        obj.load_from_json_text(json_text, loose)
        return obj

    @classmethod
    def from_yaml_text(cls, yaml_text, loose=False):
        obj = cls()
        obj.load_from_yaml_text(yaml_text, loose)
        return obj

    def attr_to_convert_to_list(self):
        """leave to user to defined a attriburteName->Class list/tuple, letting GenericItem kwon how to 
        convert the part with attributeName to a list of Class instances vice vasa"""
        return []

    def attr_to_convert(self):
        """leave for user to defined a attributeName->Class list/tuple, to convert dict to Class instance"""
        return []

    def __init__(self):
        self._order = None

    def set_attribute(self, k, v):
        if k not in self._order:
            self._order.append(k)
        self.__dict__[k] = v

    def load_from_dict(self, hash:OrderedDict, loose=False):
        """从一个dict构造对象，以及获取子类的属性"""
        self._order = list(hash.keys())
        self.__dict__.update(hash)

        for attr, __KLASS__ in self.attr_to_convert():
            if attr not in self.__dict__ or (not isinstance(self.__dict__[attr], OrderedDict) and not isinstance(self.__dict__[attr], __KLASS__)):
                if attr in self.__dict__ and len(self.__dict__[attr]) == 0:
                    # “”的情况，这个值是个optional的，直接跳过就可以
                    continue
                # 如果既无默认值，文件里面又没有配置
                raise YamlJsonException("no valid attribute: {} found for conver {}".format(attr, __KLASS__))
            if isinstance(self.__dict__[attr], OrderedDict):
                # 有可能设置了默认值，而文件里面配置配置对应的项，所以需要区分情况不一定完全要从文件load数据
                # 只有文件里有配置，才会到这里从文件load，覆盖掉默认值
                y = __KLASS__()
                y.load_from_dict(self.__dict__[attr])
                y.validate_user_items()
                self.__dict__[attr] = y

        for attr, __KLASS__ in self.attr_to_convert_to_list():
            o = OrderedDict()
            if attr not in self.__dict__ or not isinstance(self.__dict__[attr], list):
                if loose: continue
                # 期望一个OrderedDict的List
                raise YamlJsonException("no valid attribute: {} found for conver to list of {}".format(attr, __KLASS__))
            l = list()
            for x in self.__dict__[attr]:
                y = __KLASS__()
                y.load_from_dict(x)
                y.validate_user_items()
                l.append(y)
            self.__dict__[attr] = l
        if not loose:
            self.validate_user_items()

    def attr_to_convert_to_list(self):
        """leave to user to defined a attriburte->Class hash, to convert dict to list of Class instance and vice vasa"""
        return []

    def attr_to_convert(self):
        """leave for user to defined a attribute->Class hash, to convert dict to Class instance"""
        return []

    @staticmethod
    def deep_dump_to_dict(obj:OrderedDict):
        """递归调用所有GenericItem成员的dump_to_dict()"""
        for k in obj:
            v = obj[k]
            if isinstance(v, GenericItem):
                v = v.dump_to_dict()
                v = GenericItem.deep_dump_to_dict(v)
            obj[k] = v
        return obj

    def get_attribute(self, attr:str, default=None):
        if attr in self.__dict__:
            return self.__dict__[attr]
        else:
            return default

    def get_attributes(self):
        attributes = None
        if '_order' in self.__dict__ and self._order is not None:
            attributes = list(self._order)
            # 如果存在_order说明是从文件load进来的，可能有些字段文件里面没有但是取了默认值，需要补充进去
            extra = [k for k in self.__dict__.keys() if (k[0] != '_' and k not in attributes)]
            attributes += extra
        else:
            attributes = [k for k in self.__dict__.keys() if k[0] != '_']
        return attributes

    def dump_to_dict(self):
        """获取所有对用户有意义的属性, 按输入时候的顺序"""
        od = OrderedDict()
        to_list = {x:y for x,y in self.attr_to_convert_to_list()}
        attributes = self.get_attributes()
        for attribute_name in attributes:
            v = self.__dict__[attribute_name]
            if v == "":
                continue
            if attribute_name in to_list:
                v = [n.dump_to_dict() for n in v]
            if isinstance(v, GenericItem):
                v = v.dump_to_dict()
            if isinstance(v, OrderedDict):
                v = GenericItem.deep_dump_to_dict(v)
            od[attribute_name] = v
        return od

    def validate_user_items(self):
        """检查load_from_dict之后，是否所对用于有意义的属性都被初始化了"""
        d = self.dump_to_dict()
        keys_not_init = [k for k in d if d[k] is None]
        if len(keys_not_init) > 0:
            raise YamlJsonException("{} obj attributes: {} are not init".format(
                self.__class__.__name__,
                ",".join(keys_not_init)
            ))

    def load_from_json_text(self, json_text, loose=False):
        obj = json.loads(json_text, object_pairs_hook=OrderedDict)
        self.load_from_dict(obj, loose)

    def load_from_yaml_text(self, yaml_text, loose=False):
        obj = ordered_yaml_load(yaml_text)
        self.load_from_dict(obj, loose)

    def load_from_file(self, filepath, loose=False):
        suffix = filepath.split(".")[-1]
        if suffix not in ['yml', 'yaml', 'json']:
            raise YamlJsonException("cannot load file {}, only .yml, .yaml, .json supported".format(filepath))
        with open(filepath, 'r', encoding='utf-8') as f:
            if suffix == 'json':
                self.load_from_dict(json.load(f, object_pairs_hook=OrderedDict), loose)
            else:
                obj = ordered_yaml_load(f)
                self.load_from_dict(obj)

    def __str__(self):
        return str(self.jsonify())

    def __repr__(self):
        return self.__str__()

    def jsonify(self, indent=2):
        return json.dumps(self.dump_to_dict(), indent=indent, ensure_ascii=False)

    def yamlize(self):
        return ordered_yaml_dump(self.dump_to_dict())

    def dump_to_file(self, filename):
        func = None
        file_suffix = filename.split(".")[-1]
        if file_suffix in ['yaml', 'yml']:
            func = self.yamlize
        elif file_suffix == 'json':
            func = self.jsonify
        else:
            raise YamlJsonException("unrecognized file suffix for file {}, only .json, .yml, .yaml supported".format(filename))
        with open(filename, "w", encoding='utf-8') as f:
            f.write(func())
