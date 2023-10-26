import math
import Huffman

abc = {'a':8.2/100, 'b':1.5/100, 'c':2.8/100, 'd':4.3/100, 'e':13.0/100,
       'f':2.2/100, 'g':2.0/100, 'h':6.1/100, 'i':7.0/100, 'j':0.15/100,
       'k':.77/100, 'l':4.0/100, 'm':2.4/100, 'n':6.7/100, 'o':7.5/100 ,
       'p':1.9/100, 'q':0.1/100, 'r':6.0/100, 's':6.3/100, 't':9.1/100 ,
       'u':2.8/100, 'v':.98/100, 'w':2.4/100, 'x':.15/100, 'y':2.0/100 , 'z':.07/100 }

#Verificam ca suma probabilitatilor este egala cu 1
s= sum([x for x in abc.values()])
print(s)

#Calculam entropia
h = sum([-x*math.log(x,2) for x in abc.values()])
print(f"Entropia este {h}")

#Calculam entropia daca probabilitatile ar fi egale
heql = math.log(26,2)

#Scoatem o litera pt a maximiza entropia : aleg 'e' cu 13/100
abcmax = {}
for x in abc.items():
    if(x[0]!='e'):
        abcmax[x[0]] = x[1] + 13/100/25
hmax = sum([-x*math.log(x,2) for x in abcmax.values()])
print(f"Entropia maximizata este {hmax}")

#Scoatem o litera pt a minimiza entropia : aleg 'z' cu 0.07/100
abcmin = {}
for x in abc.items():
    if(x[0]!='z'):
        abcmin[x[0]] = x[1] + 0.07/100/25
hmin = sum([-x*math.log(x,2) for x in abcmin.values()])
print(f"Entropia minimizata este {hmin}")

#Vreau sa encodez cu Huffman si sa vad lungimea medie
codes = Huffman.encode(abc)
d = sum([len(codes[x])*abc[x] for x in abc.keys()])
print(f"Distanta medie este {d}")

#Mai erau niste chestii cu codul morse

morse = {'._':'A','_...':'B','_._.':'C','_..':'D','.':'E',
         '.._.':'F','__.':'G','....':'H','..':'I','.___':'J',
         '_._':'K','._..':'L','__':'M','_.':'N','___':'O',
         '.__.':'P','__._':'Q','._.':'R','...':'S','_':'T',
         '.._':'U','..._':'V','.__':'W','_.._':'X','_.__':'Y','__..':'Z',
         '.____':'1','..___':'2','...__':'3','...._':'4','.....':'5',
         '_....':'6','__...':'7','___..':'8','____.':'9','_____':'0'}

#Decodati mesajul
mesaj = "._ ... _._. . __ .. ... _ ___" 

def decode(msg):
    mesaj=""
    key=""
    for i in msg:
        if i == ' ':
            mesaj+=morse[key]
            key=""
        else :
            key+=i
    mesaj+=morse[key]        
    return mesaj

mesaj = decode(mesaj)                
print(f"Mesajul decodat este {mesaj}")

#Try decode without spaces -> nu va functiona
mesaj = "._..._._..__.....____" 

def decodes(msg):
    mesaj=""
    key=""
    for i in msg:
        if morse.get(key,"")!="":
            mesaj+=morse[key]
            key=""
        else :
            key+=i
    mesaj+=morse[key]        
    return mesaj

mesaj = decodes(mesaj)                
print(f"Mesajul decodat este {mesaj}")

#Lungimea medie
for x in morse.keys():
    if 'a' <= x <= 'z':
        l = sum([ 1 if y=='.' else 2 for y in x ])
        f = abc[morse[x]]
        d += l+f
print(f"Lungimea medie a codului morse este {d}")