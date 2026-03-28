import math
import os
from datetime import datetime, timedelta

import random


def no_vinnigrete():
    str_d1=input("The first date:")
    str_d2 = input("The second date:")
    # convert string to date object
    d1 = datetime.strptime(str_d1, "%Y-%m-%d").date()
    d2 = datetime.strptime(str_d2, "%Y-%m-%d").date()

    # difference between dates in timedelta
    delta = d2 - d1
    dateR=d1
    if delta.days < 0:
        delta*=-1
        randD=random.randint(0, delta.days)
        dateR = d2 + timedelta(days=randD)
    elif delta.days > 0:
        randD = random.randint(0, delta.days)
        dateR = d1 + timedelta(days=randD)
    dateV = dateR.strftime("%A")
    print(f'The date is {dateR}')
    if dateV == 'Monday':
        print(f"I don't have vinaigrette!")

if __name__ == "__main__":
        no_vinnigrete()
