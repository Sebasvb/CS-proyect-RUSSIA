#partidos todos contra todos:


def prob_alemania (pais2):
    dicc = {}
    dicc = {"Alemania":1.00,"Arabia_Saudita":0.27,"Argentina":0.60,"Australia":0.10,"Belgica":0.50,"Brasil":0.04,"Colombia":0.34,"Corea del Sur":0.12,"Costa Rica":0.26,"Croacia":0.24,"Dinamarca":0.22,"Egipto":0.23,"España":0.99,"Francia":0.44,"Inglaterra":0.02,"Iran":0.43,"Islandia":0.60,"Japon":0.19,"Marruecos":0.54,"Mexico":0.25,"Nigeria":0.35,"Panama":0.35,"Peru":0.00,"Polonia":0.35,"Portugal":0.62,"Rusia":0.17,"Senegal":0.69,"Serbia":0.62,"Suecia":0.88,"Suiza":0.52,"Tunez":0.49,"Uruguay":0.46}
    return dicc[pais2]
0.87,0.77,0.16,0.47,0.34,0.73,0.53,0.60
def prob_Arabia_Saudita (pais2):
    dicc = {}
    dicc = {"Alemania":0.63,"Arabia_Saudita":1.00,"Argentina":0.66,"Australia":0.29,"Belgica":0.93,"Brasil":0.19,"Colombia":0.91,"Corea del Sur":0.36,"Costa Rica":0.59,"Croacia":0.45,"Dinamarca":0.88,"Egipto":0.25,"España":0.18,"Francia":0.01,"Inglaterra":0.19,"Iran":0.73,"Islandia":0.65,"Japon":0.01,"Marruecos":0.82,"Mexico":0.70,"Nigeria":0.77,"Panama":0.05,"Peru":0.00,"Polonia":0.35,"Portugal":0.62,"Rusia":0.17,"Senegal":0.69,"Serbia":0.62,"Suecia":0.88,"Suiza":0.52,"Tunez":0.49,"Uruguay":0.46}
    return dicc[pais2]


def puntaje_paises(key,puntaje):
    dicc2 = {}
    dicc2.update({key,puntaje})
    return print(dicc2)




puntajes_pais2 =[]
pais1 = input()
pais2 = input()
pintaje = 0
if pais1 == "Alemania" and pais2 == "Alemania" or "Arabia" or "Saudita"or "Argentina" or "Australia"or "Belgica"or "Brasil"or "Colombia"or "Corea del Sur"or "Costa Rica"or "Croacia"or "Dinamarca"or "Egipto"or "España"or "Francia"or "Inglaterra"or "Iran"or "Islandia"or "Japon"or "Marruecos"or "Mexico"or "Nigeria"or "Panama"or "Peru"or "Polonia"or "Portugal"or "Rusia"or "Senegal"or "Serbia"or "Suecia"or "Suiza"or "Tunez"or "Uruguay":
    puntaje = prob_alemania(pais2)
    if 1 < puntaje > 0.5 :
        puntajes_pais2.append(3)
        print(pais2," GANA",pais1,"PIERDE")
    elif puntaje == 1:
        puntajes_pais2.append(1)
        print("EMPATE")
    else:
        print(pais2,"PIERDE",pais1,"GANA")
print(puntajes_pais2)
