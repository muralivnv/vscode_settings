from subprocess import check_output
from os import system
from sys import argv

search_type = "--search-file-content"
if len(argv) > 1:
  search_type = argv[1]

def search_inside_files():
  return "rg --line-number \"\\w*\" | fzf"

def search_filenames():
  return "fzf"

cmd = {}
cmd["--search-file-content"] = search_inside_files
cmd["--search-files"]        = search_filenames

#%%
try:
  file = check_output(cmd[search_type](), shell=True)
  file = file.decode("utf-8")
  file = ':'.join(file.split(':')[0:2])
  system("code -g {0}".format(file))
except:
  pass