from pathlib import Path
import platform

system = platform.system()
print(system)
print(Path.home())
# Linux
# /home/david

print(platform.version())

# -------

import distro
print(distro.id())


from subprocess import Popen

Popen(["dolphin", "/home"])