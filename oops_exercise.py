class Mobile:
    def __init__(self,name,ram,rom):
        self.name=name
        self.rom=rom
        self.ram=ram
    # def desplay_spec(self,specs):
    #     self.specs=specs
        

model=Mobile("Iphone",4,128)
# mob_spec=model.desplay_spec('7 plus')
#print(f"{model.name}{model.specs} ,{model.ram} GB Ram,{model.rom} GB Rom")
print(f"{model.name},{model.ram},{model.rom}")