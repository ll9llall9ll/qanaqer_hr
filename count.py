doc_txt = input()
second_txt = input()

with open(doc_txt) as f1:
    file1 = f1.read()

with open(second_txt) as f2:
    file2 = f2.read()

erkarut = len(file1) - 1
for i in range(erkarut):
    erkarut += 1

verj = input()
with open(verj, 'a') as f3:
    f3.write(file1)
    f3.write(file2)

print(f3)