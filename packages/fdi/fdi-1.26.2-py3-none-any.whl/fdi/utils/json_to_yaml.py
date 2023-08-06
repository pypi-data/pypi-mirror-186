import yaml
import json
from collections import OrderedDict
# 读取json文件
f = open('VTSE.json', 'r', encoding='utf-8')
# 转化为字典
d = json.loads(f.read(), object_pairs_hook=OrderedDict)
f.close()
import pprint
pprint.pprint(d)
#d = OrderedDict(d)
ym = yaml.dump(d, allow_unicode=True)
# print(ym)
# 转换为yaml
yaml_f = open("VTSE.yml", "w", encoding='utf-8')
yaml_f.write(ym)
yaml_f.close()
