class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _a_grade(self):

        sum = 0
        number_classes = 0
        for course, grades in self.grades.items():
            for grade in grades:
                sum += grade
                number_classes += 1
        return sum / number_classes

    def _current_grade(self):
        grade_str = []
        for grade in self.grades:
            grade_str.append(grade)
        return grade_str

    def __str__(self):
        res = f'Имя:  {self.name} \nФамилия:  {self.surname} \nСредняя оценка за лекции: {round(self._a_grade(), 1)}\nКурсы в процессе изучения: {", ".join(self._current_grade())}\n  ** Для самопроверки \nСловарь курсов и оценок: {self.grades}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _a_grade(self):

        sum = 0
        number_classes = 0
        for course, grades in self.grades.items():
            for grade in grades:
                sum += grade
                number_classes += 1

        return sum / number_classes

    def __str__(self):
        res = f'Имя:  {self.name} \nФамилия:  {self.surname} \nСредняя оценка за лекции: {round(self._a_grade(), 1)}\n ** Для самопроверки \nСловарь курсов и оценок: {self.grades}'
        return res
    def __lt__(self, other):
        return self._a_grade() < other._a_grade()


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
        res = f'Имя:  {self.name} \nФамилия:  {self.surname}'
        return res


student_1 = Student('Student_surname_1', 'Student_name_1', 'man')
student_2 = Student('Student_surname_2', 'Student_name_2', 'man')

student_1.courses_in_progress += ['Python', 'Git']
student_2.courses_in_progress += ['Git', 'Python']

lecturer_1 = Lecturer('Lecturer_surname_1', 'Lecturer_name_1')
lecturer_2 = Lecturer('Lecturer_surname_2', 'Lecturer_name_2')

lecturer_1.courses_attached += ['Python', 'Git']
lecturer_2.courses_attached += ['Git', 'Python']

reviewer_1 = Reviewer('Reviewer_surname_1', 'Reviewer_name_1')
reviewer_2 = Reviewer('Reviewer_surname_2', 'Reviewer_name_2')

reviewer_1.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git', 'Python']

reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Python', 2)
reviewer_2.rate_hw(student_1, 'Git', 3)

reviewer_1.rate_hw(student_2, 'Python', 5)
reviewer_2.rate_hw(student_2, 'Python', 5)
reviewer_2.rate_hw(student_2, 'Git', 5)

print('*****')

student_1.rate_lecturer(lecturer_1, 'Python', 7)
student_1.rate_lecturer(lecturer_1, 'Python', 4)
student_1.rate_lecturer(lecturer_1, 'Git', 10)

student_2.rate_lecturer(lecturer_2, 'Python', 7)
student_2.rate_lecturer(lecturer_1, 'Python', 4)
student_2.rate_lecturer(lecturer_2, 'Git', 10)

print(student_2)
print('')
print(student_1)
print('')
print('')
print(lecturer_1)
print(lecturer_2)
print('')
print('')
print('***Сравнение***')
print(lecturer_1 < lecturer_2)
student_list = [student_1, student_2]


def a_grade_student(list, course):
    sum = 0
    number = 0
    for student in list:
        for grade in student.grades[course]:
            sum += grade
            number += 1
    return print(f"Средняя оценка cтудентов по курсу {course} = {sum / number}")


a_grade_student(student_list, "Python")

lecturer_list = [lecturer_1, lecturer_2]


def a_grade_lecturer(list, course):
    sum = 0
    number = 0
    for lecturer in list:
        for grade in lecturer.grades[course]:
            sum += grade
            number += 1
    return print(f"Средняя оценка лекторов по курсу {course} = {sum / number}")


a_grade_lecturer(lecturer_list, "Python")
