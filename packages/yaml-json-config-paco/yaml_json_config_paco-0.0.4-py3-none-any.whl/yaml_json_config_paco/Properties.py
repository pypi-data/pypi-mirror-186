"""load/dump key value properties file, comment lines will be kept"""
import collections
import re


class PropertyException(Exception): pass


class PropertyLine:
    # 正则识别每一行的key=value以及可能有也可能没有的注释部分"#..."
    PATTERN = re.compile(r'(\w.*?)\s*=\s*(.*?)\s*(#.*){0,1}$')

    def __init__(self, line):
        self.raw_line = str(line)
        self.key = None
        self.value = None
        self.comment = None
        self.modified = False
        l = self.raw_line.strip()
        if l.startswith('#'):
            self.key = id(l)  # 考虑到要放入OrderDict，commentline也需要分配一个key
            self.comment = l
        else:
            m = PropertyLine.PATTERN.match(l)
            if m:
                self.key, self.value, self.comment = m.groups()
            else:
                # 又不是注释，有不是合适的
                raise PropertyException("unrecognized line:{}".format(line))

    def get_value(self):
        return self.value

    def set_value(self, v):
        if self.key and self.value:
            self.value = v
            self.modified = True
        else:
            raise PropertyException("cannot set value to a comment")

    def __str__(self):
        if not self.modified:
            return self.raw_line
        if self.key:
            if self.comment:
                return "{}={} {}".format(self.key, self.value, self.comment)
            else:
                return "{}={}".format(self.key, self.value)
        return ""

    def __repr__(self):
        return self.__str__()


class Properties:
    def __init__(self):
        self.data = collections.OrderedDict()

    def load_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            self.load(f)

    def load(self, iterable):
        for l in iterable:
            if len(l) <1:
                continue
            p = PropertyLine(str(l))
            self.data[p.key] = p

    def loads(self, text):
        self.load(text.split("\n"))

    def dumps(self):
        return str(self)

    def dump_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.dumps())

    def __str__(self):
        return "\n".join([str(l) for l in self.data.values()])

    # 以下方法，为Properties提供了类似dict的访问方式
    def __delitem__(self, key):
        self.data.__delitem__(key)

    def __getitem__(self, item):
        return self.data[item].value

    def __setitem__(self, key, value):
        if key in self.data:
            self.data[key].set_value(value)
        else:
            # new property to add
            self.data[key] = PropertyLine("{}={}".format(key, value))

    def __iter__(self):
        for k in self.data.keys():
            if self.data[k].value: #不是kv的行不遍历
                yield k


if __name__=='__main__':
    content = '''
# line 1
a.b.c.d = 778888
# line 2
dde.bbb = False
model = M1  # M1,M2,M3
'''
    ps = Properties()
    ps.loads(content)
    # 下面把ps当作一个普通的dict访问
    for k in ps:
        print("ITEM: [{}]={}".format(k, ps[k]))
    # add property
    ps["paco"] = 10000
    # change property
    ps["model"] = 'M3'
    # delete
    del ps["a.b.c.d"]
    # 访问一个不存在的
    try:
        print(ps['a777'])
    except KeyError as e:
        print(e)
    # 把修改过的properties dump出来一个str
    print("\nModified Properties Content:\n{}".format(ps.dumps()))





