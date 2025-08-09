# car0 = {"model":"Gentra",
#         "rang":"qora",
#         "yil":2024,
#         "narh":18000,
#         "km":3000,
#         "karobka":"avtomat",
#         }


# car1 = {"model":"Damas",
#          "rang":"qaymoqrang",
#          "yil":2006,
#          "narh":4000,
#          "km":510023,
#          "karobka":"mehanika",
#          }

# car2 = {"model":"Damas",
#          "rang":"oq",
#          "yil":2022,
#          "narh":8000,
#          "km":42311,
#          "karobka":"mexanika",
#          }

# car=car0
# print(f"{car['model'].title()},\
#     {car['rang']} rang,\
#     {car['yil']}-yil, {car['narh']}$")

# car=car1
# print(f"{car['model'].title()},\
#     {car['rang']} rang,\
#     {car['yil']}-yil, {car['narh']}$")


# car=car2
# print(f"{car['model'].title()},\
#     {car['rang']} rang,\
#     {car['yil']}-yil, {car['narh']}$")

cars=[]

for n in range(10):
    new_car ={
        'model':'BMW m5 f90',
        'rang':'qora',
        'yil':2020,
        'narh':450000,
        'km':7777,
        'karobka':'avtomat'
    }
    
    cars.append(new_car)
    
for car in cars[:3]:
    car['rang'] = 'qizil'
for car in cars[3:6]:
    car['rang']= 'oq'
    
for car in cars[6:]:
    car['rang'] = 'qora'
    
print(cars)

for car in cars[:3]:
    car['narh'] = 300000
    
for car in cars[3:6]:
    car['narh']= 250000
    
for car in cars[6:]:
    car['narh'] = 12000000
print(cars)  


dasturchilar={
    'ali':['pyton', 'c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#'],
    'sardor':['java','go'],
}

print(dasturchilar.keys())
print(dasturchilar.values())


for ism,tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dastulash tillarini biladi:")
    for til in tillar:
        print(til.upper())
        
        
for ism ,tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dastulash tillarini biladi:", end='')
    for til in tillar:
        print(f'{til.upper()}', end='')