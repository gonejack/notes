import os
import re
from datetime import datetime

date_pattern = re.compile(r"^\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}]")


def mark(directory: str):
    if not os.path.isdir(directory):
        return
    for cur_dir, sub_dirs, filenames in os.walk(directory):
        if cur_dir.endswith('.textbundle') and not date_pattern.match(cur_dir):
            datetime_str = datetime.fromtimestamp(os.stat(cur_dir).st_birthtime).strftime("[%Y-%m-%d %H:%M:%S]")
            parent_dir, basename = os.path.dirname(cur_dir), os.path.basename(cur_dir)
            rename = os.path.join(parent_dir, datetime_str + basename)
            print("%s => %s" % (cur_dir, rename))
            os.rename(cur_dir, rename)


if __name__ == '__main__':
    mark('.')
