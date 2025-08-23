# # def kvadrat_funkiyasi():
# #     son=int(input("Istalgan son kiriting: "))
# #     natija=f"{son}ning kvadrati: {son **2}"
# #     return natija


# # print(kvadrat_funkiyasi())

# # def full_name_func(first_name, last_name):
# #     full_name = f"{first_name,} {last_name}"
# #     return full_name


# # student1 = full_name_func("Muhammadyusuf", "abdusattorov")
# # student2= full_name_func("Husanboy", "shermuhammedov")
# # student3 = full_name_func("Toxirbek", "rustamov")
# # student4 = full_name_func("Izzatbek", "azamov")


# # print(f"darsga kechka qolgan talaba:{student1}. \n vaqtida kelgan talaba: {student2}, {student3}, {student4}")


# # def full_name_func(first_name, last_name, name=''):
# #     if name:
# #         full_name = f"{first_name} {name} {last_name}"
# #     else:
# #         full_name = f"{first_name}  {last_name}"
# #         return full_name.title()


# # student1 = full_name_func("Muhammadyusuf", "abdusattorov")
# # student2= full_name_func("Husanboy", "shermuhammedov")
# # student3 = full_name_func("Toxirbek", "rustamov")
# # student4 = full_name_func("Izzatbek", "azamov")
# # student5 =full_name_func("palonchi", "pistonchiyev", "xojayvich")
# # print(student1) 
# # print(student5)

# def avto_info(kompanya, model, karopka, yili, narx=230000):
#     avto = {
#         'kompanya':kompanya,
#         'model':model,
#         'rangi':rangi,
#         'karopka':karopka,
#         'yili':yili,
#         'narx':narx
#     }
#  return avto

# avto1 = afto_info('GM', 'Malibu', 'qora', "avtomat", 2020)
# avto2 = avto_info('GM', 'Lasetti', 'oq', 'mexanik' 2018, 12000)  

# print("Online savdoda mavjud avtomabillar: ")
# for avto in [avto1, avto2]:
#     if avto ['narx']:
#         print(f"{avto['yili']} {avto['kompaniya']}{avto['model']}, rangi:{avto['rangi']}, karopka:{avto['karopka']}, narx:{avto['narx']}$")
#     alse:
#         print(f"{avto['yili']} {avto['kompanya']}{avto['model']}, rangi:{avto['rangi']}, karopka: {avto['mexanika']}") 
def oraliq(min, max, qadam):
    sonlar=[]
    while min<max:
        sonlar.append(min)
        min  += qadam
        
        
    return sonlar
print(oraliq(1, 51,  2))
print(oraliq(10, 21, 3))