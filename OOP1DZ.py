class book():
    name='name'
    year='year'
    publisher='publisher'
    genre='genre'
    author='author'
    price='price'

    def input_book(self,name,year,publisher,genre,author,price):
        self.name=name
        self.year=year
        self.publisher=publisher
        self.genre=genre
        self.author=author
        self.price=price


    def print_book(self):
        print("Название книги:  ",self.name)
        print("Год выпуска   :  ",self.year)
        print("Издатель      :  ",self.publisher)
        print("Жанр          :  ",self.genre)
        print("Автор         :  ",self.author)
        print("Цена          :  ",self.price)
        print("="*100)


    def get_name(self,name):
        self.name=name


    def set_name(self):
        return self.name


    def  get_year(self, year):
        self.year = year


    def set_year(self):
        return self.year

    def get_publisher(self, publisher):
        self.publisher = publisher


    def set_publisher(self):
        return self.publisher

    def get_genre(self, genre):
        self.genre = genre


    def set_genre(self):
        return self.genre

    def get_author(self, author):
        self.author = author


    def set_author(self):
        return self.author

    def get_price(self, price):
        self.price = price


    def set_price(self):
        return self.price


python1=book()
python1.input_book("Python подробный справочник","2010","Санкт-Петербург Москва Символ","Учебное пособие","Дэвид Бизли","Cкачал бесплатно")
python1.print_book()
python1.get_name("Общетехнический справочник")
print(python1.set_name())
python1.get_year("1982")
print(python1.set_year())
python1.get_publisher("Москва Машиностроение")
print(python1.set_publisher())
python1.get_author("Под ред. Е.А. Скороходова")
print(python1.set_author())
python1.get_price("Подарили")
print(python1.set_price())
print("*"*100)
print("-"*100)
python1.print_book()