# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning  baholasini kiriting:")
#         baholar[ism] = baho
#     return baholar
    
    
# talabalar = ["Izzatbek", "Tohirjon", "Husanboy"]
# baholar = bahola(talabalar)
# print(baholar)


# def katta_harf(ismlar):
#     return [ism.title() for ism in ismlar]
    
# ismlar = ["izzatbek", "tohirjon", "husanboy"]
# yangi_ismlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)





# def summa(*sonlar):
    
#     return sum(sonlar)
  
# print(summa(100, 2436, 353456, 42364, 54745))


# def summa(x, y, *sonlar):
#     return x + y + sum(sonlar)


# print(summa(2, 3))

# **kvargs
def avto_info(kompanya, model, **malumotlar):
    
    malumotlar['kompanya']=kompanya
    malumotlar['model']=model
    return malumotlar

avto = avto_info("GM", "malibu", rang="qora", yil=2018)
avto2=avto_info("KIA", "K5", rang="qizil", naeh=35000)

print(avto)
print()
print(avto2)