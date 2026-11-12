class Perfume:

    def __init__(self, volume: float = 0.0, price: float = 0.0, manufacturer: str = "Невідомо"):
        self.__volume = volume
        self.__price = price
        self.__manufacturer = manufacturer
        self.quantity = 0           
        self.scent = "Невідомо"     

    def get_volume(self):
        return self.__volume

    def get_price(self):
        return self.__price 



    def get_manufacturer(self):
        return self.__manufacturer

    def __str__(self):
        return (f"Парфуми: обєм = {self.__volume} мл, "
                f"ціна = {self.__price} грн, "
                f"виробник = {self.__manufacturer}, "
                f"кількість = {self.quantity}, "
                f"аромат = {self.scent}")

    def __repr__(self):
        return (f"Perfume(volume={self.__volume}, price={self.__price}, "
                f"manufacturer={self.__manufacturer})")

    def __del__(self):
        print(f"Обєкт Perfume ({self.__manufacturer}) знищено.")

def main():
    p1 = Perfume()                                 
    p2 = Perfume(50.0, 1200.0, "Chanel")
    p3 = Perfume(100.0, 2500.5, "Dior")

    p2.quantity = 10
    p2.scent = "Квітковий"
    p3.quantity = 4
    p3.scent = "Деревний"

    for p in (p1, p2, p3):
        print("Обєм (мл):    ", p.get_volume())
        print("Ціна:         ", p.get_price())
        print("Виробник:     ", p.get_manufacturer())
        print("Кількість:    ", p.quantity)
        print("Аромат:       ", p.scent)
        print("str:          ", str(p))
        print("repr:         ", repr(p))
        print("-" * 30)

main()


