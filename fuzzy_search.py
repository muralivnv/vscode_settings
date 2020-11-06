from subprocess import check_output
from os import system
from sys import argv

search_type = "--search-file-content"
if len(argv) > 1:
  search_type = argv[1]

#################################################################
folders_to_ignore = ["CMakeFiles"]

def search_inside_files():
  ignore_glob = ''.join(["--iglob \"!**/{}/**\" ".format(f) for f in folders_to_ignore])
  return "rg --line-number {0} \"\\w*\" | fzf --color hl:221,hl+:74".format(ignore_glob)

def search_filenames():
  return "fzf --color hl:221,hl+:74 "
  
#################################################################

cmd = {}
cmd["--search-file-content"] = search_inside_files
cmd["--search-files"]        = search_filenames

try:
  file = check_output(cmd[search_type](), shell=True)
  file = file.decode("utf-8")
  file = ':'.join(file.split(':')[0:2])
  system("code -g {0}".format(file))
except:
  pass