import sys
import pip
import subprocess

# install a module
module_name = str(sys.argv[1])

subprocess.check_call(["python", '-m', 'pip', 'install', module_name, '--user'])


# get a list of modules
modules = ''
for item in sys.modules.keys():
    modules = modules + item + "\n"

# safe in a file
f = open(r"C:\Users\location-to-save\file.txt", "w+")
f.write(modules)
f.close()