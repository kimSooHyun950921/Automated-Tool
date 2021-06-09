import os
import re
import parsing_bl as bl

with os.scandir('..\example\pdf') as it:
    for entry in it:
        if entry.name.endswith('.pdf') and entry.is_file():

            print('======={}======='.format(entry.name))
            print(bl.main(entry.path))