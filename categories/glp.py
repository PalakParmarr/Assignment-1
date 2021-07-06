class glp:
    energycharge=0
    fixcharge=0
    totalcharge=0

    def energy_charge(self):
        self.energycharge=int(input("Enter Energy usage in units:"))
        if self.energycharge <=200:
            self.energycharge = ((self.energycharge*410)/100)
            
        elif self.energycharge>200:
           self.energycharge=(self.energycharge*480)
        else:
            print("try again")
            return g.energy_charge()
        return self.energycharge 

    def fix_charge(self):
        fixcharge=int(input("1.single phase\n2.three phase"))
        if fixcharge=="1":
           self.fixcharge=30
        elif fixcharge =="2":
           self.fixcharge=70
        else:
            print("try again")
            return self.fixcharge
        return self.fixcharge 

    def total_charge(self):
        
        self.totalcharge= (self.energycharge)+(self.fixcharge)
        print(self.totalcharge)
      
#g=glp()
#g.energy_charge()
#g.fix_charge()
#g.total_charge()
       
   