class Car():
    '''
    En klass som håller reda på några egenskaper hos en bil.
    '''
    # Metoden __init__, körs alltid då ett objekt skapas

    def __init__(self, brand, color, mileage):
        # Nedanstående variabler kallas för attribut.
        # Alla objekt av klassen Car har egna värden på dessa.
        self.brand = brand
        self.color = color
        self.mileage = mileage

    def get_brand(self):
        '''
        Skriver ut bilmärket
        '''
        #print(self.brand)
        return self.brand

    def set_brand(self, new_brand):
        '''
        Parameter: new_brand | sträng
        Uppdaterar bilmärket om det existerar. Om det inte existerar
        så tilldelas aktuellt objekt märket enligt parametern.
        '''
        self.brand = new_brand
    
    def get_color(self):
        return self.color
    
    def set_color(self, new_color):
        self.color = new_color

    def get_mileage(self):
        return self.mileage
    
    def set_mileage(self, new_mileage):
        self.mileage = new_mileage


# ----------Huvudprogram----------
# Nu när klassen finns kan vi skapa objekt (variabler) med denna typ.
# Dessa objekt har också tillgång till klassens metoder (funktioner).
a_car = Car('Volvo', 'Blå', 1587)
b_car = Car("Toyota", "Röd", 1346)
c_car = Car("Peugeot", "Gul", 982)
d_car = Car("Kia", "Silver", 1987)

my_cars = [a_car, b_car, c_car, d_car]

def menu(car_list):
    available_chocies = [1, 2, 3, 4]
    while True:
        print("1. Model\n2. Färg\n3. Miltal")
        choice = input("Vad vill du skirva ut: ")
        if not choice.isnumeric:
            print("Otillåtet val")
            continue
        else:
            choice = int(choice)
        
        if choice not in available_chocies:
            print("Otillåtet val")
        
        
