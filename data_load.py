from student import *


def load_data(filename):
    studentList = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.read().strip().split('\n'):
            line_array = line.split(',')
            studentList.append(Student(line_array))
    return studentList


students = load_data('C:\\Users\DELL\dsaa_pro\data.csv')
count_resident(students)