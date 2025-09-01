salaries = []
salaries.append(28000)
salaries.append(5000)
salaries.append(6000)
salaries.append(2000)


search = 2000
index = -1
I = 0
for i in salaries:
    if salaries == search:
        index = I
        break
    I += 1
print(index)
salaries.remove(search)
print(salaries)
