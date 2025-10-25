score_table = {
    'A+': 4.5, 'A0': 4.0,
    'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0,
    'D+': 1.5, 'D0': 1.0,
    'F': 0.0
}

result = 0
total_grade = 0

for _ in range(20):
    name, grade, score = input().strip().split()
    grade = float(grade)

    if score != 'P':  # P는 제외
        result += grade * score_table[score]
        total_grade += grade

print(round(result / total_grade,6))
