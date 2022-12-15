# sort()
students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78))

grade = lambda grades:grades[1]
sorted_students = sorted(students, key=grade)

for i in sorted_students:
  print(i)




students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr.krabs"]
students.sort(reverse=True)
for i in students:
  print(i)