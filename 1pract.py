f = open("chisla.txt", "r")
n = int(input("Введите число:"))
m = 0
while n>0:
    m = m*10 + n%10
    n = n//10
print("Перевернутое число:",m)