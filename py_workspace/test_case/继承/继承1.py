# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/10 11:18
# @File 	:继承1.py
# @Software :PyCharm

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def whoAmI(self):
        return 'I am a Person, my name is %s' % self.name


class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name


class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

    def whoAmI(self):
        return 'I am a Teacher, my name is %s' % self.name


import json


class Students(object):
    def read(self):
        return r'["Tim", "Bob", "Alice"]'


s = Students()

print(json.load(s))
s.read()