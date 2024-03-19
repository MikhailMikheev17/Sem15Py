from collections import namedtuple
from pathlib import Path
from logger import log



PATH = Path('C:\\Users\\Михаил\\Desktop', 'экз')
LOG_PATH = Path.cwd() / 'log.txt'


def get_dir_info(path: Path, logfile: Path):
    PathObject = namedtuple('PathObject', ('name', 'extension', 'is_dir', 'parent'))
    parent = path.parts[-1]
    for item in path.iterdir():
        if item.is_file():
            name = item.name[:item.name.rfind('.')]
            extension = item.name[item.name.rfind('.') + 1:]
            entry = PathObject(name, extension, item.is_dir(), parent)
            log(str(entry), logfile)
        else:
            entry = PathObject(item.name, None, item.is_dir(), parent)
            log(str(entry), logfile)

"""пример использования"""

get_dir_info(PATH, LOG_PATH)
