#1
class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password # приватный атрибут

    def set_password(self, new_password): # задать новый пароль
        self.__password = new_password
        print("Пароль успешно изменён")

    def check_password(self, password): # проверить пароль
        return(self.__password == password)

user = UserAccount("Zhenya1337", "EvgeniyP1337@gmail.com", "Q1w2e3r4") # данные

print(user.check_password("Q1w2e3r4")) # правильный пароль
print(user.check_password("11111")) # неправильный пароль

user.set_password("123456") # новый пароль

print(user.check_password("123456")) # правильный пароль

#2
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return(f"Марка: {self.make}, Модель: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model) # обращение к атрибутам из "материнского" класса
        self.fuel_type = fuel_type

    def get_info(self):
        return(f"Марка: {self.make}, Модель: {self.model}, Тип топлива: {self.fuel_type}") # добавил тип топлива

vehicle = Vehicle("марка1", "модель1")
car = Car("марка2", "модель2", "топливо")

print(vehicle.get_info())
print(car.get_info())
