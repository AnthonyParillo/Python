
#### BASE GLOB ######
# import glob
# print(glob.glob('/Applications**/V*', recursive=True))


##### NON RECURSIVE #####
import re
import os
import fnmatch
import glob

def find_files(path: str, glob_pat: str, ignore_case: bool = False):
    rule = re.compile(fnmatch.translate(glob_pat), re.IGNORECASE) if ignore_case \
            else re.compile(fnmatch.translate(glob_pat))
    return [n for n in glob.iglob(os.path.join(path, '**'), recursive=True) if rule.match(n)]


print(find_files('/Users/*/Desktop', '*bandname*', ignore_case=True))


##### BEST GLOB ##########
# import os
# import glob


# #  set text to search for 
# searchText = 'Tania'

# #   the root (top of tree hierarchy) to search, remember to change \ to / for Windows
# TOP = '/Users/aparillo/Desktop/'

# found = 0
# for filename in glob.iglob(os.path.join(TOP, '**', f'*{searchText}*'), recursive=True):
#     print ("\nFile {} exists..... \n{}".format(filename, os.path.dirname(filename)))
#     found += 1


# print('\nFile containing \'{}\' found {} times'.format(searchText, found))

#### Install 

# ####### SAME AS ABOVE FNMATCH #####
# #!/usr/bin/env python3
# import os
# import fnmatch


# #  set text to search for 
# searchText = 'Guess'

# #   the root (top of tree hierarchy) to search, remember to change \ to / for Windows
# TOP = 'C:/works'

# found = 0
# for root, dirnames, filenames in os.walk(TOP, topdown=True, onerror=None, followlinks=True):
#     for filename in filenames:
#         if fnmatch.fnmatch(filename, f'*{searchText}*'):
#             print ("\nFile {} exists..... \t\t{}".format(filename, os.path.join(root)))
#             found += 1

# print('\n File containing \'{}\' found {} times'.format(searchText, found))