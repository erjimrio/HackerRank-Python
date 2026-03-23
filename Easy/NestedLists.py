if __name__ == '__main__':
    N = int(input())
    students = []
    grades = []
    new_list = []

# create lists

    for i in range (N):
        name = input()
        score = float(input())
        students.append([name, score])
        grades.append(score)
    
# Sort list
    sorted_grades = sorted(set(grades))

# Identify second lowest    
    second_lowest = sorted_grades[1]

# Filter students list
    for student in students:
        if (student[1]== second_lowest):
            new_list.append(student)
        
    sorted_new_list = sorted(new_list)
    
# Print sorted new list    
    for i in sorted_new_list:
        print(i[0])