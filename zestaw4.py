# ZADANIE 4.2
def make_ruler(n):
    gora = "|"
    dol = "0"
    num = 1

    for i in range(1, n+1):
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
        
    return(gora + "\n" + dol)

def make_grid(rows, cols):
    ans = ""
    for i in range(rows * 2 + 1):
        if i % 2 == 0:
            ans += "+---" * cols + "+\n"
        else:
            ans += "|   " * (cols + 1) + "\n"
    return(ans)

# ZADANIE 4.3
def factorial(n):
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans

# ZADANIE 4.4
def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    prev = 0
    curr = 1
    for i in range(2, n + 1):
        temp = prev + curr
        prev = curr
        curr = temp
    return curr

# ZADANIE 4.5
L = [1, 2, 3, 4, 5]

def odwracanieIteracyjnie(L, left, right):
    while(left <= right):
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        right -= 1
        left += 1

def odwracanieRekurencyjnie(L, left, right):
    if left >= right:
        return
    temp = L[left]
    L[left] = L[right]
    L[right] = temp
    odwracanieRekurencyjnie(L, left + 1, right - 1)

# ZADANIE 4.6
seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
def sum_seq(sequence):
    ans = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            ans += sum_seq(item)
        else:
            ans += item
    return ans

print(sum_seq(seq))

# ZADANIE 4.7
def flatten(sequence):
    ans = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            ans.extend(flatten(item))
        else:
            ans.append(item)
    return ans

print(flatten(seq))