#!/usr/bin/env python3

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
    print(f"company.yamlize():  {company.yamlize()}")

