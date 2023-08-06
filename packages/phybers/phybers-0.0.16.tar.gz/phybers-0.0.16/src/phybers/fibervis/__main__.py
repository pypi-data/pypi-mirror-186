import shlex
import sys
import os
from subprocess import run

pathname = os.path.dirname(__file__)
cmd_str2 = os.path.join(pathname,"FiberVis.py")
fvcore_path = os.path.join(pathname,'FiberVis_core')

if os.name == 'nt':
    os.system('python setup.py build')
    os.system('python setup.py install')
    
elif os.name == 'posix':
    run(['python', 'setup.py', 'build'], cwd=fvcore_path)
    run(['python', 'setup.py', 'install'], cwd= fvcore_path)

print('Running fibervis...')
run(['python3', cmd_str2])
