class ev:
    energycharge=0
    demandcharge=0
    totalcharge=0
    def energy_charge(self):
        print("enter yes or no:")
        f=(input("flat slab?"))
        if f=="yes":
            self.energycharge=410/100
        elif f=="no":
            return e.demandcharge()
    
        return self.energycharge 
    def demand_charge(self):
        print("choose option :\n1.For Billing Demand up to contract demand\n2.For Billing Demand in excess of contract demand")
        f1=int(input(""))
        if f1==1:
            self.demandcharge=25
        elif f1==2:
            self.demandcharge=50
        else:
            return e.totalcharge()
        return self.demandcharge



    def total_charge(self):
        self.totalcharge= (self.energycharge)+(self.demandcharge)
        print(self.totalcharge)
    
if __name__== "__main__":

    e=ev()()
    e.energy_charge()
    e.demand_charge()
    e.total_charge()
       