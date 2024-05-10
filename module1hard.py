grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades_students = {}
st_1 = sum(grades[0])/len(grades[0])
st_2 = sum(grades[1])/len(grades[1])
st_3 = sum(grades[2])/len(grades[2])
st_4 = sum(grades[3])/len(grades[3])
st_5 = sum(grades[4])/len(grades[4])
grades_1 = [st_1, st_2, st_3, st_4, st_5]
students_1 = list(students)
res = students_1.sort() # Сортировка списка по алфавиту
grades_students.update({students_1[0]:grades_1[0]})
grades_students.update({students_1[1]:grades_1[1]})
grades_students.update({students_1[2]:grades_1[2]})
grades_students.update({students_1[3]:grades_1[3]})
grades_students.update({students_1[4]:grades_1[4]})
print(grades_students)
