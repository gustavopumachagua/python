first_name = "Bro"
last_name = "code"
full_name = first_name + " " + last_name
print("Hello " + full_name)
print(type(full_name))

age = 21
age += 1
print(age)
print("Your age is: "+str(age))
print(type(age))

height = 250.5
print("Your height is: "+str(height)+"cm")
print(type(height))

human = True
print("Are you a human: "+str(human))
print(type(human))

# multiple assignment
# ejemplo 1
name = "Gustavo"
age = 21
attractive = True
print(name)
print(age)
print(attractive)

# ejemplo 2
name, age, attractive = "Pedro", 22, True
print(name)
print(age)
print(attractive)

# ejemplo 3
# Spongebob = 30
# Patrick = 30
# Sandy = 30
# Squidward = 30

Spongebob = Patrick = Sandy = Squidward = 30
print(Spongebob)
print(Patrick)
print(Sandy)
print(Squidward)