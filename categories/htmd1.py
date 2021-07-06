class htmd1:
    energycharge=0
    fixcharge=0
    powerfactor=0
    toucharge=0
    nightcharge=0 
    def energy_charge(self):
        self.energycharge=int(input("Enter Energy usage in units:"))
        self.energycharge = ((self.energycharge*455)/100)
       
        return self.energycharge
    def fix_charge(self):
        self.fixcharge=int(input("enter fix charges:"))
        if self.fixcharge <=1000:
            self.fixcharge = self.fixcharge*260
        elif self.fixcharge >1000 & self.fixcharge <=2000:
            self.fixcharge = self.fixcharge*335
        elif self.fixcharge >2000:
            self.fixcharge = self.fixcharge*385
        else:
            print("wrong choice")
            return h1.fix_charge()
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
        
        
    def tou_charge(self):
        self.toucharge=int(input("enter fix charges:"))
        if self.toucharge <=300:
            self.toucharge = (self.toucharge*80)/100
        elif self.toucharge >300:
            self.toucharge = (self.toucharge*100)/100
        else:
            print("wrong choice")
            return h1.tou_charge()
        return self.toucharge
    def night_charge(self):
        print("enter yes or no:")
        f3=(input("night time charge---flat slab?"))
        if f3=="yes":
            self.nightcharge=30/100
        elif f3=="no":
            return h1.totalcharge()
        return self.nightcharge

    def total_charge(self):
        self.totalcharge= (self.energycharge)+(self.fixcharge)+(self.powerfactor)+(self.toucharge)+(self.nightcharge)
        print(self.totalcharge)

#h1=htmd1()
#h1.energy_charge()
#h1.fix_charge()
#h1.power_factor()
#h1.tou_charge()
#h1.night_charge()
#h1.total_charge()
