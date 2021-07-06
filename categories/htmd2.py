class htmd2:
    energycharge=0
    fixcharge=0
    powerfactor=0
    toucharge=0
    nightcharge=0 
    def energy_charge(self):
        print("enter yes or no:")
        f1=(input("flat slab?"))
        if f1=="yes":
            self.energycharge=30/100
        elif f1=="no":
            return h1.energycharge()
        return self.energycharge
       
        
    def fix_charge(self):
        print("choose option")
        print("1.Fix charge/KW of billing Demand/montn\n2.Excess Demand")
        f2=int(input())
        if f2 ==1:
            self.fixcharge = 225
        elif f2 ==2:
            self.fixcharge = 285
        else:
            print("wrong choise")
            return h2.fix_charge()
        return self.fixcharge        
       
    def power_factor(self):
        print("1.For each 1 improvement in Power Factor from 90% to 95% 0.15\n 2.For  each 1 above 95% Power Factor\n3.For each 1 decrease in Power Factor below 90%")
        f3=int(input())
        if f3 == 1:
            self.powerfactor=0.15/100
        elif f3 == 2:
            self.powerfactor=0.27/100 
        elif f3 == 2:
            self.powerfactor=3/100 
        else:
            print("wrong choise")
            return h1.power_factor()
        return self.powerfactor
        
        
    def tou_charge(self):
        print("enter yes or no:")
        f4=(input("tou charge---flat slab?"))
        if f4=="yes":
            self.toucharge=60/100
        elif f4=="no":
            return h1.totalcharge()
        return self.toucharge
        return self.toucharge
    
    def night_charge(self):
        print("enter yes or no:")
        f5=(input("night time charge---flat slab?"))
        if f5=="yes":
            self.nightcharge=30/100
        elif f5=="no":
            return h1.totalcharge()
        return self.nightcharge

    def total_charge(self):
        self.totalcharge= (self.energycharge)+(self.fixcharge)+(self.powerfactor)+(self.toucharge)+(self.nightcharge)
        print(self.totalcharge)

#h2=htmd2()
#h2.energy_charge()
#h2.fix_charge()
#h2.power_factor()
#h2.tou_charge()
#h2.night_charge()
#h2.total_charge()
