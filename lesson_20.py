# 1# real_madrid={"Casilas":1,"Sergio":4,"Pepe":3,"Varane":5,"Ronaldo":7,"Bale":9,"Benzema":9}
# 2# print(real_madrid)
# 3# del real_madrid["Varane"]
# 4# print(real_madrid)
# son=1
# ismlar=[]
# while son<=5:
#     print(son,end= '')
#     ism=input("Ismingizni kiriting:")
#     ismlar.append({"id":son,"ism":ism})
#     son=son+1
# print(ismlar)
print("Kiritilgan sonning kvadratini qaytaruvchi dastur")
savol="Istalgan son kiriting:"
savol+="(dasturni toxtatish uchun 'exit'so'zini kiriting)"
qiymat=''
while qiymat !='exit':
    qiymat=input(savol)
    if qiymat!='exit':
        print(float(qiymat)**2)

