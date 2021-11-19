#pip3 install psutil

import psutil
psutil.cpu_percent()
psutil.disk_io_counters()
psutil.net_io_counters()





rsync [Options] [Source-Files-Dir] [Destination]

#1)Copy or sync files locally:
rsync -zvh [Source-Files-Dir] [Destination]

#2)Copy or sync directory locally:
rsync -zavh [Source-Files-Dir] [Destination]

#3)Copy files and directories recursively locally:
rsync -zrvh [Source-Files-Dir] [Destination]

import subprocess
src = "<source-path>" # replace <source-path> with the source directory
dest = "<destination-path>" # replace <destination-path> with the destination directory

subprocess.call(["rsync", "-arq", src, dest])
