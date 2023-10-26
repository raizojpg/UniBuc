import math
import Huffman

e = {'a':1/3, 'b':1/4, 'c':1/6, 'd':1/6, 'e':1/12}

# Calculati entropia
h = sum([-x*math.log(x,2) for x in e.values()])
print(f"Entropia este {round(h,2)}")

# Hufman encoding
codes = Huffman.encode(e)
print(codes)

# Distanta medie a unui mesaj
d = sum([len(codes[x])*e[x] for x in codes.keys()])
print(f"Distanta medie este {round(d,2)}")

#Codati mesajul
mesaj="abececdad"
codare=""
for i in mesaj:
    cod=codes[i]
    codare+=cod
print(f"Codarea este {codare}")

#Decodati mesajul (trb sa parcurgem arborele)
mesaj_decodat = ""

#Evaluam cate doua litere
e2={}
for x in e.keys():
    for y in e.keys():
        e2[x+y]=e[x]*e[y]

# Calculati entropia pt e2
h2 = sum([-x*math.log(x,2) for x in e2.values()])
print(f"Entropia este {round(h2/2,2)}")

# Hufman encoding
codes2 = Huffman.encode(e2)

# Distanta medie a unui mesaj
d2 = sum([len(codes2[x])*e2[x] for x in codes2.keys()])
print(f"Distanta medie este {round(d2/2,2)}")

#observ ca daca impart la 2 imi da valorile asteptate, dar nu inteleg dc e asta necesar