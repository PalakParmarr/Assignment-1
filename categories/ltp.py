class ltp:
    energycharge=0
    mincharge=0
    print("enter yes or no:")
    def energy_charge(self):
        l= input("flat?")
        if l=="yes":
            self.energycharge=(340/100)
        elif l=="no":
            return e.min_charge()
        return self.energycharge
    def min_charge(self):
        m= input("per BHP?")
        if m == "yes":
            self.mincharge=10
        elif m=="no":
            return e.total_charge()
        return self.mincharge

    def total_charge(self):
        self.totalcharge=self.energycharge+self.mincharge
        
        print(self.totalcharge)
#
#e=ltp()
#e.energy_charge()
#e.min_charge()
#e.total_charge()