#!/usr/bin/env  python3

import logging

from libsrg.Runner import Runner

banner_DEBUG = """

######   #######  ######   #     #   #####   
#     #  #        #     #  #     #  #     #  
#     #  #        #     #  #     #  #        
#     #  #####    ######   #     #  #  ####  
#     #  #        #     #  #     #  #     #  
#     #  #        #     #  #     #  #     #  
######   #######  ######    #####    #####   

"""

banner_INFO = """

###  #     #  #######  #######  
 #   ##    #  #        #     #  
 #   # #   #  #        #     #  
 #   #  #  #  #####    #     #  
 #   #   # #  #        #     #  
 #   #    ##  #        #     #  
###  #     #  #        #######  

"""

banner_WARNING = """

#     #     #     ######   #     #  ###  #     #   #####   
#  #  #    # #    #     #  ##    #   #   ##    #  #     #  
#  #  #   #   #   #     #  # #   #   #   # #   #  #        
#  #  #  #     #  ######   #  #  #   #   #  #  #  #  ####  
#  #  #  #######  #   #    #   # #   #   #   # #  #     #  
#  #  #  #     #  #    #   #    ##   #   #    ##  #     #  
 ## ##   #     #  #     #  #     #  ###  #     #   #####   

"""

banner_ERROR = """

#######  ######   ######   #######  ######   
#        #     #  #     #  #     #  #     #  
#        #     #  #     #  #     #  #     #  
#####    ######   ######   #     #  ######   
#        #   #    #   #    #     #  #   #    
#        #    #   #    #   #     #  #    #   
#######  #     #  #     #  #######  #     #  

"""

banner_CRITICAL = """

 #####   ######   ###  #######  ###   #####      #     #        
#     #  #     #   #      #      #   #     #    # #    #        
#        #     #   #      #      #   #         #   #   #        
#        ######    #      #      #   #        #     #  #        
#        #   #     #      #      #   #        #######  #        
#     #  #    #    #      #      #   #     #  #     #  #        
 #####   #     #  ###     #     ###   #####   #     #  #######  

"""

banners: dict[str, str] = {
    'DEBUG': banner_DEBUG,
    'INFO': banner_INFO,
    'WARNING': banner_WARNING,
    'ERROR': banner_ERROR,
    'CRITICAL': banner_CRITICAL,
}


class LevelBanner:
    levs = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    levmap = {'CRITICAL': 50, 'FATAL': 50, 'ERROR': 40, 'WARN': 30, 'WARNING': 30, 'INFO': 20, 'DEBUG': 10, 'NOTSET': 0}

    # logging.getLevelNamesMapping()  # levmap[int]->str
    # {'CRITICAL': 50, 'FATAL': 50, 'ERROR': 40, 'WARN': 30, 'WARNING': 30, 'INFO': 20, 'DEBUG': 10, 'NOTSET': 0}

    @classmethod
    def find(cls, name: str, threshold=logging.WARNING) -> str:
        if isinstance(name, str):
            iname = logging.getLevelName(name)
        else:
            iname = name
        if iname < threshold:
            return ""  # f"All logging below {threshold=}"
        if name in banners:
            return banners[name]
        else:
            return f"Unknown level {name}"

    @classmethod
    def generate(cls):
        # this method used the system banner utility to generate the text arrays pasted above
        for lev in cls.levs:
            print(f'banner_{lev}="""')
            r = Runner(["banner", lev])
            print("\n".join(r.so_lines))
            print('"""')
            print()
        print("banners:dict[str,str]={")
        for lev in cls.levs:
            print(f"   '{lev}':banner_{lev},")
        print("}")

        for lev in cls.levs:
            s = cls.find(lev)
            print(lev, s)


if __name__ == '__main__':
    LevelBanner.generate()
