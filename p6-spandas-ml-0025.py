import pandas as pd
import numpy as np
# Emily Barraza NC 0025
serie_amigos=["Pepe","Mimi","Lola","Flor","Titi","Edith","Vero"]
print("---serie listado de amigos NC 0025---")
amigos=pd.Series(serie_amigos)
print(amigos)

serie_billetes=[20,50,100,200,500,1000]
print("---serie listado de billetes NC 0025---")
amigos=pd.Series(serie_billetes)
print(amigos)

serie_billetes=[20,50,100,200,500,1000]
serie_bletras=["vente","cincuenta","cien","doscientos","quinientos","mil"]
print("---serie listado nombre y valor de billetes MX NC 0025---")
tablabilletes=pd.Series(serie_bletras,serie_billetes)
print(tablabilletes)

# Diccionario DataFrame
# diccionario monedas y nombre
print("datos de diccionario a DataFrame en pandas ")
dicc_monedas={
    "serie_billetes":[20,50,100,200,500,1000],
    "serie_bletras":["vente","cincuenta","cien","doscientos","quinientos","mil"]
}
tablaEmily=pd.DataFrame(dicc_monedas,index=["A","B","C","D","E","F"])
print(tablaEmily)

print("---casa de cambio de Emily Barraza NC 0025---")