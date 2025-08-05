# # # # kun=input("bugun qaysi kun?>>")
# # # # if kun.lower() == "shanba"or kun.lower() == "yakshanba":
# # # #     print("bugun dam olish kuni!")
# # # # else:
# # # #     print("bugun ish kuni!")
# # # kun=input("bugun qaysi kun?>>")
# # # if kun.lower()!= "shanba"andkun.lower()!="yakshanba":
# # #     print("bugun dam olish kuni!")
# # # else:
# # #     print("bugun ish kuni!")

# # kun=input("bugun qanaqa kun ?>>")
# # harorat = int(input("Bugun havo harorati qanday? >>"))

# # if kun.lower() == "yakshanba" and harorat >= 30:
# #     print("Cho'milishga ketdik!")
    
# # elif kun.lower() == "yakshanba" and harorat < 30:
# #     print("Bugun havo sovuq, uyda qolamiz!")
    
# # else:
# #     print("Bugun ish kuni!")
# narh=15000
# choy=True
# salat=False

# if choy and salat:
#     narh=narh+10000
    
# elif choy or salat:
#     narh=narh+5000
    
# print(f"Jami {narh} so'm")

narh=15000
choy=True
salat=False
non=True
kampot=False
asarti=True

if choy:
    narh=narh+3000
if salat:
    narh=narh+5000
if non:
    narh=narh+2000
if kampot:
    narh=narh+5000
if asarti:
    narh=narh+15000
    
print(narh)