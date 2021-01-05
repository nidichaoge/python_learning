cars = ['audi', 'bmw', 'subaru']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

age_0 = 22
age_1 = 18
if age_0 > 21 and age_1 < 20:
    print("01")
if age_0 > 21 or age_1 < 17:
    print("01")

if 'audi' in cars:
    print("audi")
if 'tesla' not in cars:
    print("tesla")

age = 12
if age < 4:
    print(4)
elif age < 18:
    print(18)
else:
    print("other")
