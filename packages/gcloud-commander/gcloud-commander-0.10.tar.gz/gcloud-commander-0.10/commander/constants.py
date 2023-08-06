import os
import platform

CWD = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
CACHE_DIR = f"{CWD}/cache/"


PLATFORM = platform.system().lower()


OPTIONS = """
ls
cp
mv
rm
""".strip()