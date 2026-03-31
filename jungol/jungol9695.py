class House:
    def __init__(self, city, bed, bath):
        self.city = city
        self.bed = bed
        self.bath = bath

city, bed, bath = input().split()
h = House(city, bed, bath)

print(f"location: {h.city}")
print(f"bedrooms: {h.bed}")
print(f"bathrooms: {h.bath}")

###############################################(방법01)

class House:
    def __init__(self, location, bedrooms, bathrooms):      # 생성자
        self.location = location
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms

    def show_info(self):
        print(f"location: {self.location}")
        print(f"bedrooms: {self.bedrooms}")
        print(f"bathrooms: {self.bathrooms}")

data = input().split()
my_house = House(data[0], data[1], data[2])
my_house.show_info()

###############################################(방법02)

class House:
    def __init__(self, city, room, bathroom):
        self.city = city
        self.room = room
        self.bathroom = bathroom

    def print(self):
        # print(city, room, bathroom)
        print("location:", city)
        print("bedrooms:", room)
        print("bathrooms:", bathroom)

city, room, bathroom = input().split()
print(city, room, bathroom)

h1 = House(city, room, bathroom)
h1.print()

###############################################(방법03)


