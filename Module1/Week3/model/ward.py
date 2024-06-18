from Module1.Week3.model.person import Teacher, Doctor


class Ward:
    def __init__(self, name, community=None):
        if community is None:
            community = []
        self.name = name
        self.community = community

    def add_person(self, person):
        self.community.append(person)

    def describe(self):
        print(f"Ward Name: {self.name}")
        for person in self.community:
            person.describe()

    def count_doctor(self):
        count = 0
        for person in self.community:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.community = sorted(self.community, key=lambda person: person.yob, reverse=True)

    def compute_average(self):
        sum_yob = 0
        count = 0
        for person in self.community:
            if isinstance(person, Teacher):
                sum_yob += person.yob
                count += 1
        sum_yob /= count
        return sum_yob
