# read file
try:
  with open("./test.txt") as file:
    print(file.read())
  print(file.closed)
except FileNotFoundError:
  print("That file was not found :(")




f = open("./test.txt", "r")
print(f.read())
