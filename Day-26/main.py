# import random
# names = ["Angela", "Beth", "Caronline", "Nanda", "Avni", "Elanor", "Freddie"]
# newname = [name.upper() for name in names if len(name) > 4]
# print(newname)

# students_scores = {
#     student : random.randint(0, 100) for student in names
# }
# print(students_scores)


# passed_students = {
#     student : score for student, score in students_scores.items() if score >= 60
# }

# print(passed_students)
import pandas as pd
student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
}

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)
print()
# for key, value in student_data_frame.items():
#     # print(key)
#     print(value)

for index, row in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)