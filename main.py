from categories.categories import *


class main:
    def fmain(self):
        try:
            print("TorrentPower")
            print("1. RGP : Residential Purpose (Up to & Including 15KW\n2. GLP : For Hospitals, Schools & Religious Purpose\n3. Non-RGP : Commercial and Industrial Purose (Up to & Including 15Kw\n4. LTP(AG) : For Agricultural Purpose\n5. LTMD 1 : For Residential Purpose(Above 15KW)\n6. LTMD 2 : For Commercial/Industrial Purpose(Above 15KW)\n7. LEV -LT : Electric Vehicle Charging Stations\n8. SL : For Street Light\n9. TMP :  For Temporary Supply(Below 100kw)\n10. HTMD-1 : For High Tension Load (100 kw & Above)\n11. HTMD-2 : For High Tension AMC Pumping Stations\n12. HTMD-3 : For Temporary Supply (100kw & above\n13. EV -HT - Electric Vehicle Charging Stations\n14. HTMD - Metro Traction")
            print("Choose number : ")
            i = int(input())
            while i not in range(1,15):
                print("incorrect choice")
                i=int(input(("choose another number")))
            choise_dict={
                1:Rgp,
                2:Glp,
                3:Nonrgp,
                4:Ltp,
                5:Ltmd1,
                6:Ltmd2,
                7:Lev,
                8:Sl,
                9:Tmp,
                10:Htmd1,
                11:Htmd2,
                12:Htmd3,
                13:Ev,
                14:Htmd,
            }
            obj=choise_dict[i]()       
            obj.total_charge()
        except Exception as e:
            print("try again",e)

m=main()        
m.fmain()
