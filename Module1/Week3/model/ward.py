from Module1.Week3.model.person import Teacher, Doctor


class Ward:
    def __init__(self, name, community=None):
        if community is None:
            community = []
        self.__name = name
        self.__community = community

    def add_person(self, person):
        self.__community.append(person)

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for person in self.__community:
            person.describe()

    def count_doctor(self):
        count = 0
        for person in self.__community:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.__community = sorted(self.__community, key=lambda person: person.get_yob(), reverse=True)

    def compute_average(self):
        sum_yob = 0
        count = 0
        for person in self.__community:
            if isinstance(person, Teacher):
                sum_yob += person.get_yob()
                count += 1
        sum_yob /= count
        return sum_yob
