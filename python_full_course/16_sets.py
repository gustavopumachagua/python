# set
utensils = {"fork", "spoon", "knife", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")
utensils.remove("fork")
#utensils.clear()
utensils.clear()
dishes.update(utensils)
dinner_table = utensils.union(dishes)
print(dishes.difference(utensils))
print(utensils.intersection(dishes))

for x in utensils:
  print(x)

for x in dishes:
  print(x)

for x in dinner_table:
  print(x)