import pandas as pd
lenguajes=pd.read_csv('languages_dataset.csv')

def creacion():
    print(lenguajes.head() )

def filtrar():
    seleccion=int(input("""
    Que desea filtrar:
          1.-Lenguaje
          2.-Familia
          3.-Region
          4.-Speaker
          5.-Sistema de escritura
          6.-Codigo Iso
    """ ))
    if seleccion==1:
            a=input()
            print(lenguajes[lenguajes['Language']==a])
    elif seleccion==2:
            a=input()
            print(lenguajes[lenguajes['Family']==a])       
    elif seleccion==3:
            a=input()
            print(lenguajes[lenguajes['Region']==a])
    elif seleccion==4:
            a=input()
            print(lenguajes[lenguajes['Speakers']==a])
    elif seleccion==5:
            a=input()
            print(lenguajes[lenguajes['Writing System']==a])
    elif seleccion==6:
            a=input()
            print(lenguajes[lenguajes['ISO Code']==a])        
    else:
            print("ERROR DE DATO")

def agregar():
       global lenguajes
       leng=input("Lenguaje: ")
       fam=input("Familia: ")
       reg=input("Region: ")
       Speaker=input("Speaker: ")
       escritura=input("S.EScritura: ")
       codigo=input("Codigo: ")
       nuevo=pd.DataFrame({'Language':[leng],'Family':[fam],'Region':[reg],'Speakers':[Speaker],'Writing System':[escritura],'ISO Code':[codigo]})
       lenguajes=pd.concat([lenguajes, nuevo], ignore_index=True)
       print(lenguajes)

def modificar():
        global lenguajes
        nro=int(input("que valor desea modificar: "))
        leng=input("Lenguaje: ")
        fam=input("Familia: ")
        reg=input("Region: ")
        Speaker=int(input("Speaker: "))
        escritura=input("S.EScritura: ")
        codigo=input("Codigo: ")
        lenguajes.loc[nro, 'Language'] = leng
        lenguajes.loc[nro, 'Family'] = fam
        lenguajes.loc[nro, 'Region'] = reg
        lenguajes.loc[nro, 'Speakers'] = Speaker
        lenguajes.loc[nro, 'Writing System'] = escritura
        lenguajes.loc[nro, 'ISO Code'] = codigo
        print(lenguajes)