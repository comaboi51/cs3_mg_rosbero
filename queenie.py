class person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hello, my name is {self.name}."    

class nurse(person):
    def __init__(self, name,license_number):
        super().__init__(name)
        self.license_number = license_number

    def introduce(self):
        print(f"Hello, my name is {self.name} and my license number is {self.license_number}.")

    def assist(self, student):
        print(f"nurse {self.name} is assisting  {student.name}")

    def temperature_check(self, student):
        print(f"nurse {self.name} is checking the temperature of {student.name}")
        return student.medical_record.temperature

class clinic:

    def __init__(self, nurse, student):
        self.nurse = nurse
        self.student = student

    def register_student(self, student):
        self.student.append(student)
        print(f"Student {student.name} has been registered in the clinic.")

class student(person):
    def __init__(self, name, grade_level, temperature):
        super().__init__(name)
        self.grade_level = grade_level
        self.temperature = temperature

    def introduce(self):
        return f"Hello, my name is {self.name} and I am in grade {self.grade_level}."

    class thermometer:

        def __init__(self, temperature):
            self.temperature = temperature

        def check_status(self):
            if self.temperature <= 36.0:
                status = 'Low'
            elif 36.0 < self.temperature <= 37.5:
                status = 'Normal'
            else:
                status = 'Fever'
            return status

    def medical_record(self):
        thermometer = self.thermometer(self.temperature)
        status = thermometer.check_status()
        return f"{self.name}'s temperature is {self.temperature}°C, which is considered {status}."


nurse1 = nurse("Nyen", "8970")
student1 = student("microwavve", "67890", 67.5)
student2 = student("laptop", "54321", 98.6)

clinic1 = clinic(nurse1, [student1, student2])
print(clinic1.register_student(student1))
print(student1.medical_record())

#imsosorry ToT