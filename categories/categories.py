class Rgp:
    energycharge=0
    fixcharge=0
    totalcharge=0
    def energy_charge(self):
        self.energycharge=int(input("Enter Energy usage :"))
        if self.energycharge <=50:
            self.energycharge= (self.energycharge*320)/100
        elif self.energycharge >50 & self.energycharge <=150:
            self.energycharge= (self.energycharge*395)/100
        elif self.energycharge >150:
            self.energycharge= (self.energycharge*500)/100
        else:
           return 0
        return self.energycharge 
    def fix_charge(self):
        fixcharge=int(input("1.single phase\n2.three phase"))
        if fixcharge==1:
           self.fixcharge=25
        elif fixcharge ==2:
           self.fixcharge=65
        return self.fixcharge 
    def total_charge(self):
        echarge=self.energy_charge()
        fcharge=self.fix_charge()
        print(echarge,fcharge)
        self.totalcharge= echarge+fcharge
        print(self.totalcharge)
        return self.totalcharge



class Glp:
    energycharge=0
    fixcharge=0
    totalcharge=0

    def energy_charge(self):
        self.energycharge=int(input("Enter Energy usage in units:"))
        if self.energycharge <=200:
            self.energycharge = ((self.energycharge*410)/100)
            
        elif self.energycharge>200:
           self.energycharge=(self.energycharge*480)
        
        return self.energycharge 

    def fix_charge(self):
        fixcharge=int(input("1.single phase\n2.three phase"))
        if fixcharge==1:
           self.fixcharge=30
        elif fixcharge ==2:
           self.fixcharge=70
    
        return self.fixcharge 

    def total_charge(self):
        echarge=self.energy_charge()
        fcharge=self.fix_charge()
        print(echarge,fcharge)
        self.totalcharge= echarge+fcharge
        print(self.totalcharge)
        return self.totalcharge

class Nonrgp:
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
        echarge=self.energy_charge()
        fcharge=self.fix_charge()
        print(echarge,fcharge)
        self.totalcharge= echarge+fcharge
        print(self.totalcharge)
        return self.totalcharge
class Ltp:
    energycharge=0
    mincharge=0
    print("enter yes or no:")
    def energy_charge(self):
        print("enter yes or no:")
        l= input("flat?")
        if l=="yes":
            self.energycharge=(340/100)
        elif l=="no":
            return 0
        return self.energycharge
    def min_charge(self):
        m= input("per BHP?")
        if m == "yes":
            self.mincharge=10
        elif m=="no":
            return 0
        return self.mincharge

    def total_charge(self):
        echarge=self.energy_charge()
        mcharge=self.min_charge()
        print(echarge,mcharge)
        self.totalcharge= echarge+mcharge
        print(self.totalcharge)
    
class Ltmd1:
    energycharge=0
    fixcharge=0
    powerfactor=0
    def energy_charge(self):
        self.energycharge=int(input("energy charge in kw: "))
        if self.energycharge<=50:
            self.energycharge=(self.energycharge*465)/100
        elif self.energycharge> 50:
            self.energycharge=(self.energycharge*480)/100
        return self.energycharge
    def fix_charge(self):
        self.fixcharge=int(input("fix charge in kw :"))
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
        elif f1 == 3:
            self.powerfactor=3/100 
        else:
            print("wrong choise")
            
        return self.powerfactor

    def total_charge(self):
        echarge=self.energy_charge()
        fcharge=self.fix_charge()
        pfactor=self.power_factor()
        print(echarge,fcharge,pfactor)
        self.totalcharge= echarge+fcharge+pfactor
        print(self.totalcharge)
        return self.totalcharge
        
class Ltmd2:
    energycharge=0
    fixcharge=0
    powerfactor=0
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
            return 0
            
        return self.powerfactor
    
    def total_charge(self):
        echarge=self.energy_charge()
        fcharge=self.fix_charge()
        pfactor=self.power_factor()
        print(echarge,fcharge,pfactor)
        self.totalcharge= echarge+fcharge+pfactor
        print(self.totalcharge)
        return self.totalcharge
class Lev:
    energycharge=0
    fixcharge=0
    totalcharge=0
    print("enter yes or no:")
    def fix_charge(self):
        
        f=(input("slab?"))
        if f=="yes":
            self.fixcharge=25
        elif f=="no":
            return 0
        return self.fixcharge
    def energy_charge(self):
        f1=(input("flat slab?"))
        if f1=="yes":
            self.energycharge=420/100
        elif f1=="no":
            return 0
        return self.energycharge 
        
    def total_charge(self):
        fcharge=self.fix_charge()
        echarge=self.energy_charge() 
        print(fcharge,echarge)
        self.totalcharge= echarge+fcharge
        print(self.totalcharge)
        return self.totalcharge
class Sl:
    enerycharge=0
    def energy_charge(self):
        print("enter yes or no:")
        f=(input("flat slab?"))
        if f=="yes":
            self.energycharge=430/100
            
        elif f=="no":
            return 0
        return self.energycharge

    def total_charge(self):
        echarge=self.energy_charge()
        print(echarge)
        self.totalcharge= echarge
        print(self.totalcharge)
        return self.totalcharge
class Tmp:
    fixcharge=0
    energycharge=0
    
    def fix_charge(self):
        print("enter yes or no:")
        f1=(input("fix charge ----slab?"))
        if f1=="yes":
            self.fixcharge=25   
        elif f1=="no":
            return 0
        return self.fixcharge   

    def energy_charge(self):
        print("enter yes or no:")
        f1=(input("energy charge ----flat slab?"))
        if f1=="yes":
            self.fixcharge=510/100  
        elif f1=="no":
            return 0
        return self.energycharge
        
    def total_charge(self):
        echarge=self.energy_charge()
        fcharge=self.fix_charge()
        print(echarge,fcharge)
        self.totalcharge= echarge+fcharge
        print(self.totalcharge)
        return self.totalcharge
class Htmd1:
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
            return 0
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
            return 0
        return self.powerfactor  
    def tou_charge(self):
        self.toucharge=int(input("enter fix charges:"))
        if self.toucharge <=300:
            self.toucharge = (self.toucharge*80)/100
        elif self.toucharge >300:
            self.toucharge = (self.toucharge*100)/100
        else:
            print("wrong choice")
            return 0
        return self.toucharge
    def night_charge(self):
        print("enter yes or no:")
        f3=(input("night time charge---flat slab?"))
        if f3=="yes":
            self.nightcharge=30/100
        elif f3=="no":
            return 0
        return self.nightcharge

    def total_charge(self):
        echarge=self.energy_charge()
        fcharge=self.fix_charge()
        pfactor=self.power_factor()
        tcharge=self.tou_charge()
        ncharge=self.night_charge()
        print(echarge,fcharge,pfactor,tcharge,ncharge)
        self.totalcharge= echarge+fcharge+pfactor+tcharge+ncharge
        print(self.totalcharge)
        return self.totalcharge
class Htmd2:
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
            return 0
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
            return 0
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
            return 0
        return self.powerfactor
        
        
    def tou_charge(self):
        print("enter yes or no:")
        f4=(input("tou charge---flat slab?"))
        if f4=="yes":
            self.toucharge=60/100
        elif f4=="no":
            return 0
        return self.toucharge
        return self.toucharge
    
    def night_charge(self):
        print("enter yes or no:")
        f5=(input("night time charge---flat slab?"))
        if f5=="yes":
            self.nightcharge=30/100
        elif f5=="no":
            return 0
        return self.nightcharge
    def total_charge(self):
            echarge=self.energy_charge()
            fcharge=self.fix_charge()
            pfactor=self.power_factor()
            tcharge=self.tou_charge()
            ncharge=self.night_charge()
            print(echarge,fcharge,pfactor,tcharge,ncharge)
            self.totalcharge= echarge+fcharge+pfactor+tcharge+ncharge
            print(self.totalcharge)
            return self.totalcharge

class Htmd3:
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
            return 0
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
            return 0
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
            return 0
        return self.powerfactor
        
        
    def tou_charge(self):
        print("enter yes or no:")
        f4=(input("tou charge---flat slab?"))
        if f4=="yes":
            self.toucharge=60/100
        elif f4=="no":
            return 0
        return self.toucharge
    
    def total_charge(self):
        echarge=self.energy_charge()
        fcharge=self.fix_charge()
        pfactor=self.power_factor()
        tcharge=self.tou_charge()
        ncharge=self.night_charge()
        print(echarge,fcharge,pfactor,tcharge,ncharge)
        self.totalcharge= echarge+fcharge+pfactor+tcharge+ncharge
        print(self.totalcharge)
        return self.totalcharge
class Ev:
    energycharge=0
    demandcharge=0
    totalcharge=0
    def energy_charge(self):
        print("enter yes or no:")
        f=(input("flat slab?"))
        if f=="yes":
            self.energycharge=410/100
        elif f=="no":
            return 0
    
        return self.energycharge 
    def demand_charge(self):
        print("choose option :\n1.For Billing Demand up to contract demand\n2.For Billing Demand in excess of contract demand")
        f1=int(input(""))
        if f1==1:
            self.demandcharge=25
        elif f1==2:
            self.demandcharge=50
        else:
            return 0
        return self.demandcharge



    def total_charge(self):
        
        echarge=self.energy_charge()
        dcharge=self.demand_charge()
        print(echarge,dcharge)
        self.totalcharge= echarge+dcharge
        
        print(self.totalcharge)

class Htmd:
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
            return 0
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
            return 0
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
            return 0
        return self.powerfactor
        
    def tou_charge(self):
        print("enter yes or no:")
        f2=(input("tou charge ----flat slab?"))
        if f2=="yes":
            self.toucharge=60/100
        elif f2=="no":
            return 0
        return self.toucharge
    def night_charge(self):
        print("enter yes or no:")
        f3=(input("night time charge---flat slab?"))
        if f3=="yes":
            self.nightcharge=30/100
        elif f3=="no":
            return 0
        return self.nightcharge
    def total_charge(self):
        echarge=self.energy_charge()
        fcharge=self.fix_charge()
        pfactor=self.power_factor()
        tcharge=self.tou_charge()
        ncharge=self.night_charge()
        print(echarge,fcharge,pfactor,tcharge,ncharge)
        self.totalcharge= echarge+fcharge+pfactor+tcharge+ncharge
        print(self.totalcharge)
        return self.totalcharge