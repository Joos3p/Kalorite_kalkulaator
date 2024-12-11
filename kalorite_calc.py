import random


print("")
print("Tere! See on kalorite kalkulaator. Autor Stenar Lääne ja Joosep Kurg")
print("")

#Soo määramine ja selle põhjal arvutamine kasutades Harris-Benedicti valemit (Kaal kilogrammides, pikkus sentimeetries, vanus aastates)
def harris_benedict_valem(sugu, kaal, pikkus, vanus):
    bmr = 0
    if sugu == "mees":
        bmr = 88.36 + (13.4 * kaal) + (4.8 * pikkus) - (5.7 * vanus)
    elif sugu == "naine":
        bmr = 447.6 + (9.2 * kaal) + (3.1 * pikkus) - (4.3 * vanus)
    else:
        return 'Sugu peab olema "naine" või "mees"!'
    return bmr


#Keha aktiivsuse tase (PAL)
def pal_valem(bmr, aktiivsuse_tase):
    if aktiivsuse_tase == "Istuv":
        return bmr * 1.2
    elif aktiivsuse_tase == "Väike":
        return bmr * 1.375
    elif aktiivsuse_tase == "Mõõdukas":
        return bmr * 1.55
    elif aktiivsuse_tase == "Kõrge":
        return bmr * 1.725
    elif aktiivsuse_tase == "Väga kõrge":
        return bmr * 1.9
    else:
        return 'Aktiivsuse tase peab olema kas "Istuv", "Väike", "Mõõdukas", "Kõrge" või "Väga kõrge".'
    
    
#Makrotoitainete jaotus (valgud, rasvad, süsivesikud)
def mak_jaotus(kalorid):
    valgud = kalorid * 0.25 // 4
    rasvad = kalorid * 0.25 // 9
    süsivesikud = kalorid * 0.5 // 4
    

#minu testimine
bmr = harris_benedict_valem("mees", 90, 170, 19)
print("Teie energiavajadus päevas on...")
print(round((pal_valem(bmr, "Istuv"))))
print("kalorit.")


