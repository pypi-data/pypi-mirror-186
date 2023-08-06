#!/usr/bin/env  python3

import argparse
import logging

import libsrg

banner_DEBUG="""

######   #######  ######   #     #   #####   
#     #  #        #     #  #     #  #     #  
#     #  #        #     #  #     #  #        
#     #  #####    ######   #     #  #  ####  
#     #  #        #     #  #     #  #     #  
#     #  #        #     #  #     #  #     #  
######   #######  ######    #####    #####   

"""

banner_INFO="""

###  #     #  #######  #######  
 #   ##    #  #        #     #  
 #   # #   #  #        #     #  
 #   #  #  #  #####    #     #  
 #   #   # #  #        #     #  
 #   #    ##  #        #     #  
###  #     #  #        #######  

"""

banner_WARNING="""

#     #     #     ######   #     #  ###  #     #   #####   
#  #  #    # #    #     #  ##    #   #   ##    #  #     #  
#  #  #   #   #   #     #  # #   #   #   # #   #  #        
#  #  #  #     #  ######   #  #  #   #   #  #  #  #  ####  
#  #  #  #######  #   #    #   # #   #   #   # #  #     #  
#  #  #  #     #  #    #   #    ##   #   #    ##  #     #  
 ## ##   #     #  #     #  #     #  ###  #     #   #####   

"""

banner_ERROR="""

#######  ######   ######   #######  ######   
#        #     #  #     #  #     #  #     #  
#        #     #  #     #  #     #  #     #  
#####    ######   ######   #     #  ######   
#        #   #    #   #    #     #  #   #    
#        #    #   #    #   #     #  #    #   
#######  #     #  #     #  #######  #     #  

"""

banner_CRITICAL="""

 #####   ######   ###  #######  ###   #####      #     #        
#     #  #     #   #      #      #   #     #    # #    #        
#        #     #   #      #      #   #         #   #   #        
#        ######    #      #      #   #        #     #  #        
#        #   #     #      #      #   #        #######  #        
#     #  #    #    #      #      #   #     #  #     #  #        
 #####   #     #  ###     #     ###   #####   #     #  #######  

"""

banners:dict[str,str]={
   'DEBUG':banner_DEBUG,
   'INFO':banner_INFO,
   'WARNING':banner_WARNING,
   'ERROR':banner_ERROR,
   'CRITICAL':banner_CRITICAL,
}

class LevelBanner:
    levs = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    levmap = logging.getLevelNamesMapping()  #levmap[int]->str
    @classmethod
    def find(cls,name:str,threshold=logging.WARNING)->str:
        if logging.getLevelName(name)< threshold:
            return "" # f"All logging below {threshold=}"
        if name in banners:
            return banners[name]
        else:
            return f"Unknown level {name}"



    @classmethod
    def generate(cls):
        # this method used the system banner utility to generate the text arrays pasted above
        for lev in cls.levs:
            print(f'banner_{lev}="""')
            r=libsrg.Runner(["banner",lev])
            print("\n".join(r.so_lines))
            print('"""')
            print()
        print("banners:dict[str,str]={")
        for lev in cls.levs:
            print(f"   '{lev}':banner_{lev},")
        print("}")


if __name__ == '__main__':
    LevelBanner.generate()
