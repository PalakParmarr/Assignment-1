class htmd:
    energycharge=0
    fixcharge=0
    powerfactor=0
    toucharge=0
    nightcharge=0 
    def energy_charge(self):
        print("enter yes or no:")
        f6=(input("flat slab?"))
        if f6=="yes":
            self.energycharge=355/100
        elif f6=="no":
            return 
        return self.energycharge
    def fix_charge(self):
        print("choose option:")
        print("1.For Billing demand up to and including contract demand\n2.For Billing demand in excess of contract demand")
        f5=int(input())
        if f5 == 1:
            self.fixcharge = 335
        elif f5 == 2:
            self.fixcharge = 385
        else:
            print("wrong choise")
            return h.fix_charge()
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
            return h.power_factor()
        return self.powerfactor
        
    def tou_charge(self):
        print("enter yes or no:")
        f2=(input("tou charge ----flat slab?"))
        if f2=="yes":
            self.toucharge=60/100
        elif f2=="no":
            return h.nightcharge()
        return self.toucharge
    def night_charge(self):
        print("enter yes or no:")
        f3=(input("night time charge---flat slab?"))
        if f3=="yes":
            self.nightcharge=30/100
        elif f3=="no":
            return h.totalcharge()
        return self.nightcharge
    def total_charge(self):
        self.totalcharge= (self.energycharge)+(self.fixcharge)+(self.powerfactor)+(self.toucharge)+(self.nightcharge)
        print(self.totalcharge)
#
#h=htmd()
#h.energy_charge()
#h.fix_charge()
#h.power_factor()
#h.tou_charge()
#h.night_charge()
#h.total_charge()
