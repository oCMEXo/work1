N = int(input('Введите количество секунд: \n '))
b = N // 3600
n = 3600 * b
c = (N - n) // 60
a = (N - n) % 60
print(b , c, a)
