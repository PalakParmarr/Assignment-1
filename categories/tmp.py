class tmp:
    fixcharge=0
    energycharge=0
    
    def fix_charge(self):
        print("enter yes or no:")
        f1=(input("fix charge ----slab?"))
        if f1=="yes":
            self.fixcharge=25   
        elif f1=="no":
            return t.energycharge()
        return self.fixcharge   

    def energy_charge(self):
        print("enter yes or no:")
        f1=(input("energy charge ----flat slab?"))
        if f1=="yes":
            self.fixcharge=510/100  
        elif f1=="no":
            return t.totalcharge()
        return self.energycharge
        
    def total_charge(self):
        self.totalcharge= self.fixcharge+self.energycharge
        print(self.totalcharge)
#
#t=tmp()
#t.fix_charge() 
#t.energy_charge() 
#t.total_charge() 