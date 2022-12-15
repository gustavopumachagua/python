# file detection
import os
path = "./test.txt"
if os.path.exists(path):
  print("That location exists!")
  if os.path.isfile(path):
    print("That is a file")
else:
  print("That location doesn't exist!")



# archivo detection
import os
path = "./test"
if os.path.exists(path):
  print("That location exists!")
  if os.path.isfile(path):
    print("That is a file")
  elif os.path.isdir(path):
    print("That is a directory!")
else:
  print("That location doesn't exist!")