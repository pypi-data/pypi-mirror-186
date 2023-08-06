# -*- coding: utf-8 -*-

from ruamel.yaml import YAML
import os.path as op
import sys

yaml = YAML()

d = op.join(op.abspath(op.dirname(__file__)),
            '../../share/svom/products/vt/resources/VT_frame_common.yml')
with open(d) as f:
    dic = yaml.load(f.read())

for n, att in dic['metadata'].items():
    line = '\t|'.join([n,
                       str(att['default']),
                       att.get('description_zh_cn', ''),
                       att.get('description', ''),
                       ])
    print(line)

sys.exit(0)

if 1:
    import requests
    from fdi.pns.jsonio import commonheaders, auth_headers

auth = auth_headers('foo', 'bar', commonheaders)

url = 'http://127.0.0.1:5000/fdi/v0.10'

x = requests.get(url)

print(x.status_code, x.text)


# url = 'http://127.0.0.1:5000/fdi/v0.10/pools'
# x = requests.get(url, auth=auth_headers)
# print(x.status_code, x.text)
