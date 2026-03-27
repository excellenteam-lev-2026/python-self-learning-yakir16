import math
import os

def not_the_way():

    Direc = input(r"Enter the path of the folder: ")
    files = os.listdir(Direc)

    files = [f for f in files if os.path.isfile(Direc+'/'+f) and f.startswith("deep")]
    return (files)


if __name__ == "__main__":
    not_the_way()

