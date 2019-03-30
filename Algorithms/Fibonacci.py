#Рекурсивный метод обработки
def fibr(n):
    if n<3:
        return 1
    return fibr(n-1) + fibr(n-2)
#Не рекурсивный метод обработки
def fibnr(n):
    x=y=1
    i=2
    while i < n:
        sum = y + x
        x = y
        y = sum
        i += 1
    return sum

print("Recursive = " + str(fibr(10)))
print("NonRecursive = " + str(fibnr(10)))





