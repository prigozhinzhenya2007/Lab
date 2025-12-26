#1
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_info(self):
        return f"Сотрудник: {self.name}, ID: {self.emp_id}"


#2
class Manager:
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department

    def manage_project(self):
        return f"{self.name} управляет проектом в отделе {self.department}"

    def get_info(self):
        return f"Менеджер: {self.name}, ID: {self.emp_id}, Отдел: {self.department}"


# 3. Technician
class Technician:
    def __init__(self, name, emp_id, specialization):
        self.name = name
        self.emp_id = emp_id
        self.specialization = specialization

    def perform_maintenance(self):
        return f"{self.name} выполняет техническое обслуживание ({self.specialization})"

    def get_info(self):
        return f"Техник: {self.name}, ID: {self.emp_id}, Специализация: {self.specialization}"


#4–6
class TechManager:
    def __init__(self, name, emp_id, department, specialization):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.specialization = specialization
        self.team = []

    def manage_project(self):
        return f"{self.name} управляет проектом в отделе {self.department}"

    def perform_maintenance(self):
        return f"{self.name} выполняет техническое обслуживание ({self.specialization})"

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        if not self.team:
            return "Подчинённых нет"
        return "\n".join(emp.get_info() for emp in self.team)

    def get_info(self):
        return (
            f"Техменеджер: {self.name}, ID: {self.emp_id}, "
            f"Отдел: {self.department}, Специализация: {self.specialization}"
        )


#7
emp = Employee("имя1", 1)
man = Manager("имя2", 2, "деп1")
tech = Technician("имя3", 3, "спец1")
tech_man = TechManager("имя4", 4, "деп2", "спец2")

print(emp.get_info())
print(man.get_info())
print(tech.get_info())
print(tech_man.get_info())

print(tech_man.manage_project())
print(tech_man.perform_maintenance())

tech_man.add_employee(emp)
tech_man.add_employee(tech)

print("\nКоманда:")
print(tech_man.get_team_info())
