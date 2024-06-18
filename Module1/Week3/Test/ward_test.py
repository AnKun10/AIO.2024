from Module1.Week3.model.person import Student, Teacher, Doctor
from Module1.Week3.model.ward import Ward

# Part (a)
student1 = Student(name="StudentA", yob=2010, grade="7")
student1.describe()
teacher1 = Teacher(name="TeacherA", yob=1969, subject="Math")
teacher1.describe()
doctor1 = Doctor(name="DoctorA", yob=1945, specialist="Endocrinologists")
doctor1.describe()

# Part (b)
print()
teacher2 = Teacher(name="TeacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

# Part (c)
print(f"\nNumber of doctors: {ward1.count_doctor()}")

# Part (d)
print("\nAfter sorting Age of Ward1 people")
ward1.sort_age()
ward1.describe()

# Part (e)
print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")
