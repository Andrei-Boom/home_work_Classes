class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __average_score(self):
        average_score_list = sum(self.grades.values(), [])
        average_score_grade = sum(average_score_list) / len(average_score_list)
        return round(average_score_grade,2)

    def __str__(self):
        res = f'Student' \
              f'\nИмя: {self.name}' \
              f'\nФамилия: {self.surname}' \
              f'\nСредняя оценка за домашние задания: {self.__average_score()}' \
              f'\nКурсы в процессе изучения: {", ".join(map(str, self.courses_in_progress))}' \
              f'\nЗавершенные  курсы: {", ".join(map(str, self.finished_courses))}'
        return res

    def __lt__(self,other):
        if not isinstance(other, Lecturer):
            return 'Not a Lecturer'
        else:
            return self.__average_score() < other._Lecturer__average_score()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):
      def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

      def __str__(self):
          res = f'Reviewer' \
                f'\nИмя: {self.name}' \
                f'\nФамилия: {self.surname} '
          return res

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __average_score(self):
        average_score_list = sum(self.grades.values(), [])
        average_score_grade = sum(average_score_list) / len(average_score_list)
        return round(average_score_grade,2)

    def __str__(self):
        res = f'Lecturer' \
              f'\nИмя: {self.name}' \
              f'\nФамилия: {self.surname}' \
              f'\nСредняя оценка за лекции: {self.__average_score()}  '
        return res

# def who_is_better(class_student,class_lecturer):
#     student = class_student.average_score()
#     lecturer = class_lecturer.average_score()
#     if student > lecturer:
#         print(f'student {class_student.name} {class_student.surname} '
#               f'is better than lecturer {class_lecturer.name} {class_lecturer.surname}')
#     elif student < lecturer:
#         print(f'lecturer {class_lecturer.name} {class_lecturer.surname}'
#               f' is better than student {class_student.name} {class_student.surname}')
#     else:
#         print(f'draw')

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

best_student_2 = Student('Bob', 'Jonson', 'your_gender')
best_student_2.courses_in_progress += ['Python']
best_student_2.courses_in_progress += ['Git']
best_student_2.finished_courses += ['Аналитика и Data Science']

best_student_3 = Student('Jon', 'Smit', 'your_gender')
best_student_3.courses_in_progress += ['Python']
best_student_3.courses_in_progress += ['Git']
best_student_3.finished_courses += ['Введение в программирование']

cool_lector = Lecturer('Max', 'Fry')
cool_lector.courses_attached += ['Python']
cool_lector.courses_attached += ['Git']

cool_lector_2 = Lecturer('Pol', 'Mon')
cool_lector_2.courses_attached += ['Python']
cool_lector_2.courses_attached += ['Git']

best_student.rate_hw(cool_lector, 'Git', 9)
best_student.rate_hw(cool_lector, 'Python', 10)
best_student.rate_hw(cool_lector_2, 'Git', 8)
best_student.rate_hw(cool_lector_2, 'Python', 7)

best_student_2.rate_hw(cool_lector, 'Git', 7)
best_student_2.rate_hw(cool_lector, 'Python', 9)
best_student_2.rate_hw(cool_lector_2, 'Git', 10)
best_student_2.rate_hw(cool_lector_2, 'Python', 10)

best_student_3.rate_hw(cool_lector, 'Git', 8)
best_student_3.rate_hw(cool_lector, 'Python', 8)
best_student_3.rate_hw(cool_lector_2, 'Git', 8)
best_student_3.rate_hw(cool_lector_2, 'Python', 7)

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']
reviewer_1.rate_hw(best_student, 'Python', 10)
reviewer_1.rate_hw(best_student, 'Git', 8)
reviewer_1.rate_hw(best_student_2, 'Python', 9)
reviewer_1.rate_hw(best_student_2, 'Git', 7)
reviewer_1.rate_hw(best_student_3, 'Python', 8)
reviewer_1.rate_hw(best_student_3, 'Git', 9)

reviewer_2 = Reviewer('Mister', 'Black')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']
reviewer_2.rate_hw(best_student, 'Python', 9)
reviewer_2.rate_hw(best_student, 'Git', 9)
reviewer_2.rate_hw(best_student_2, 'Python', 10)
reviewer_2.rate_hw(best_student_2, 'Git', 7)
reviewer_2.rate_hw(best_student_3, 'Python', 7)
reviewer_2.rate_hw(best_student_3, 'Git', 7)

print(f'\n{reviewer_1}')
print(f'\n{reviewer_2}')
print(f'\n{cool_lector}')
print(f'\n{cool_lector_2}')
print(f'\n{best_student}')
print(f'\n{best_student_2}')
print(f'\n{best_student_3}')
print('')
# who_is_better(best_student,cool_lector)
# who_is_better(best_student_2,cool_lector)
# who_is_better(best_student_3,cool_lector_2)

students_list = [best_student,best_student_2,best_student_3]
lecturers_list = [cool_lector,cool_lector_2]

def average_students(list,course):
    grades_list=[]
    courses_list=[]
    for i in list:
        for j, d in i.grades.items():
            if j in course:
                for s in d:
                    grades_list.append(s)
                    courses_list.append(j)
    if course in courses_list:
        average = sum(grades_list) / len(grades_list)
        if list == students_list:
            print(f'Средняя оценка студентов за домашние задания на курсе {course} = {round(average, 2)}')
        elif list == lecturers_list:
            print(f'Средняя оценка лекторов на курсе {course} = {round(average, 2)}')
        else:
            print('Ошибка')
    else:
        print(f'Курс {course} отсутствует')

print('')
average_students(students_list,'Git')
average_students(lecturers_list,'Python')
average_students(lecturers_list,'C+')

print(best_student < cool_lector)
print(best_student_2 < cool_lector_2)
print(best_student_3 < reviewer_2)


