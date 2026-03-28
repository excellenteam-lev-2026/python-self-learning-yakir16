import math
import os
import random
import binascii
import re
def parsle_tongue():
    fileName=input("input file image path:")
    with open(fileName, mode='rb') as file:
        while True:
             fileContent = file.read(1024)
             if not fileContent:
                break
             fileS=(bytes.__str__(fileContent))
             positions = [match.start() for match in re.finditer("!", fileS)]
             if positions !=[]:
                 s=''
                 l=[]
                 for index in positions:
                         index-=1
                         while fileS[index].isalpha() and index-1>=0:
                                    s=fileS[index]+s
                                    index-=1
                         if s.islower() and len(s)>=5:
                             s=s+"!"
                             l.append(s)
                             s=''
                         else:
                             s=''
                 yield print(l)

if __name__ == "__main__":
    our_generator = parsle_tongue()
    while True:
        next(our_generator)



#This is the message:
#python!
#isawesome!
#welldone!
#goodjob!