import os, platform
bit = platform.architecture()[0]
def __init__():
if bit == '64bit':
from abar_main import defultchk
defultchk()
elif bit == '32bit':
from abar_main_32 import defultchk
defultchk()
else:
print(bit)
exit()
__init__()
