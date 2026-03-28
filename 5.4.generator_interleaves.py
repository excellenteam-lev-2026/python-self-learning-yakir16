import math

def generator_interleaves(*argI):
    l=[]
    endl=False
    for a in range(len(argI[0])):
        for b in range(len(argI)):
            if a==len(argI[b])-1:
                endl=True
            l.append(argI[b][a])
            yield print(l)
        if endl==True:
            break


if __name__ == "__main__":
    generator_interleaves()
