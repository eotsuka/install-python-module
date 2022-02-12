# install-python-module
Run this in SQL agent job to install python module for the agent user

use case:
To run a python script using a sql agent job, the python modules sometimes need to be installed on the sql agent user. 
To install python modules for the sql agent user, run this script as a sql agent job. 

Set 

Type: 
Operating system (CmdExec)

Run as: 
SQL Server Agent Service Account

Command: 
path-to-python.exe path-to-python-file name-of-the-module

(example:)
C:\Program Files\Python\Python\python.exe C:\Users\SqlAgent\filelocation\install_module.py pysftp
