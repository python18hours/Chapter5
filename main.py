# coding=utf-8
from functools import wraps
import logging


def logged(level, name=None, message=None):
    """
    Question 1: Define a log decorator function
    :param level: level is the logging level
    :param name: name is the logger name
    :param message: message is the log message
    :return:
    """
    def decorate(func):
        log_name = name if name else func.__module__
        logging.basicConfig()
        log = logging.getLogger(log_name)
        log_msg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, log_msg)
            return func(*args, **kwargs)
        return wrapper
    return decorate


@logged(logging.CRITICAL, "example", "add result:  ")
def add(x, y):
    print(x + y)


class Person:
    """
    Question 2: define a basic class Person, which contains name/age...
    """
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personInfo(self):
        print("My name is %s, I'm %d years old and I'm %s" % (self.name, self.age, self.gender))


class Teacher(Person):
    """
    Question 3: Define a teacher class
    """
    def __init__(self, name, age, gender, college, professional):
        super().__init__(name, age, gender)
        self.college = college
        self.professional = professional

    def personInfo(self):
        super().personInfo()
        print("My college is: %s and professional is: %s" % (self.college, self.professional))

    def teachObj(self):
        return "今天讲了如何面向对象设计程序"


class Student(Person):
    """
    Question 4: Define a student class
    """
    def __init__(self, name, age, gender, college, class_name):
        super().__init__(name, age, gender)
        self.college = college
        self.class_name = class_name

    def personInfo(self):
        super().personInfo()
        print("My college is: %s and class_name is: %s" % (self.college, self.class_name))

    def study(self, teacher_obj):
        study_content = teacher_obj.teachObj()
        print("老师，%s，我学会了" % study_content)

    def __str__(self):
        return self.name, self.age, self.gender, self.college, self.class_name


if __name__ == '__main__':
    add(3, 4)
    tea = Teacher("a", 18, "male", "Computer", "AI")
    tea.personInfo()
    stu = Student("bob", 29, "female", "Computer", "二班")
    stu.study(tea)
