#!/usr/bin/env python
import json
import subprocess

data = json.load(open('/tmp/data.json'))
for i,d in enumerate(data,1):
    id_shrink = '%s..%s' % (d['id'][0:2],d['id'][-2:])
    filename = list(d['files'].keys())[0]
    description = d.get('description','') or '' # todo: remove
    url = 'git@gist.github.com:%s.git' % d['id']
    path = '%s %s %s' % (id_shrink,filename,description)
    args = ['git','submodule','add','-q',url,path]
    print('1) https://gist.github.com/%s' % d['id'])
    print(' '.join(args))
    subprocess.call(args)
