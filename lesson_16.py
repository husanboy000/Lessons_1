# # # # menyu=["kabob", "somsa", "baliq", "hoddog", "lavash"]
# # # # ovqat=input("Nima ovqat yeysiz?")

# # # # if ovqat.lower() in menyu:
# # # #     print("Buyurtma qabul qilindi")
    
# # # # else:
# # # #     print("Kechirasiz bunday taom yo'q")

# # # menyu=["somsa", "osh", "qazi", "bishdeks", "sushi", "joja"]
# # # buyurtma=["somsa", "qazi", "kampot"]

# # # for taom in buyurtma:
# # #     if taom not in menyu:
# # #         print(f"Buyurtmangiz {taom} qabul qilindi.")
        
# # #     else:
# # #         print(f"Bunaqa {taom} yoq")
# # menyu=["somsa", "osh", "norn", "qazi", "joja"]
# # ovqat=input("Nima ovqat yisiz? ")

# # if ovqat.lower() not in  menyu:
# #     print("Buyurtmangiz ovqat yoq")
# # else:
# #     print("Buyurtmangiz qabul qilindi")
# son=int(input("istalgan son kiritin ? "))
# for n in range(2,11):
#     if not (son%n):
#         print(f"{son} soni {n} sonigaqoldiqsiz blinadi!")
users=["izzat", "behruz", "muhammadyusuf", "tohir"]
login=input("Yangi login talang: ")

if login in users:
    print("Bu yuzes band, boshqa login tanlang!")
else:
    print("Xush kelibsiz", login.title())