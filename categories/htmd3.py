class htmd3:
    energycharge=0
    fixcharge=0
    powerfactor=0
    toucharge=0
    
    def energy_charge(self):
        print("enter yes or no:")
        f1=(input("flat slab?"))
        if f1=="yes":
            self.energycharge=700/100
        elif f1=="no":
            return h1.energycharge()
        return self.energycharge
       
        
    def fix_charge(self):
        print("choose option")
        print("1.Fix charge/KW of billing Demand/montn\n2.Excess Demand")
        f2=int(input())
        if f2 ==1:
            self.fixcharge = 25
        elif f2 ==2:
            self.fixcharge = 30
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
    
    def total_charge(self):
        self.totalcharge= (self.energycharge)+(self.fixcharge)+(self.powerfactor)+(self.toucharge)
        print(self.totalcharge)
#h3=htmd3()
#h3.energy_charge()
#h3.fix_charge()
#h3.power_factor()
#h3.tou_charge()
#
#h3.total_charge()