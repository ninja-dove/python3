# želimo izpisati vse elemente s seznama, zato bomo uporabili 'for loop' (pazi, da za ukazom for uporabiš dvopičje:).
# pri tem mu lahko damo več ukazov, ki jih zamaknjene pišemo v vsako vrsto posebej, izvedli pa se bodo vsi za vsak element posebej.
#vse kar pišemo za temi ukazi v naslednje vrste brez tabulatorja/zamika, se potem izvede kot običajno, ne pa za vsak element posebej
magicians = ["alice", "david", "carolina"]
magicians_new = []
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    magicians_new.append(magician.title())

print(magicians_new)


# če želimo, da nam program izpiše števila v določenem razponu, uporabimo funkcijo range():
# pri tem pazimo, ker se pri drugem številu loop utavi in ga ne zapiše, torej v našem primeru izpiše števila od 1 do 4. Če mu podamo samo eno število, bo začel šteti od 0 in se ustavil pri določenem številu.
for value in range (1, 5):
    print(value)

# števila, ki jih dobimo z uporabo funkcije range, lahko dodamo na seznam:
stevilski_seznam = list(range(1, 6))
print(stevilski_seznam)

#funkciji range lahko dodamo tudi tretji parameter, ki programu ukaže, kakšen preskok med števili naj naredi - npr. vsako drugo število, vsako tretje ipd.:
liha_stevila = list(range(1, 11, 2))
soda_stevila = list(range(0, 12, 2))
print(liha_stevila)
print(soda_stevila)

# naredimo primer, kako bi ustvarili seznam kvadratov števil od 1 do 10:
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
#ali...
squares2 = []
for value in range(1, 11):
    squares2.append(value**2)
print(squares2)

