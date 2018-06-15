import random
bombos = [["Rusia", "Alemania", "Brasil", "Portugal", "Argentina", "Belgica", "Polonia", "Francia"],
          ["España", "Perú", "Suiza", "Inglaterra", "Colombia", "Mexico", "Uruguay", "Croacia"],
          ["Dinamarca", "Islandia", "Costa Rica", "Suecia", "Tunez", "Egipto",  "Senegal", "Irán"],
          ["Serbia", "Niegeria", "Australia", "Japón", "Marruecos", "Panamá", "Corea del Sur", "Arabia Saudita"]]

def sorteo (bombos):
    lista_grupos = []
    for i in range (8):
        grupo = []
        for j in (bombos):
            grupo.append(j[random.randint(0,7-i)])
            j.remove(grupo[-1])
        lista_grupos.append(grupo)
    return lista_grupos

lista = sorteo(bombos)

print(lista)

#                     Alemania Arabia Saudita Argentina Australia Belgica Brasil Colombia Corea del Sur Costa Rica Croacia Dinamarca Egipto España Francia Inglaterra Iran Islandia Japon Marruecos Mexico Nigeria Panama Peru Polonia Portugal Rusia Senegal Serbia Suecia Suiza Tunez Uruguay
tabla_probabilidades = [1.00,0.27,0.60,0.10,0.50,0.04,0.34,0.12,0.26,0.24,0.22,0.23,0.99,0.44,0.02,0.43,0.60,0.19,0.54,0.25,0.35,0.35,0.00,0.35,0.62,0.17,0.69,0.62,0.88,0.52,0.49,0.46],\
                       [0.63,1.00,0.66,0.29,0.93,0.19,0.91,0.36,0.59,0.45,0.88,0.25,0.18,0.01,0.19,0.73,0.65,0.01,0.82,0.70,0.77,0.54,0.05,0.68,0.87,0.77,0.16,0.47,0.34,0.73,0.53,0.60],\
                       [0.40,0.34,1.00,0.99,0.01,0.35,0.54,0.40,0.51,0.39,0.13,0.02,0.02,0.05,0.62,0.50,0.53,0.94,0.07,0.02,0.62,0.85,0.33,0.16,0.21,0.66,0.81,0.93,0.20,0.21,0.67,0.67],\
                       [0.90,0.71,0.01,1.00,0.16,0.44,0.02,0.84,0.41,0.86,0.37,0.85,0.13,0.97,0.42,0.87,0.58,0.78,0.86,0.50,0.01,0.86,0.39,0.66,0.61,0.60,0.22,0.10,0.35,0.46,0.10,0.09],\
                       [0.50,0.07,0.99,1.00,0.84,0.34,1.00,0.39,0.48,0.23,0.38,0.17,0.93,0.71,0.40,0.56,0.05,0.17,0.27,0.77,0.63,0.30,0.48,0.79,0.94,0.91,0.63,0.31,0.93,0.75,0.17,0.47],\
                       [0.96,0.81,0.65,0.56,0.66,1.00,0.44,0.56,0.33,0.64,0.39,0.63,0.60,0.70,0.83,0.99,0.96,0.73,0.21,0.13,0.32,0.56,0.98,0.01,0.42,0.65,0.59,0.52,0.65,0.62,0.41,0.35],\
                       [0.66,0.09,0.46,0.98,0.00,0.56,1.00,0.30,0.85,0.80,0.01,0.22,0.68,0.61,0.52,0.42,0.37,0.47,0.25,0.34,0.72,0.91,0.07,0.63,0.24,0.63,0.59,0.28,0.19,0.07,0.27,0.05],\
                       [0.88,0.64,0.60,0.16,0.61,0.44,0.70,1.00,0.66,0.68,0.77,0.38,0.53,0.55,0.24,0.86,0.47,0.68,0.74,0.04,0.55,0.96,0.64,0.49,0.07,0.86,0.41,0.43,0.30,0.52,0.85,0.76],\
                       [0.74,0.41,0.49,0.59,0.52,0.67,0.15,0.34,1.00,0.81,0.71,0.32,0.66,0.19,0.71,0.97,0.69,0.64,0.50,0.47,0.84,0.95,0.41,0.96,0.56,0.44,0.30,0.65,0.53,0.77,0.83,0.25],\
                       [0.76,0.55,0.61,0.14,0.77,0.36,0.20,0.32,0.19,1.00,0.90,0.14,0.17,0.52,0.27,0.22,0.84,0.65,0.72,0.16,0.50,0.40,0.73,0.88,0.77,0.21,0.39,0.89,0.17,0.34,0.43,0.73],\
                       [0.78,0.12,0.87,0.63,0.62,0.61,0.99,0.23,0.29,0.10,1.00,0.34,0.12,0.03,0.40,0.13,0.34,0.71,1.00,0.41,0.80,0.64,0.50,0.58,0.75,0.52,0.84,0.83,0.25,0.47,0.84,0.89],\
                       [0.77,0.75,0.98,0.15,0.83,0.37,0.78,0.62,0.68,0.86,0.66,1.00,0.47,0.52,0.15,0.29,0.13,0.76,0.64,0.11,0.30,0.45,0.16,0.07,0.22,0.05,0.46,0.61,0.35,0.44,0.32,0.96],\
                       [0.01,0.82,0.98,0.87,0.07,0.40,0.32,0.47,0.34,0.83,0.88,0.53,1.00,0.72,0.13,0.24,0.11,0.74,0.20,0.47,0.62,0.79,0.21,0.27,0.20,0.04,0.39,0.73,0.10,0.94,0.59,0.04],\
                       [0.56,0.99,0.95,0.03,0.29,0.30,0.39,0.45,0.81,0.48,0.97,0.48,0.28,1.00,0.24,0.12,0.58,0.06,0.27,0.64,0.88,0.67,0.24,0.71,0.76,0.63,0.47,0.27,0.67,0.04,0.13,0.69],\
                       [0.98,0.81,0.38,0.58,0.60,0.17,0.48,0.76,0.29,0.73,0.60,0.85,0.87,0.76,1.00,0.83,0.00,0.66,0.65,0.24,0.62,0.80,0.04,0.57,0.97,0.53,0.79,0.77,0.74,0.07,0.66,0.70],\
                       [0.57,0.27,0.50,0.13,0.44,0.01,0.58,0.14,0.03,0.78,0.87,0.71,0.76,0.88,0.17,1.00,0.72,0.04,0.15,0.91,0.70,0.90,0.89,0.07,0.95,0.68,0.37,0.70,0.72,0.51,0.85,0.41],\
                       [0.40,0.35,0.47,0.42,0.95,0.04,0.63,0.53,0.31,0.16,0.66,0.87,0.89,0.42,1.00,0.28,1.00,0.83,0.74,0.60,0.54,0.19,0.84,0.76,0.28,0.21,0.16,0.55,0.33,0.93,0.36,0.98],\
                       [0.81,0.99,0.06,0.22,0.83,0.27,0.53,0.32,0.36,0.35,0.29,0.24,0.26,0.94,0.34,0.96,0.17,1.00,0.41,0.23,0.45,0.89,0.84,0.96,0.84,0.90,0.84,0.04,0.75,0.26,0.40,0.31],\
                       [0.46,0.18,0.93,0.14,0.73,0.79,0.75,0.26,0.50,0.28,0.00,0.36,0.80,0.73,0.35,0.85,0.26,0.59,1.00,0.19,0.08,0.53,0.67,0.46,0.04,0.11,0.32,0.80,0.82,0.06,0.96,0.43],\
                       [0.75,0.30,0.98,0.50,0.23,0.87,0.66,0.96,0.53,0.84,0.59,0.89,0.53,0.36,0.76,0.09,0.40,0.77,0.81,1.00,0.13,0.82,0.66,0.87,0.30,0.59,0.50,0.03,0.77,1.00,0.83,0.46],\
                       [0.65,0.23,0.38,0.99,0.37,0.68,0.28,0.45,0.16,0.50,0.20,0.70,0.38,0.12,0.38,0.30,0.46,0.55,0.92,0.87,1.00,0.57,0.67,0.34,0.24,0.92,0.48,0.35,0.55,0.72,0.20,0.50],\
                       [0.65,0.46,0.15,0.14,0.70,0.44,0.09,0.04,0.05,0.60,0.36,0.55,0.21,0.33,0.20,0.10,0.81,0.11,0.47,0.18,0.43,1.00,0.14,0.08,0.71,0.94,0.64,0.49,0.11,0.46,0.42,0.08],\
                       [1.00,0.95,0.67,0.61,0.52,0.02,0.93,0.36,0.59,0.27,0.50,0.84,0.79,0.76,0.96,0.11,0.16,0.16,0.33,0.34,0.33,0.86,1.00,0.10,0.87,0.76,0.37,0.51,0.68,0.33,0.20,0.08],\
                       [0.65,0.32,0.84,0.34,0.21,0.99,0.37,0.51,0.04,0.12,0.42,0.93,0.73,0.29,0.43,0.93,0.24,0.04,0.54,0.13,0.66,0.92,0.90,1.00,0.13,0.96,0.78,0.10,0.74,0.35,0.24,0.35],\
                       [0.38,0.13,0.79,0.39,0.06,0.58,0.76,0.93,0.44,0.23,0.25,0.78,0.80,0.54,0.03,0.05,0.72,0.16,0.96,0.70,0.76,0.29,0.13,0.87,1.00,0.72,0.26,0.83,0.85,0.81,0.33,0.10],\
                       [0.83,0.23,0.34,0.40,0.09,0.35,0.37,0.14,0.56,0.79,0.48,0.95,0.96,0.37,0.47,0.32,0.79,0.10,0.89,0.41,0.08,0.06,0.24,0.04,0.28,1.00,0.23,0.79,0.71,0.00,0.63,0.51],\
                       [0.31,0.84,0.19,0.78,0.37,0.41,0.41,0.59,0.70,0.61,0.16,0.54,0.61,0.53,0.21,0.63,0.84,0.16,0.68,0.50,0.52,0.36,0.63,0.22,0.74,0.77,1.00,0.45,0.60,0.10,0.29,0.77],\
                       [0.38,0.53,0.07,0.90,0.69,0.48,0.72,0.57,0.35,0.11,0.17,0.39,0.27,0.73,0.23,0.30,0.45,0.96,0.20,0.97,0.65,0.51,0.49,0.90,0.17,0.21,0.55,1.00,0.25,0.20,0.35,0.00],\
                       [0.12,0.66,0.80,0.65,0.07,0.35,0.81,0.70,0.47,0.83,0.75,0.65,0.90,0.33,0.26,0.28,0.67,0.25,0.18,0.23,0.45,0.89,0.32,0.26,0.15,0.29,0.40,0.75,1.00,0.39,0.65,0.18],\
                       [0.48,0.27,0.79,0.54,0.25,0.38,0.93,0.48,0.23,0.66,0.53,0.56,0.06,0.96,0.93,0.49,0.07,0.74,0.94,0.00,0.28,0.54,0.67,0.65,0.19,1.00,0.90,0.80,0.61,1.00,0.98,0.11],\
                       [0.51,0.47,0.33,0.90,0.83,0.59,0.73,0.15,0.17,0.57,0.16,0.68,0.41,0.87,0.34,0.15,0.64,0.60,0.04,0.17,0.80,0.58,0.80,0.76,0.67,0.37,0.71,0.65,0.35,0.02,1.00,0.43],\
                       [0.54,0.40,0.33,0.91,0.53,0.65,0.95,0.24,0.75,0.27,0.11,0.04,0.96,0.31,0.30,0.59,0.02,0.69,0.57,0.54,0.50,0.92,0.92,0.65,0.90,0.49,0.23,1.00,0.82,0.89,0.57,1.00]
print(tabla_probabilidades)


print(tabla_probabilidades [0][2])



def prob_alemania (pais2):
    dicc = {}
    dicc = {"Alemania":1.00,"Arabia_Saudita":0.27,"Argentina":0.60,"Australia":0.10,"Belgica":0.50,"Brasil":0.04,"Colombia":0.34,"Corea del Sur":0.12,"Costa Rica":0.26,"Croacia":0.24,"Dinamarca":0.22,"Egipto":0.23,"España":0.99,"Francia":0.44,"Inglaterra":0.02,"Iran":0.43,"Islandia":0.60,"Japon":0.19,"Marruecos":0.54,"Mexico":0.25,"Nigeria":0.35,"Panama":0.35,"Peru":0.00,"Polonia":0.35,"Portugal":0.62,"Rusia":0.17,"Senegal":0.69,"Serbia":0.62,"Suecia":0.88,"Suiza":0.52,"Tunez":0.49,"Uruguay":0.46}
    return dicc[pais2]

def prob_Arabia_Saudita (pais2):
    dicc = {}
    dicc = {"Alemania":0.63,"Arabia_Saudita":1.00,"Argentina":0.66,"Australia":0.29,"Belgica":0.93,"Brasil":0.19,"Colombia":0.91,"Corea del Sur":0.36,"Costa Rica":0.59,"Croacia":0.45,"Dinamarca":0.88,"Egipto":0.25,"España":0.18,"Francia":0.01,"Inglaterra":0.19,"Iran":0.73,"Islandia":0.65,"Japon":0.01,"Marruecos":0.82,"Mexico":0.70,"Nigeria":0.77,"Panama":0.05,"Peru":0.05,"Polonia":0.35,"Portugal":0.87,"Rusia":0.77,"Senegal":0.16,"Serbia":0.47,"Suecia":0.34,"Suiza":0.73,"Tunez":0.53,"Uruguay":0.60}
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







