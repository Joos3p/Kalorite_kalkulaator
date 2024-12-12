import random
import tkinter as tk
from tkinter import messagebox

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
    valgud = kalorid * 0.25 / 4
    rasvad = kalorid * 0.25 / 9
    süsivesikud = kalorid * 0.5 / 4

    #Tagastab sõnastiku makrotoitainetega
    return {
        "Valgud (g)": round(valgud, 2),
        "Rasvad (g)": round(rasvad, 2),
        "Süsivesikud (g)": round(süsivesikud, 2)
    }

#Juhuslik toidu soovitus päevase kaloraaži täitmiseks
def soovitused(kalorid):
    toiduandmed = {
        "Leib": 250,
        "Sai": 290,
        "Piim": 50,
        "Juust": 350,
        "Vorst": 300,
        "Või": 720,
        "Muna": 155,
        "Kartul": 85,
        "Riis": 130,
        "Šokolaad": 530,
        "Kohv": 2,
        "Must tee": 1,
        "Suhkur": 200,
        "Müsli": 370,
        "Makaronid": 110,
        "Värske kurk": 15,
        "Värske tomat": 20,
        "Marineeritud kurk": 30,
        "Marineeritud kapsas": 20,
        "Tatar": 340,
        "Seamaks": 135,
        "Rõskkoor": 200,
        "Praetud muna": 200,
        "Viinerid": 270,
        "Peekon": 500,
        "Uba tomatikastmes": 90,
        "Jäätis": 200
    }
    valitud = []
    kokku = 0

    while kokku < kalorid:
        toit, kcal = random.choice(list(toiduandmed.items()))
        valitud.append(toit)
        kokku += kcal

    return valitud

#Arvutab kasutaja päevase energiavajaduse ja jaotab selle makrotoitaineteks
def arvuta():
    try:
        sugu = sugu_var.get()
        kaal = float(kaal_entry.get())
        pikkus = float(pikkus_entry.get())
        vanus = int(vanus_entry.get())
        aktiivsus = aktiivsus_var.get()

        
#Trollz
        if kaal > 1000:
            messagebox.showinfo("Tulemus", "Sa pead sisestama enda kaalu, mitte enda ema oma")
            return
        elif kaal > 650:
            messagebox.showinfo("Palju õnne!", "Olete ületanud maailma raskeima inimese rekordi!")
        if pikkus > 500:
            messagebox.showinfo("Tulemus", "Kalkulaator on mõeldud inimestele, mitte kaelkirjakutele")
            return
        elif pikkus > 272:
            messagebox.showinfo("Palju õnne!", "Olete ületanud maailma pikima inimese rekordi!")
        if vanus > 150:
            messagebox.showinfo("Tulemus", "Oled sa elus? Mis on su vanuse saladus?")
            return
        if vanus > 122:
            messagebox.showinfo("Palju õnne!", "Olete ületanud maailma vanima inimese rekordi!")
            
        bmr = harris_benedict_valem(sugu, kaal, pikkus, vanus)
        if isinstance(bmr, str):  #Kontrollib, kas tagastatud väärtus on sõnum, mitte arv
            raise ValueError(bmr)

        energiavajadus = pal_valem(bmr, aktiivsus)
        if isinstance(energiavajadus, str):  #Kontrollib, kas tagastatud väärtus on sõnum 
            raise ValueError(energiavajadus)

        makrod = mak_jaotus(energiavajadus)

        tulemus_text.set(f"Päevane energiavajadus: {round(energiavajadus)} kcal\n"
                         f"Valgud: {makrod['Valgud (g)']} g\n"
                         f"Rasvad: {makrod['Rasvad (g)']} g\n"
                         f"Süsivesikud: {makrod['Süsivesikud (g)']} g")

        toidud = soovitused(round(energiavajadus))
        soovitused_text.set("Soovitused toitudeks: " + ", ".join(toidud))

    except Exception as e:
        messagebox.showerror("Viga", f"Sisendite töötlemine ebaõnnestus: {e}")

#Graafiline liides Tkinteriga
app = tk.Tk()
app.title("Kalorite Kalkulaator")

#Sugu
tk.Label(app, text="Sugu:").pack()
sugu_var = tk.StringVar(value="")
sugu_menu = tk.OptionMenu(app, sugu_var, "mees", "naine")
sugu_menu.pack()

#Kaal
tk.Label(app, text="Kaal (kg):").pack()
kaal_entry = tk.Entry(app)
kaal_entry.pack()

#Pikkus
tk.Label(app, text="Pikkus (cm):").pack()
pikkus_entry = tk.Entry(app)
pikkus_entry.pack()

#Vanus
tk.Label(app, text="Vanus (aastat):").pack()
vanus_entry = tk.Entry(app)
vanus_entry.pack()

#Aktiivsus
tk.Label(app, text="Aktiivsuse tase:").pack()
aktiivsus_var = tk.StringVar(value="")
aktiivsus_menu = tk.OptionMenu(app, aktiivsus_var, "Istuv", "Väike", "Mõõdukas", "Kõrge", "Väga kõrge")  # OptionMenu for activity level
aktiivsus_menu.pack()

#Arvutuse nupp
arvuta_btn = tk.Button(app, text="Arvuta", command=arvuta)
arvuta_btn.pack()

#Tulemus
tulemus_text = tk.StringVar()
tk.Label(app, textvariable=tulemus_text).pack()

#Soovitused
soovitused_text = tk.StringVar()
tk.Label(app, textvariable=soovitused_text).pack()

app.mainloop()
