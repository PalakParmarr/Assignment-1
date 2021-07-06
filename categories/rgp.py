class rgp:
    energycharge=0
    fixcharge=0
    totalcharge=0
    print("1.RGP\n2.BPL  ")

    def energy_charge(self):
        self.energycharge=int(input("Enter Energy usage :"))
        if self.energycharge <=50:
            self.energycharge= (self.energycharge*320)/100
        elif self.energycharge >50 & self.energycharge <=150:
            self.energycharge= (self.energycharge*395)/100
        elif self.energycharge >150:
            self.energycharge= (self.energycharge*500)/100
        else:
           print("incorrect")
           return r.energy_charge()
        return self.energycharge 

    def fix_charge(self):
        fixcharge=int(input("1.single phase\n2.three phase"))
        if fixcharge=="1":
           self.fixcharge=25
        elif fixcharge =="2":
           self.fixcharge=65
        return self.fixcharge 

    def total_charge(self):
        self.totalcharge= (self.energycharge)+(self.fixcharge)
        print(self.totalcharge)
#        
#r=rgp()
#r.energy_charge()
#r.fix_charge()
#r.total_charge()
       