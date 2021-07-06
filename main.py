from categories.rgp import rgp
from categories.glp import glp
from categories.nonrgp import nonrgp
from categories.ltp import ltp
from categories.ltmd1 import ltmd1
from categories.ltmd2 import ltmd2
from categories.lev import lev
from categories.sl import sl
from categories.tmp import tmp
from categories.htmd1 import htmd1
from categories.htmd2 import htmd2
from categories.htmd3 import htmd3
from categories.ev import ev
from categories.htmd import htmd
class main:
    def fmain(self):
        print("TorrentPower")
        print("1. RGP : Residential Purpose (Up to & Including 15KW)")
        print("2. GLP : For Hospitals, Schools & Religious Purpose") 
        print("3. Non-RGP : Commercial and Industrial Purose (Up to & Including 15Kw)")
        print("4. LTP(AG) : For Agricultural Purpose")
        print("5. LTMD 1 : For Residential Purpose(Above 15KW)")
        print("6. LTMD 2 : For Commercial/Industrial Purpose(Above 15KW)")
        print("7. LEV -LT : Electric Vehicle Charging Stations")
        print("8. SL : For Street Light")
        print("9. TMP :  For Temporary Supply(Below 100kw)")
        print("10. HTMD-1 : For High Tension Load (100 kw & Above)")
        print("11. HTMD-2 : For High Tension AMC Pumping Stations")
        print("12. HTMD-3 : For Temporary Supply (100kw & above) ")
        print("13. EV -HT - Electric Vehicle Charging Stations")
        print("14. HTMD - Metro Traction")
        print("Choose number : ")
       
        i = int(input())
        while i not in range(1,15):
            print("incorrect choise")
            i=int(input(("choose another number")))
        choise_dict={
            1:rgp,
            2:glp,
            3:nonrgp,
            4:ltp,
            5:ltmd1,
            6:ltmd2,
            7:lev,
            8:sl,
            9:tmp,
            10:htmd1,
            11:htmd2,
            12:htmd3,
            13:ev,
            14:htmd,
        }
        obj=choise_dict[i]
        obj=obj()
        obj.energy_charge()
        obj.fix_charge()
        obj.total_charge()
        


m=main()
m.fmain()
