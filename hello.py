# сранные окончания
n = int(input())
a = n % 10
b = n % 100
if a == 0 or 5 <= a <= 9 or 11 <= b <= 14:
    print (n, 'программистов')
elif a == 1 and b != 11:
    print (n, 'программист')
elif 2 <= a <= 4 and b != 12 and b != 13 and b != 14:
    print(n, 'программиста')
