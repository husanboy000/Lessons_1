
# def avto_info(kompanya, model, rangi, karopka, yili, narx=230000):
#     avto = {
#         'kompanya':kompanya,
#         'model':model,
#         'rangi':rangi,
#         'karopka':karopka,
#         'yili':yili,
#         'narx':narx
#     }
#     return avto

# print("sayitimizdagi avtolar royxatini shakillantiramiz")
# avtolar=[]
# while True:
#     print("\nQuydagi malumotlatni kiriting\n", end="")
#     kompanya=input("Ishlab chiqaruvchi:")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     karobka=input("Karopka turi: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("narx:")
    
#     avtolar.append(avto_info(kompanya,model,rangi,karobka,yili,narhi))
#     javob = input("yana avto qoshasizmi? (yes/no):")
#     if javob.lower() != 'yes':
#         break

# print("Avtomobil tavsifi: ")
# for a in avtolar:
#     print(f"Kompaniyasi: {a['kompanya']}, modeli: {a['Modeli:']}, rangi: {a['Rangi:']}, karopka: {a['Karopka turi:']}, yili: {a['Ishlab chiqarilgan yili:']}, narx: {a['narx:']}")

def user_info(ismi, familyasi, t_yil, t_joy, email=None, telefon=None):
    user={'ismi':ismi,
       'familyasi':familyasi,
       't_yil':t_yil, 
       't_joy':t_joy,
       'email':email,
       'telefon':telefon
       }
    return user


print("foydalanuvchi royxatini shakillantiramiz.")
users = []

while True:
    print("\nQuydagi malumotlarni kirriting\n, end=")
    ismi=input("foydalanuvchi iami:")
    familyasi=input("foydalanuvchi familyasi:")
    t_yil=input("tugilgan yili:")
    t_joy=input("tugilgan joyi:")
    email=input("foydalanuvchini emaili:")
    telefon=input("foydalanuvchining telefon raqami:")
    
    users.append(user_info(ismi, familyasi, t_yil, t_joy, telefon))
    javob=input("yana foydalanuvchi qoshasizmi? (yes/no):")
    if javob.lower() !='yes':
        break
        
print("\nRoyhadagi foydalanuvchilar")
for a in users:
    print(f"foydalanuvch ismi {a['ismi']}, \nfoydalanuvchi familyasi {a['familyasi']}\nfoydalanuvchi t_yili {a['t_yil']}\nfoydalanuvchi t_joyi {a['t_joy']}\nfoydalanuvchi eamil {a['email']}\nfoydalanuvchi telvoni{a['telefon']}")