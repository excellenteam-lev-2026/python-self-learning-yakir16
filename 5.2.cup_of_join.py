import math

def cup_of_join(*args, sep='-'):
    if not args:
        return None
    result = []
    for i, lst in enumerate(args):
        if i > 0:
            result.append(sep)
        result.extend(lst)
    return result

if __name__ == "__main__":
    cup_of_join()


