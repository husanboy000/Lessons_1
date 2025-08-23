# # son=1
# # while son<=5:
# #     print(son,end='')
# #     son = son+1

# togri_parol = "Izzatbek_11"
# for urunish in  range(5):
#     Kiritilgan_parol = input(f"Parolni kiriting ({urunish+1}-urunish):")    
    
#     if Kiritilgan_parol == togri_parol:
#         print("Parol togri siz muuvoffaqiyatli kirdingiz")
#         break
#     else:
#         if urunish == 4:
#             print("Parolni 5 martta notogri kiritdingiz.Tizm bloklandi.")
#         else:
#             print("Parol notogri .Qayta urunib ko'ring")

# print("kiritilgan sonni kvadratini qaytaruvchi dastur.")
# savol= "Istalgan son kiriting"
# savol="(dasturni toxtatish uchun exit deb yozingt):"

# while True:
#     qiymat=input(savol)
#     if qiymat=="exit":
#         break
#     else:
#         print(float(qiymat)**3)

def salom_ber(ism):
   """salom beruvchi funksiya
   """
    print(f"Assalomu alaykum,hurmatli {ism.title()}")

     
     
salom_ber("Izzatbek")
