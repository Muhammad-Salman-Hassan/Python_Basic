
import random
class Mobile:
    
    def __init__(self, brand, ram, rom):
         self.brand = brand
         self.ram = ram
         self.rom = rom
    @staticmethod
    def lucky_draw(value):
         return random.randint(0,10)

class keypad(Mobile):
    def __init__(self, brand, ram, rom):
        super().__init__(brand, ram, rom)

     # Your code here
touch=keypad(brand="Iphone",ram=64,rom=32)

print(f"Brand={touch.brand},ram={touch.ram}")
list = ['Nokia', 'Iphone', 'Samsung', 'Blackberry']
print(f"Your Lucky draw number is : {Mobile.lucky_draw(list)}")



# class Mobile:

#     total_phones = 0
#     def __init__(self, brand, ram, rom):
#         self.brand = brand
#         self.ram = ram
#         self.rom = rom
#         Mobile.total_phones+=1

#     # Your code here
    
#     #class method on way
#     @classmethod
#     def change_total(cls,ammount):
#         cls.total_phones=ammount



# print(Mobile.total_phones) # Result before changing total_phones
# Mobile.change_total(5) # changing total_phones
# print(Mobile.total_phones) # Result after changing total_phones