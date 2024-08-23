grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = [
    "Johnny",
    "Bilbo",
    "Steve",
    "Khendrik",
    "Aaron",
]  # Используется массив, так как множество неупорядочено
average_score = {}
for i, student in enumerate(students):
    average_score[student] = sum(grades[i]) / len(grades[i])
print(average_score)
