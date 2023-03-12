# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Example

# The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

# alpha
# beta
if __name__ == '__main__':
    record = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record[name] = score
    sorted_record = sorted(record.items(),key=lambda item:item[-1])
    pop_minimum_score = [student for student in sorted_record if student[-1]!=min(record.values())]
    second_min = [student[0] for student in pop_minimum_score if student[1]==pop_minimum_score[0][1]]
    sorted_min = sorted(second_min)
    for i in sorted_min:
        print(i)