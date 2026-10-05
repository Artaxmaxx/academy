print("Введите параметры автомобиля по шаблону LADA 2010г 205000км 450000руб")

t = input()

b = t.find(" ")
brand = t[0:b]
print (brand)

y = t.find("г")
year = t[b+1:y+1]
mileage = t[y:y+3]
print (year)

m = t.find("км")
mileage = t[y+2:m+2]
print (mileage)

p = t.find("руб")
price = t[m+3:p+3]
print (price)

print(f"Продается автомобиль\nМарка: {brand}\nГод выпуска: {year}\nПробег: {mileage}\nЦена:{price}")