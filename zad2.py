line = """raz dwa 
trzy cztery GvR 232 a"""

word = "Przyklad"

list1 = [10, 'a', -1, 20, 30, 40, 50, 60, 70]

list2 = [12, 7, 333, 8641, 2, 1, 123, -1, 0]

num = 18480466560775

# ZADANIE 2.10
def words_count(line):
    words = line.split()
    return len(words)

print("ZADANIE 2.10:\n", words_count(line))

# ZADANIE 2.11
def word_separate(word):
    return "_".join(word)

print("ZADANIE 2.11:\n", word_separate(word))

# ZADANIE 2.12
def firstchars(line):
    words = line.split()
    return "".join([word[0] for word in words])

def lastchars(line):
    words = line.split()
    return "".join([word[-1] for word in words])

print("ZADANIE 2.12:\n", firstchars(line), lastchars(line))

# ZADANIE 2.13
def words_len(line):
    words = line.split()
    return sum(len(word) for word in words)

print("ZADANIE 2.13:\n", words_len(line))

# ZADANIE 2.14
def longestword(line):
    longestword = ''
    maxlen = 0
    words = line.split()
    for word in words:
        if(len(word) > maxlen):
            maxlen = len(word)
            longestword = word
    return (longestword, maxlen)

ans = longestword(line)
print("ZADANIE 2.14:\n", ans[0], ans[1])

# ZADANIE 2.15
def intstostr(list):
    return "".join(str(num) for num in list if(isinstance(num, int) and num > 0))

print("ZADANIE 2.15:\n", intstostr(list1))

# ZADANIE 2.16
def change_gvr(line):
    return line.replace("GvR", "Guido van Rossum")

print("ZADANIE 2.16:\n", change_gvr(line))

# ZADANIE 2.17
def sort_len(line):
    return sorted(line.split(), key=len)

def sort_alph(line):
    return sorted(line.split())

print("ZADANIE 2.17:\n", sort_len(line), sort_alph(line))

# ZADANIE 2.18
def zerocount(num):
    return str(num).count('0')

print("ZADANIE 2.18:\n", zerocount(num))

# ZADANIE 2.19
def join_nums(list):
    return "".join(str(num).zfill(3) for num in list if(isinstance(num, int) and 0 < num <= 999 ))

print("ZADANIE 2.19:\n", join_nums(list2))

