#z metodo .title nam vse besede v string napiše z velikimi začetnicami, ostale črke so male
message = "hello world!"
print(message.title())

# z metodo .lower damo vse znake v string v male črke, z metodo .upper pa v velike črke
name = "ADA"
print(name.upper())
print(name.lower())

#z uporabo črke f pred string lahko združimo različne spremenljivke v eni string, vendar moramo vsako var dati v zavite oklepaje
first_name = "\nada"
last_name = "\tlovelace"
full_name = f"{first_name} {last_name}"
print(full_name.title())
pozdrav = f"Hello, {full_name.title()}"
print(pozdrav)


#da odstranimo presledke z začetka in konca besedila uporabimo metodo .strip, če želimo odstraniti presledke na začetku vpišemo .lstrip (torej pobere presledke na levi strani -l), za na koncu pa vpišemo .rstrip (torej odstrani presledke z desne strani - r)
favorite_language = " Python Python "
favorite_language = favorite_language.strip()
print(favorite_language)

#lahko odstranimo del besedila na začetku z metodo .removeprefix ali konec besedila z metodo .removesuffix
naslov = "https://www.google.com"
naslov = naslov.removeprefix("https://")
print(naslov)

#za lažje branje številk lahko uporabimo _, ki pa ga py ne izpiše uporabniku
universe_age = 14_000_000_000
print(universe_age)

#lahko določimo več spremenljivk hkrati
x, y, z = 1, 2, 3
print(f"{x} {y} {z}")

#py nima konstante, jih pa lahko ustvarimo/označimo tako, da jih napišemo z velikimi črkami
MAX_CONNECTIONS = 5000

