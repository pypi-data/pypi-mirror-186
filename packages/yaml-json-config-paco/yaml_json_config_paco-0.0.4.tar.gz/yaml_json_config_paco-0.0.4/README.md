# Module yaml_json_config

This is a module to facilitate reading a config file or text string in json or yaml to a python object, vice versa.

Not only flat key value style is supported, nested objects and list of objects can be supported.

## Demo of Usage
Let's say there is a sample config file in yaml format to represent a company
```yaml
address: "#368 GuangZhou District, GZ, GD"
telephone: "+86206666666666"
boss:
  name: alpha
  id: 001
  age: 40
  linkman:
    name: omega
members:
  - name: alpha
    id: 001 
    age: 40
  - name: beta 
    id: 002 
    age: 33
  - name: sigma
    id: 003 
    age: 38
```
There are 4 shallow attributes, 'address', 'telephone' are simple strings, 'members' is a list of common nested structure, 'boss' is a nested structure with a nested structure 'linkman'.

### Shallow Load to Object
```python
from yaml_json_config_paco.GenericItem import GenericItem

class Company0(GenericItem):
    """shallow load demo"""
    pass

if __name__=='__main__':
    company0 = Company0.from_file("sample.yml") 
    print(f"company0.address:  {company0.address}")
    print(f"company0.telephone:  {company0.telephone}")
    print(f"company0.boss:  {company0.boss}")
    print(f"company0.members:  {company0.members}")
    print(f"company0.dump_to_dict(): {company0.dump_to_dict()}")
    print(f"company0.jsonify():\n{company0.jsonify()}")
    print(f"company0.yamlize():\n{company0.yamlize()}")
```
run above code, you will get below, the 4 shallow attribute can be access directly by attribute name as object attributes, the nested structures are kept as OrderedDict and list of OrderedDict, the nested structure is just kept as OrderedDict in side OrderedDict

```python
company0.address:  #368 GuangZhou District, GZ, GD
company0.telephone:  +86206666666666
company0.boss:  OrderedDict([('name', 'alpha'), ('id', 1), ('age', 40), ('linkman', OrderedDict([('name', 'omega')]))])
company0.members:  [OrderedDict([('name', 'alpha'), ('id', 1), ('age', 40)]), OrderedDict([('name', 'beta'), ('id', 2), ('age', 33)]), OrderedDict([('name', 'sigma'), ('id', 3), ('age', 38)])]
company0.dump_to_dict(): OrderedDict([('address', '#368 GuangZhou District, GZ, GD'), ('telephone', '+86206666666666'), ('boss', OrderedDict([('name', 'alpha'), ('id', 1), ('age', 40), ('linkman', OrderedDict([('name', 'omega')]))])), ('members', [OrderedDict([('name', 'alpha'), ('id', 1), ('age', 40)]), OrderedDict([('name', 'beta'), ('id', 2), ('age', 33)]), OrderedDict([('name', 'sigma'), ('id', 3), ('age', 38)])])])

# This is the way to dump to json
company0.jsonify(): 
{
  "address": "#368 GuangZhou District, GZ, GD",
  "telephone": "+86206666666666",
  "boss": {
    "name": "alpha",
    "id": 1,
    "age": 40,
    "linkman": {
      "name": "omega"
    }
  },
  "members": [
    {
      "name": "alpha",
      "id": 1,
      "age": 40
    },
    {
      "name": "beta",
      "id": 2,
      "age": 33
    },
    {
      "name": "sigma",
      "id": 3,
      "age": 38
    }
  ]
}

# this is the way to dump to yaml
company0.yamlize(): 
address: '#368 GuangZhou District, GZ, GD'
telephone: '+86206666666666'
boss:
  name: alpha
  id: 1
  age: 40
  linkman:
    name: omega
members:
- name: alpha
  id: 1
  age: 40
- name: beta
  id: 2
  age: 33
- name: sigma
  id: 3
  age: 38
```
### Deep Load to Object
```python
from yaml_json_config_paco.GenericItem import GenericItem

class Person(GenericItem):
    def __init__(self):
        self.name = None
        self.id = None
        self.age = None        

class Company(GenericItem):
    def __init__(self):
        self.boss: Person = None
        self.members:list(Person) = None

    def attr_to_convert_to_list(self):
        # tell GenericItem to load members as list of Person Class objects
        return (('members', Person),)

    def attr_to_convert(self):
        # tell GenericItem to load boss as a Person Class object
        return (('boss', Person),)

if __name__=='__main__':
    company = Company.from_file("sample.yml") 
    print(f"company.address:  {company.address}")
    print(f"company.boss:  {company.boss}")
    print(f"company.boss.name:  {company.boss.name}")
    print(f"company.boss.linkman:  {company.boss.linkman}")
    print(f"company.members:  {company.members}")
    print(f"company.members[1]: {company.members[1]}")
    print(f"company.members[1].name: {company.members[1].name}")
    print(f"company.jsonify():\n{company.jsonify()}")
    print(f"company.yamlize():\n{company.yamlize()}")
```

run above will get below.
The 'attr_to_convert_to_list' and 'attr_to_convert' will be called by GenericItem so that it will get information how to deal with some nested attributes.
The nested can be recursive.

```python
company.address:  #368 GuangZhou District, GZ, GD
company.boss:  {
  "name": "alpha",
  "id": 1,
  "age": 40,
  "linkman": {
    "name": "omega"
  }
}
# this time, boss' name can be access by attribute name
company.boss.name:  alpha
# linkman is not specified with a python class, so it is kept as a OrderDict
company.boss.linkman:  OrderedDict([('name', 'omega')])
# members is a list of Person, so it can be access by index to the Person object, and access by Person attributes
company.members:  [{
  "name": "alpha",
  "id": 1,
  "age": 40
}, {
  "name": "beta",
  "id": 2,
  "age": 33
}, {
  "name": "sigma",
  "id": 3,
  "age": 38
}]
company.members[1]: {
  "name": "beta",
  "id": 2,
  "age": 33
}
company.members[1].name: beta

company.jsonify():
{
  "address": "#368 GuangZhou District, GZ, GD",
  "telephone": "+86206666666666",
  "boss": {
    "name": "alpha",
    "id": 1,
    "age": 40,
    "linkman": {
      "name": "omega"
    }
  },
  "members": [
    {
      "name": "alpha",
      "id": 1,
      "age": 40
    },
    {
      "name": "beta",
      "id": 2,
      "age": 33
    },
    {
      "name": "sigma",
      "id": 3,
      "age": 38
    }
  ]
}

company.yamlize():
address: '#368 GuangZhou District, GZ, GD'
telephone: '+86206666666666'
boss:
  name: alpha
  id: 1
  age: 40
  linkman:
    name: omega
members:
- name: alpha
  id: 1
  age: 40
- name: beta
  id: 2
  age: 33
- name: sigma
  id: 3
  age: 38
```

### Default Value nd Optiontal Attribute
```python
from yaml_json_config_paco.GenericItem import GenericItem

class Person(GenericItem):
    def __init__(self):
        self.name = None   # set None as mandatory attribute
        self.id = "na"     # set value as default value
        self.age = "na"    # set value as default value
        self.linkman = ""  # set to "" as optional

    def attr_to_convert(self):
        return (('linkman', Person),)

class Company(GenericItem):
    def __init__(self):
        self.boss: Person = None
        self.members:list(Person) = None

    def attr_to_convert_to_list(self):
        # tell GenericItem to load members as list of Person Class objects
        return (('members', Person),)

    def attr_to_convert(self):
        # tell GenericItem to load boss as a Person Class object
        return (('boss', Person),)

if __name__=='__main__':
    company = Company.from_file("sample.yml") 
    print(f"company.address:  {company.address}")
    print(f"company.boss:  {company.boss}")
    print(f"company.boss.name:  {company.boss.name}")
    print(f"company.boss.linkman.name:  {company.boss.linkman.name}")
    print(f"company.members:  {company.members}")
    print(f"company.members[1]: {company.members[1]}")
    print(f"company.members[1].name: {company.members[1].name}")
    print(f"company.members[1].linkman: {company.members[1].linkman}")
```

run above to get below,

```python
company.address:  #368 GuangZhou District, GZ, GD
company.boss:  {
  "name": "alpha",
  "id": 1,
  "age": 40,
  "linkman": {
    "name": "omega",
    "id": "na",            # with default value as the config file not set
    "age": "na"            # with default value
  }
}
company.boss.name:  alpha
company.boss.linkman.name:  omega
company.members:  [{    # the optional linkman is not present here
  "name": "alpha",
  "id": 1,
  "age": 40
}, {
  "name": "beta",
  "id": 2,
  "age": 33
}, {
  "name": "sigma",
  "id": 3,
  "age": 38
}]
company.members[1]: {
  "name": "beta",
  "id": 2,
  "age": 33
}
company.members[1].name: beta
company.members[1].linkman: 
# pack to yaml
company.yamlize():  
address: '#368 GuangZhou District, GZ, GD'
telephone: '+86206666666666'
boss:
  name: alpha
  id: 1
  age: 40
  linkman:
    name: omega
    id: na
    age: na
members:
- name: alpha
  id: 1
  age: 40
- name: beta
  id: 2
  age: 33
- name: sigma
  id: 3
  age: 38
```


### Dump and Load, Json or Yaml
A GenericItem classmethod 'from_file' is provided to load from file.
A GenericItem method 'dump_to_file' is provide to dump to file.
The format is automatically recognized by the suffix of the filename you feed, 'json', 'yml', 'yaml' are supported.

Example:

```python
company.dump_to_file("sample.json")
with open("sample.json", "r", encoding="utf-8") as f:
   print(f"read sample.json file:\n{f.read()}\n")

company2 = Company.from_file("sample.json")
print(f"company2.yamlize():\n{company2.yamlize()}")
```

Run above to get below

```python
read sample.json file:
{
  "address": "#368 GuangZhou District, GZ, GD",
  "telephone": "+86206666666666",
  "boss": {
    "name": "alpha",
    "id": 1,
    "age": 40,
    "linkman": {
      "name": "omega"
    }
  },
  "members": [
    {
      "name": "alpha",
      "id": 1,
      "age": 40
    },
    {
      "name": "beta",
      "id": 2,
      "age": 33
    },
    {
      "name": "sigma",
      "id": 3,
      "age": 38
    }
  ]
}

company2.yamlize():
address: '#368 GuangZhou District, GZ, GD'
telephone: '+86206666666666'
boss:
  name: alpha
  id: 1
  age: 40
  linkman:
    name: omega
members:
- name: alpha
  id: 1
  age: 40
- name: beta
  id: 2
  age: 33
- name: sigma
  id: 3
  age: 38
```



