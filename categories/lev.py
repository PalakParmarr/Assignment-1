class lev:
    energycharge=0
    fixcharge=0
    totalcharge=0
    print("enter yes or no:")
    def fix_charge(self):
        
        f=(input("slab?"))
        if f=="yes":
            self.fixcharge=25
        elif f=="no":
            return l.energy_charge()
        return self.fixcharge
    def energy_charge(self):
        f1=(input("flat slab?"))
        if f1=="yes":
            self.energycharge=420/100
        elif f1=="no":
            return l.total_charge()
        return self.energycharge 
        
    def total_charge(self):
        self.totalcharge= (self.energycharge)+(self.fixcharge)
        print(self.totalcharge)
#        
#l=lev()
#l.energy_charge()
#l.fix_charge()
#l.total_charge()
       