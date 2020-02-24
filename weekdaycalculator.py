import sys
import time
import math

# Author: Niklas Wendt 2020
# Source: https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week#Disparate_variation
# Lang:   German

while True:

    print("###############################################################")
    print("#                                                             #")
    print("#                    Wochentagsrechner 2000                   #")
    print("#                                                             #")
    print("###############################################################")

# Eingabe des Tages, Monats & Jahres 

    print("                                                               ")

    try: 
        d, m, y = input("Geben Sie Tag, Monat und Jahr an (Bsp. 2.2.2020): ").split(".")
    except ValueError:
        print("Sie haben ein falsches Datum eingegeben.")
        sys.exit()
    if len(y)!=4:
        print("Die Jahreszahl ist falsch")
        sys.exit()

# Monat m in julianischen Kalender umrechnenw

    monate = {
             '1' : 11,
             '2' : 12,
             '3' : 1,
             '4' : 2,
             '5' : 3,
             '6' : 4,
             '7' : 5,
             '8' : 6,
             '9' : 7,
             '10' : 8,
             '11' : 9,
             '12' : 10 }

#print(type(monate))
 
    monat = monate[m]

#print(monat)

# Datumsausgabe
    print("                                                               ")
    print("###############################################################")
    print("                                                               ")
    print("Ihr eingebenes Datum lautet:")
    print(d+"."+m+"."+y)
#print(type(d))

# Umwandlung der Stringeingabe in float

    jz = y[2] #jahrzehnt
    j = y[3] #jahr
    d = int(d)
    m = int(m)
    j = int(j)
    jz = int(jz)*10
    yy = j + jz
    e = 20 # c = 20 gilt für Zeitraum März 2000 bis Februar 2100

    print("                                                               ")
    print("###############################################################")

#Wenn der Monat Januar oder Februar ist: Jahr --> -1

    if monat>10:
        jahr = yy-1
    else:
        jahr = yy

# Berechnung des Wochentages

    a = math.floor(2.6*monat - 0.2)
    b = math.floor(jahr/4)
    c = math.floor(e/4)

    A = d + a + jahr + b + c - 2*e
    w = A%7

#print(w)

    def f(w):
        return {
            0 : "Sonntag",
            1 : "Montag",
            2 : "Dienstag",
            3 : "Mittwoch",
            4 : "Donnerstag",
            5 : "Freitag",
            6 : "Samstag"
        }[w]

    print("                                                               ")
    print("Der "+str(d)+"."+str(m)+"."+str(y)+" ist ein: "+f(w))
    print("                                                               ")
    print("###############################################################")
    print("                                                               ")
    print("Wollen Sie \n[1] Einen weiteren Wochentag berechnen \n[2] Das Programm beenden")
    print("                                                               ")
    while True:
        auswahl = input()
        if auswahl=='1':
            print("                                                               ")
            break
        elif auswahl=='2':
            time.sleep(5)
            sys.exit()
            break
        else:
            print("                                                               ")
            print("Bitte wählen Sie [1] weiter oder [2] zum beenden")
time.sleep(5)
sys.exit()
