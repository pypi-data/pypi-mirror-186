shlex import
import sys
import os
from subprocess import run

pathname = os.path.dirname(__file__)
#cextend_dir = os.path.join(pathname,'Framework','CExtend')
cmd_str2 = os.path.join(pathname,"FiberVis.py")
fvcore_path = os.path.join(pathname,'FiberVis_core','setup.py')

if os.name == 'nt':
    os.system('python ' + fvcore_path + 'build')
    os.system('python ' + fvcore_path + 'install')
    
elif os.name == 'posix':
    run(['python', fvcore_path, 'build'])
    run(['python', fvcore_path, 'install'])

'''
if not os.path.exists(os.path.join(pathname,'Framework','CExtend','bundleCFunctions.o')):
    print("bundleCFunctions.o does not exist. Creating it...")
    run(shlex.split("make -C " + cextend_dir))
    if not os.path.exists(os.path.join(pathname,'Framework','CExtend','bundleCFunctions.o')):
        print("bundleCFunctions.o still doesn't exist. Exiting...")
        exit()
    else:
        print("Running fibervis...")
        run(["python3", cmd_str2])
else:
    print("Running fibervis...")
    run(["python3", cmd_str2])
'''

print("Running fibervis...")
run(["python3", cmd_str2])

