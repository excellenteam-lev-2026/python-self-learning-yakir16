import math

def interleaves(*argI):
    l=[]
    endl=False
    for a in range(len(argI[0])):
        for b in range(len(argI)):
            if a==len(argI[b])-1:
                endl=True
            l.append(argI[b][a])
        if endl==True:
            break

    return(l)

if __name__ == "__main__":
    interleaves()