import math
import os
import random

def peace_of_cake(prices,optional=[],**argF):
       if prices=={}:
           return 0
       newd={}
       c=0
       for a,b in argF.items():
            if optional != []:
                if (a in optional):
                    pass

            c+=prices[a]*(b/100)

       return c
if __name__ == "__main__":
    peace_of_cake()

