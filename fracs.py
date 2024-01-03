import math

def reduce_fraction(frac):
    common = math.gcd(frac[0], frac[1])

    frac[0] = frac[0] // common
    frac[1] = frac[1] // common

    return frac

def is_valid(*args):
    for frac in args:
        if len(frac) > 2 or len(frac) <= 1:
            raise ValueError("Wrong number of values")
        if frac[1] == 0:
            raise ValueError("Denominator can't be 0")
        if isinstance(frac[0], float) or isinstance(frac[1], float):
            raise ValueError("Values aren't ints")

def add_frac(frac1, frac2):        # frac1 + frac2
    is_valid(frac1, frac2)

    ans = [frac1[0] * frac2[1] + frac1[1] * frac2[0], frac1[1] * frac2[1]]

    return reduce_fraction(ans)

def sub_frac(frac1, frac2):        # frac1 - frac2
    is_valid(frac1, frac2)
    
    ans = [frac1[0] * frac2[1] - frac1[1] * frac2[0], frac1[1] * frac2[1]]

    return reduce_fraction(ans)
    
def mul_frac(frac1, frac2):        # frac1 * frac2
    is_valid(frac1, frac2)
    
    ans = [frac1[0] * frac2[0], frac1[1] * frac2[1]]

    return reduce_fraction(ans)

def div_frac(frac1, frac2):        # frac1 / frac2
    is_valid(frac1, frac2)
    
    ans = [frac1[0] * frac2[1], frac1[1] * frac2[0]]

    return reduce_fraction(ans)

def is_positive(frac):             # bool, czy dodatni
    if (frac[0] > 0 and frac[1] > 0) or (frac[0] < 0 and frac[1] < 0): return True
    return False

def is_zero(frac):                 # bool, typu [0, x]
    return frac[0] == 0

def cmp_frac(frac1, frac2):        # -1 | 0 | +1
    num1 = frac2float(frac1)
    num2 = frac2float(frac2)
    if(num1 == num2): return 0
    elif(num1 > num2): return -1
    else: return 1

def frac2float(frac):              # konwersja do float
    return frac[0] / frac[1]
