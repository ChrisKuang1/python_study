class Student():
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        max_score = 0
        for index, value in enumerate(self.scores):
            if value > max_score:
                max_score = value
        return max_score

hx = Student('韩信',23,[87,67,96])
print(hx.get_name())
print(hx.get_age())
print(hx.get_course())