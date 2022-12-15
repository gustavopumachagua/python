# zip(*iterables)

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
users = dict(zip(usernames, passwords))
print(type(users))
for key, value in users.items():
  print(key+" : "+value)








usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]
users = zip(usernames, passwords, login_date)
for i in users:
  print(i)