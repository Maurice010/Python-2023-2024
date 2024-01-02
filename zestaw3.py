# ZADANIE 3.1
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

print(x, y, result)

# for i in "axby": if ord(i) < 100: print (i)
# POPRAWNIE:
for i in "axby":
    if ord(i) < 100: print(i)

for i in "axby": print (ord(i) if ord(i) < 100 else i)

# ZADANIE 3.2
# L = [3, 5, 4] ; L = L.sort() -> ZLE: lista bedzie miala wartosci None
# x, y = 1, 2, 3 -> ZLE: przypisanie 3 wartosci do 2 zmiennych
# X = 1, 2, 3 ; X[1] = 4 -> ZLE: proba zmiany krotki (immutable)
# X = [1, 2, 3] ; X[3] = 4 -> ZLE: wyjscie poza indeks
# X = "abc" ; X.append("d") -> ZLE: string nie ma append()
# L = list(map(pow, range(8))) -> ZLE: pow() nie ma drugiego argumentu

# ZADANIE 3.3
for i in range(31):
    if i % 3 != 0:
        print(i)

# ZADANIE 3.4
while True:
    try:
        liczba = input("Podaj liczbe rzeczywista: ")
        if liczba.lower() == 'stop':
            break
        liczba = float(liczba)
        print(f"Liczba: {liczba}, Potega: {liczba ** 3}")
    except ValueError:
        print("Niepoprawny typ na wejsciu")

# ZADANIE 3.5
def miarka(x):
    gora = "|"
    dol = "0"
    num = 1

    for i in range(1, x+1):
        if(num < 10):
            dol += "    " + str(num)
        elif(num < 100):
            dol += "   " + str(num)
        elif(num < 1000):
            dol += "  " + str(num)
        elif(num < 10000):
            dol += " " + str(num)
        num += 1
        gora += "....|"
        
    ans = gora + "\n" + dol
    print(ans)

miarka(20)

# ZADANIE 3.6
def prostokat(wiersz, kolumna):
    ans = ""
    for i in range(wiersz * 2 + 1):
        if i % 2 == 0:
            ans += "+---" * kolumna + "+\n"
        else:
            ans += "|   " * (kolumna + 1) + "\n"
    print(ans)

prostokat(2, 4)

# ZADANIE 3.8

def funA(a, b):
    temp = []
    for x in a:
        if x in b and x not in temp:
            temp.append(x)

def funB(a, b):
    temp = []
    for x in a + b:
        if x not in temp:
            temp.append(x)

# ZADANIE 3.9
y = [[],[4],(1,2),[3,4],(5,6,7)],
list(sum(x) for x in y)

# ZADANIE 3.10
roman_nums = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def roman2int(roman):
    ans = 0
    temp_prev = 0

    for i in reversed(roman):
        temp = roman_nums[i]
        if temp < temp_prev:
            ans -= temp
        else:
            ans += temp
        temp_prev = temp

    return ans