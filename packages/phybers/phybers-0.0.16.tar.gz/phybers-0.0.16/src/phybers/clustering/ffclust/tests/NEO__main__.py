import shlex
import sys
import os
from subprocess import run

print("running")

pathname = os.path.dirname(__file__)
print("path is: " + pathname)
lestr = "python3 " + pathname + "/main.py "
aux = 0
for arg in sys.argv[1:]:
    if (aux == 1):
        print("output path is: " + arg)
        outpath = arg
        aux = 0
    if(arg.startswith('--output-directory')):
        aux = 1
        print("it does")
    print(arg)
    lestr += arg + " "
    
#run([python3, 'main.py', '--infile', 'dir', '--points', '0', '3', '10', '17', '20', '--ks',])
print("lestr is: " + lestr)
#run(shlex.split(lestr))

lestr2 = "python3 " + pathname + "/UtilsTools2.py " + outpath

print("lestr2 is: " + lestr2)

#run(['python3', ])
