import pandas as pd
print("Menu")
print("1-Leer archivo")
print("2-Mostrar cantidad de registros")
print("3-Mostrar datos estadisticos")
print("4-Consultas mayor o menor que")
print("5-Salir")

df=pd.read_csv("ENARM.csv")
while True:
    op=input("Seleccione una opcion: ")
    if op=="1":
        print("Leer archivo")
        df =pd.read_csv("ENARM.csv")
    if op=="2":
        print("Mostrar cantidad de registros")
        pritn=df.head(5)
    if op=="3":
        print("Mostrar datos estadisticos")
        print(df["promedio"].min())
        print(df["Seleccionados"].max())
        print(df["Sustentantes"].median())
    if op=="4":
        print("Consultas mayor o menor que")
        print(df[df["promedio"] > 70])
        print(df[df["promedio"] < 65])
    if op=="5":
        print(" SALIR")
        break
else:
    print("ERROR: Intente de nuevo")
