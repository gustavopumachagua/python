# scope
name = "Bro" # global scope

def display_name():
  name = "Code" # local scope
  print(name)

display_name()
print(name)