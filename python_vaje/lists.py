# sezname ustvarimo z oglatimi oklepaji
seznam = ["prvi", "drugi", "tretji", "četrti"]
print(seznam)

#elemente s seznama prikkličemo s št. indexa v oglatem oklepaju. pri tem lahko uporabimo tudi metode za string
print(seznam[0].title())
print(seznam[-1].upper())

#tudi tukaj lahko uporabimo f za združevanje
print(f"Danes je {seznam[0].upper()} januar, jutri pa bo {seznam[1].upper()} januar.")

#elemente na seznamu lahko tudi spreminjamo in menjamo:
print(seznam)
seznam[0] = "sedmi"
print(seznam)

#na seznam lahko dodajamo tudi nove elemente. lako tudi ustvarimo prazen seznam in nanj naknadno dodajamo elemente.
seznam.append("devetnajsti")
print(seznam)

#elemente lahko vnesemo na seznam tudi na določeno mesto. v tem primeru se bodo vsi ostali elementi premaknili za en index v desno.
seznam.insert(1, "deseti")
print(seznam)

#elemente z določenega indexa v seznamu zbrišemo takole:
del seznam[1]
print(seznam)

#ko neko vrednost izbrišemo iz seznama, jo lahko hkrati določimo kot vrednost novi var. ta metoda izvrže vrednost, ki je na zadnjem mestu v seznamu, razen če znotraj oklepaja vpišemo številko indexa.
print(seznam)
popped_seznam = seznam.pop()
print(seznam)
print(popped_seznam)

#če ne vemo na katerem indexu je neka vrednost, jo lahko odstranimo z uporabo metode .remove. ta metoda odstrani samo prvi vnos, ki ga zazna, za odstranitev vseh vnosov s to vrednostjo bomo pozneje uporabili loop.
seznam.remove("tretji")
print(seznam)
#lahko odstranimo tudi var z določeno vrednostjo:
odstrani_vnos = ("sedmi")
seznam.remove(odstrani_vnos)
print(seznam)

#tukaj bom samo dodala nekaj stvari na seznam, da jih bo več
seznam.append("dvajseti")
seznam.append("trideseti")
seznam.append("štirideseti")
seznam.append("petdeseti")
print(seznam)

#vnose na seznamu lahko razvrstimo tudi po abecednem vrstnem redu - to nam trajno spremeni vrstni red. to očitno ne deluje za šumnike. pazi, da so vse besede napisane z malo začetnico, ali pa vse z veliko, sicer to ne bo delovalo prvailno.
seznam.sort()
print(seznam)

#za osortiranje v obratnem vrstnem redu naredimo takole:
seznam.sort(reverse=True)
print(seznam)

#kadar želimo samo začasno urediti seznam in ohraniti njegovo prvotno obliko oz. vrstni red, to naredimo z uporabo funkcije sorted:
print(sorted(seznam))
print(seznam)

#če želimo obrniti vrstni red seznama, to naredimo z uporao metode .reverse(). to trajno spremeni seznam, da bo v obratnem vrstnem redu, ne glede na abecedo. če želimo seznam vrniti v prvotno stanje enostavno šeenkrat uporabimo .reverse().
print(seznam)
seznam.reverse()
print(seznam)

#če želimo ugotoviti koliko elementov jena seznamu, oz. kolikšna je dolžina seznama, uporabimo funkcijo len(). to nam pove količino elementov na seznamu, ne pa index zadnjega elementa!
print(len(seznam))

