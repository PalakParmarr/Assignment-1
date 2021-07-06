class nonrgp:
    energycharge=0
    fixcharge=0
    totalcharge=0
    def energy_charge(self):
        self.energycharge=input("flat?")
        if self.energycharge =="yes":
            self.energycharge= 460/100
        return self.energycharge
    def fix_charge(self):
        slab=int(input("enter in kw"))
        if slab <= 5:
            self.fixcharge=70*slab
        elif slab >5 & slab <= 15:
            self.fixcharge=90*slab
        return self.fixcharge

    def total_charge(self):
        self.totalcharge= (self.energycharge)+(self.fixcharge)
        print(self.totalcharge)
#
#n=nonrgp()
#n.energy_charge()
#n.fix_charge()
#n.total_charge()