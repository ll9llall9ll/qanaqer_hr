with open('source.txt', 'r') as file1, open('student.txt', 'r') as file2:
    text1 = file1.read().split()
    text2 = file2.read().split()

unique_words = []
for word in text1:
    if word not in unique_words:
        unique_words.append(word)

words_count = 0
for word in unique_words:
    if word in text2:
        words_count += 1

total = len(unique_words)
a = words_count / total
tokos = a * 100
print(tokos)