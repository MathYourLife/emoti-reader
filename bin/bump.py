#!/usr/bin/env python

import os
import subprocess

module_path = 'src'
module_name = 'EmotiReader'

root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
init = os.path.join(root, module_path, '%s/__init__.py' % module_name)

with open(init) as f:
    contents = f.read()


leader = '\n__version__ = \''
start = contents.find(leader) + len(leader)
end = contents.find('\n', start) - 1

ver = map(int, contents[start:end].split('.'))


p = subprocess.Popen(['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
branch, err = map(str.strip, p.communicate())

if branch == 'master':
    exit()

p = subprocess.Popen(['git', 'log', 'master..' + branch],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
log, err = map(str.strip, p.communicate())

if '#major' in log:
    bump_type = 'major'
    ver[0] += 1
    ver[1] = 0
    ver[2] = 0
elif '#minor' in log:
    bump_type = 'minor'
    ver[1] += 1
    ver[2] = 0
else:
    bump_type = 'patch'
    ver[2] += 1


bumped = '.'.join(map(str, ver))

with open(init, 'w') as f:
    f.write(contents[:start] + bumped + contents[end:])

p = subprocess.Popen(['git', 'commit', '-m', 'bump version: ' + bump_type, '%s/__init__.py' % module_name],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p.communicate()

p = subprocess.Popen(['git', 'tag', '-a', bumped, '-m', 'branch merged: ' + branch + ' (' + bump_type + ')'],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p.communicate()

