class ltmd2:
    energycharge=0
    fixcharge=0
   #powerfactor=0
    def energy_charge(self):
        charge=int(input("energy charge in kw: "))
        if self.energycharge<=50:
            self.energycharge=(self.energycharge*465)/100
        elif billdemand > 50:
            self.energycharge=(self.energycharge*480)/100
        return self.energycharge
    def fix_charge(self):
        ch=int(input("fix charge in kw :"))
        if self.fixcharge <=50:
            self.fixcharge = self.fixcharge*150
        elif self.fixcharge >50 & self.fixcharge<=70:
            self.fixcharge = self.fixcharge*185
        elif self.fixcharge >70:
            self.fixcharge= self.fixcharge+245
        return self.fixcharge
    def power_factor(self):
        print("1.For each 1 improvement in Power Factor from 90% to 95% 0.15\n 2.For  each 1 above 95% Power Factor\n3.For each 1 decrease in Power Factor below 90%")
        f1=int(input())
        if f1 == 1:
            self.powerfactor=0.15/100
        elif f1 == 2:
            self.powerfactor=0.27/100 
        elif f1 == 2:
            self.powerfactor=3/100 
        else:
            print("wrong choise")
            return h1.power_factor()
        return self.powerfactor
    
    def total_charge(self):
        self.totalcharge= (self.energycharge)+(self.fixcharge)+(self.powerfactor)
        print(self.totalcharge)
        
#l2=ltmd2()
#l2.energy_charge()
#l2.fix_charge()
#l2.power_factor()
#l2.total_charge()