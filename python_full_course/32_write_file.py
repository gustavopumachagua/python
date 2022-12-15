# write file
text = "Yooooooooooo\nThis is some text\nHave a good one!\n"
with open("./test.txt", "w") as file:
  file.write(text)

f = open("./test.txt", "r")
print(f.read())