import os
import re
import parsing_credit as pc

with os.scandir('.\example') as it:
    for entry in it:
        if not entry.name.endswith('.txt') and entry.is_file():
            if re.search("어멘드", entry.name):
                continue
            print('======={}======='.format(entry.name))

            print(pc.main(entry.path))

            