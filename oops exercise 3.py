# class Mobile:

#     def __init__(self, brand, model, country):
#         self.brand = brand
#         self.model = model
#         self.country = country
        
#     @property
#     def manufacture(self):
#         return f"{self.brand} {self.model} was manufactured in {self.country}"
#     # Your code here


# phone1 = Mobile("Iphone", "7plus", "California")
# print(phone1.manufacture)
# phone1.country = "China"
# print(phone1.manufacture)
class Mobile:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    @property
    def fullname(self):
        return f"{self.brand} {self.model}"
    @fullname.setter
    def fullname(self,name):
        first=name.split(' ')
        last=name.split(' ')
        self.first=first
        self.last=last


    # Your code here

phone1 = Mobile("Iphone", "7plus")
print(phone1.fullname)
phone1.fullname = "Samsung S21"
print(phone1.fullname)