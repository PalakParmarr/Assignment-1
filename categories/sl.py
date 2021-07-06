class sl:
    enerycharge=0
    def energy_charge(self):
        print("enter yes or no:")
        f=(input("flat slab?"))
        if f=="yes":
            self.energycharge=430/100
            
        elif f=="no":
            return s.enery_charge()
        print(self.energycharge)
    

#s=sl()
#s.energy_charge()