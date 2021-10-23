N = int(input('Введите количество секунд: \n '))
hours = N // 3600
sec = 3600 * hours
minutes = (N - sec) // 60
seconds = (N - sec) % 60
print(hours, minutes, seconds)
