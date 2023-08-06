#!/usr/bin/env python3

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