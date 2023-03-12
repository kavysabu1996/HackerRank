"""Given the names and grades for each student in a class of  students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.
"""

if __name__ == '__main__':
    record = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        record.append([name])
        record[i].append(score)
    record_sorted = sorted(record,key= lambda item: item[-1])    
    pop_min = [student for student in record_sorted if student[-1]!=record_sorted[0][-1]]
    second_min = [student[0] for student in pop_min if student[-1]==pop_min[0][-1]]
    for i in sorted(second_min):
        print(i)