#1
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return(f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}")

book = Book("1984", "Джордж Оруэл", 1949)
print(book.get_info())

#2
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return(self.radius)

    def set_radius(self, new_radius):
        self.radius = new_radius

circle = Circle(5)
print("Радиус1:", circle.get_radius())

circle.set_radius(10)
print("Радиус2:", circle.get_radius())
