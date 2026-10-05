t = 3
while (t < 50):
     print(t)
     t = t + 10


pas = input ("Введите пароль: ")
while (len(pas) < 8):
   print ("Пароль короткий, длина менее 8 символов")
   pas = input ("Введите пароль: ")
else:
   print ("Пароль безопасный, длина более 8 символов")


print("Введите параметры автомобиля по шаблону LADA 2010г 205000км 450000руб")
brand = input("Марка: ")
year = input("Год выпуска: ")
mileage = input("Пробег: ")
price = input("Цена: ")
print(f"Продается автомобиль\nМарка: {brand}\nГод выпуска: {year}\nПробег: {mileage}\nЦена:{price}")



