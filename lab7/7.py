# Employee
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.id = emp_id

    def get_info(self):
        return f"Сотрудник: {self.name}, ID: {self.id}"

# Manager
class Manager:
    def __init__(self, name, emp_id, department):
        self.name = name
        self.id = emp_id
        self.department = department

    def get_info(self):
        return f"Менеджер: {self.name}, ID: {self.id}, Отдел: {self.department}"

    def manage_project(self):
        return f"{self.name} управляет проектом в отделе {self.department}"


# Technician
class Technician:
    def __init__(self, name, emp_id, specialization):
        self.name = name
        self.id = emp_id
        self.specialization = specialization

    def get_info(self):
        return f"Техник: {self.name}, ID: {self.id}, Специализация: {self.specialization}"

    def perform_maintenance(self):
        return f"{self.name} выполняет техническое обслуживание ({self.specialization})"


# TechManager
class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Manager.__init__(self, name, emp_id, department)
        Technician.__init__(self, name, emp_id, specialization)
        self.team = []  # список подчинённых

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        if not self.team:
            return "Команда пуста"
        return "\n".join(emp.get_info() for emp in self.team)

# Создание сотрудников
employee1 = Employee("имя1", 1)
employee2 = Employee("имя2", 2)
manager = Manager("имя3", 3, "1")
technician = Technician("имя4", 4, "2")
tech_manager = TechManager("имя5", 5, "1", "2")

# Вывод информации
print(employee1.get_info())
print(manager.get_info())
print(technician.get_info())

print(manager.manage_project())
print(technician.perform_maintenance())

# Работа TechManager
tech_manager.add_employee(employee1)
tech_manager.add_employee(employee2)

print("\nПодчинённые TechManager:")
print(tech_manager.get_team_info())

print("\nTechManager может:")
print(tech_manager.manage_project())
print(tech_manager.perform_maintenance())
