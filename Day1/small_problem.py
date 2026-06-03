def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()

    true_count = 0
    for letter in "true":
        true_count += combined_names.count(letter)

    love_count = 0
    for letter in "love":
        love_count += combined_names.count(letter)

    love_score = int(str(true_count) + str(love_count))

    print(f"Your love score is {love_score}")
    return love_score

# calculate_love_score("Angela Yu", "Jack Bauer")

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    if 91 <= student_scores[key] <= 100: student_grades[key] = "Outstanding"
    elif 81 <= student_scores[key] <= 90: student_grades[key] = "Exceeds Expectations"
    elif 71 <= student_scores[key] <= 80: student_grades[key] = "Accepable"
    else: student_grades[key] = "Fail"

print(student_grades)