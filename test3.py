with open('names.txt') as file, open('surnames.txt') as file1:
    a = file.read()
    b = file1.read()
    expenses = a.split('\n')
    incomes = b.split('\n')

names = []
for i in expenses:
    names.append(i)

surnames = []
for i in incomes:
    surnames.append(i)

c = "\n".join(names)
c1 = "\n".join(surnames)

full_names = c + '\n ' + c1
with open('fullnames.txt', 'w') as full_names1:
    full_names1.write(full_names)