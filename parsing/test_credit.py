import os
import re
import parsing_credit as pc

with os.scandir('.\example') as it:
    for entry in it:
        if entry.name.endswith('.TXT') and entry.is_file():
            print(entry.name)
            if re.search("어멘드", entry.name):
                continue
            print('======={}======='.format(entry.name))
            print(pc.main(entry.path))

            