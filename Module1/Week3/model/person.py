class Person:
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob

    def describe(self):
        print(f"{self.__class__.__name__} - Name: {self._name} - YoB: {self._yob}", end='')

    def get_yob(self):
        return self._yob


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.__grade = grade

    def describe(self):
        super().describe()
        print(f" - Grade: {self.__grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        super().describe()
        print(f" - Subject: {self.__subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        super().describe()
        print(f" - Specialist: {self.__specialist}")
