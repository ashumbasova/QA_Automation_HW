class Employee:

    def __init__(self, fullName=None, position=None, salary = 0):
        self.fullName = fullName
        self.position = position
        self.salary = salary

    def __str__(self):
        return "fullName: {}, position: {}".format(self.fullName, self.position)

    def name(self):
        nameList = self.fullName.split(" ")
        return nameList[0]
    def surname(self):
        surnameList = self.fullName.split(" ")
        return surnameList[1]

    def income(self, month):
        return self.salary * month



class ITEmployee(Employee):
    '''Class description'''
    def __init__(self, fullName=None, position=None, salary = 0, new_skill=None, years = 0):
        Employee.__init__(self, fullName, position, salary)
        self.skills = []
        self.seniority = ''

    def add_skill(self, new_skill):
        self.skills.append(new_skill)

    def __str__(self):
        return Employee.__str__(self) + "skills: {}".format(self.skills)

    def add_seniority(self, years):
        if 0 <= years <= 3 :
            self.seniority = 'Junior'
        elif 3 < years <= 6:
            self.seniority = 'Middle'
        elif years > 6:
            self.seniority = "Senior"
        return self.seniority + " " + self.position