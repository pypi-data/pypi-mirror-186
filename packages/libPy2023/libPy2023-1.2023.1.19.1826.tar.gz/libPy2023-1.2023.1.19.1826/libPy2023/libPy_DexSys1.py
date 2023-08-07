## -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import pandas as pd
from pandas import ExcelWriter
import os
from os import  listdir
import numpy as np
import sys
from pandas.core.frame import DataFrame
# pip install pywin32 para usar win32com
from win32com import client
import keyboard

global UserName ,PassWord,HOST_DB,USER_DB,PASS_DB,PORT_DB,_TIPOEJECUCION
UserName="colbun\\lcorales"


USER_DB = 'root'
HOST_DB="192.168.0.18"  #"dexsys.ddns.net" #if os.environ['COMPUTERNAME']=='HPLUDWIG' else "10.10.241.167"
PASS_DB = 'isijoa'
PORT_DB=3306

IsOK  = bcolors.BBLUE+"\u2611"+bcolors.ENDC
IsBad = bcolors.BRED+"\u2612"+bcolors.ENDC

dias = {
    0: "Domingo",
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado"}

Ahora = datetime.now()

DiaSemana=dias.get(int(Ahora.strftime("%w")))
_PRUEBA = True if ~(DiaSemana =="Martes" or DiaSemana=="Lunes" )==-1 else False
_TIPOEJECUCION=bcolors.BOLD+bcolors.OKGREEN+("TEST" if _PRUEBA else "PRODUCTIVO")+bcolors.ENDC

# def ImportarHojasXLSX(RutaArchivo,Archivo,Hoja,Encabezados=0,AgregaOrigen=False):
#     """
#     ImportarHojasXLSX: Permite importar Hojas de Calculo en Pandas.\n
#         RutaArchivo : Ruta de Archivo Excel a Importar.
#         Archivo     : Excel del que se importara la hoja.
#         Hoja        : Hoja de la que se extraeran los datos.
#         Encabezados : Fila donde están los encabezados, Cero sin encabezados.
#         AgregaOrigen: Agrega dos columnas con información desde donde se obtuvieron los datos.
#     \n
#                 Retorna un DataFrame.
#     """
#     print(f"Lectura de Archivo Excel {bcolors.BBLUE}{Archivo}{bcolors.ENDC}\nHoja {bcolors.BBLUE}{Hoja}{bcolors.ENDC}",end="\t- ")
#     WBS = pd.read_excel(RutaArchivo+"/"+Archivo, sheet_name=Hoja,header=Encabezados)
#     if AgregaOrigen:
#         WBS['Archivo']=Archivo
#         WBS['Hoja']=Hoja
#         print(f"N° Filas Filtradas :{len(WBS)}\tDelta: {Ahora.Delta()}")
#     return WBS

def MessageBox(Texto="Falta el Mensaje",Opciones="SN"):
    """
    Requisito previo : pip install keyboard
    MessageBox -> Muestra un mensaje en la pantalla y espera a que se presionen algunas de las teclas indicadas.\n
        Texto    : Mensaje a desplegar\n
        Opciones : las teclas que se espera que presionen
    """
    BOTONRED="\033[1;31;47m"
    ENDC="\x1b[00m"
    GREEN="\x1b[32m"
    xTeclas=list(Opciones)
    xkey=""
    for xOpcion in xTeclas:

        xkey+=f"{BOTONRED} {xOpcion} {ENDC} / "
    xkey=xkey[:-2]
    print(f"\n{GREEN}{Texto}{ENDC}  {xkey}\n")
    #Espera hasta que se presione unas de las teclas indicado en Opciones, da lo mismo si es mayúscula o minúscula
    while True:
        Tecla=keyboard.read_key().upper()
        if Tecla in Opciones:
            break
    return Tecla

def df2colstr(df):
    """
    df2colstr : Permite obtener un string con todos los nombres de columna de un DataFrame
    """
    Lista=df.columns.values
    Cadena=""
    for Valor in Lista:
        if type(Valor) is not str:
            Valor=str(Valor)
        Cadena=Cadena+"`"+Valor+"`"+" ,"
    return Cadena[:-1] #devuelve la cadena sin la ultima coma

def PrintError(e,connextion=""):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fName = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(f"\n\nError en Linea : {bcolors.RED}{exc_tb.tb_lineno}{bcolors.ENDC} en {bcolors.RED}{fName}{bcolors.ENDC}")
    print(exc_type)
    print(f"Error Inesperado: {bcolors.RED}{str(sys.exc_info()[0])}")
    print(str(e))
    print(str(EnvironmentError)+bcolors.ENDC)
    #print(bcolors.FAIL+"No se puede conectar a la base de datos"+bcolors.ENDC)
    if not connextion=="":
        connextion.close()
    #sys.exit(0)

def toVars(xNumero):
    """
    toVars  : Permite crear cadena de sustitución para consultas SQL con %s\n
    xNumero : Cantidad de %s que se crearan.
    """
    xPassVariables="%s,"*xNumero
    xPassVariables=xPassVariables[:-1]
    return xPassVariables

def GenerateQuery(xdf,TABLENAME,Tipo="REPLACE"):
    """
    GenerateQuery() -> Permite Generar la Clausula Query\n
    xdf             -> DataFrame que se usara\n
    Tipo            -> Puede ser Insert o Replace
    """
    Mis_Campos=df2colstr(xdf) # Obtiene un String con las columnas de la Tabla
    xPassVariables=toVars(len(xdf.columns)) # crea la cadena %s de remplazo según la cantidad de campos
    Consulta=f"{Tipo.upper()} INTO {TABLENAME}({Mis_Campos}) VALUES ({xPassVariables});"
    return Consulta

class Cronometro:
    def __init__(self):
        self.Iniciar=datetime.now()
        #self.Ahora=self.Iniciar

    def Delta(self):
        self.Ahora=datetime.now()
        return self.Ahora-self.Iniciar

    def Reset(self):
        self.Iniciar=datetime.now()

    def Termino(self):
        return f"Termino :{datetime.now()}"

    def now(self):
        return datetime.now()

    def Inicio(self):
        return f"{self.Iniciar}"

    def Año(self):
        return self.Iniciar.year

    def Mes(self):
        return self.Iniciar.month

    def Dia(self):
        return self.Iniciar.day

    def __str__(self):
        return f"Delta Time {self.Delta}"

def ImportarHojasXLSX(Ruta,Archivo,Hoja,Encabezados=0,AgregaOrigen=True,Mensajes=False):
    """
    ImportarHojasXLSX: Permite importar Hojas de Calculo en Pandas.\n
        Ruta        : Ruta de Archivo Excel a Importar.
        Archivo     : Excel del que se importara la hoja.
        Hoja        : Hoja de la que se extraeran los datos.
        Encabezados : Fila donde están los encabezados, Cero sin encabezados.
        AgregaOrigen: Agrega dos columnas con información desde donde se obtuvieron los datos.
    \n
                Retorna un DataFrame.
    """
    Ahora=Cronometro()
    if Mensajes:
        print(f"Lectura de Archivo Excel {bcolors.BBLUE}{Archivo}{bcolors.ENDC}\nHoja {bcolors.BBLUE}{Hoja}{bcolors.ENDC}",end="\t- ")
    WBS = pd.read_excel(Ruta+"/"+Archivo, sheet_name=Hoja,header=Encabezados)
    if AgregaOrigen:
        WBS['Archivo']=Archivo
        WBS['Hoja']=Hoja
        if Mensajes:
            print(f"N° Filas Filtradas :{len(WBS)}\tDelta: {Ahora.Delta()}")
    return WBS

def pos(x,y):
    return "\033[" + str(x) + ";" + str(y) + "H"

def xprint(x:int,y:int,text:str):
    print(pos(x,y)+text)

def Registro2Lista(df:DataFrame,xDataTypeColumns=None):
    """
    Registro2Lista() : Transforma un dataframe en una lista de tuplas\n
                       Adicionalmente eliminan los NaN y los cambia a None
    parameters       : df -> Dataframe a transformar
    """
    #column_dtypes={"A": "int32"}
    df = df.replace({np.nan: None})
    if not xDataTypeColumns==None:
        #xdf=df.to_records(index=False,column_dtypes=xDataTypeColumns).tolist()
        #xdf_=df.to_records(index=False,column_dtypes=xDataTypeColumns)
        index_dtypes = f"<S{df.index.str.len().max()}"
        xdf=list(df.itertuples(index=False, name=None))
        ##xdf=df.to_records(index=False,column_dtypes=index_dtypes).tolist()
    else:
        xdf= df.to_records(index=False).tolist()
    return xdf

def QueMes(xMes="Debe proporcionar una cadena que contenga el mes en 3 letras",Corto=True):
    MesEspañol = ["ENE", "FEB", "MAR", "ABR", "MAY",
                  "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]
    MesEspañolLargo=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    MiMes = MesEspañol.index(xMes[:3].upper())+1 if Corto else MesEspañolLargo.index(xMes[:3].upper())
    return (MiMes)

def Import_Histórico(xPath1="Debe especificar una Ruta", xDataFrameImport="Debe Indicar DataFrame",NombreHoja="Hoja1", \
        xTitulo="", Avisos=False,xdtype={}):
    ListaArchivo = listdir(xPath1)  # Revisar esto despues
    print(f"\t\tSe procesaran :{bcolors.BLUE}{len(ListaArchivo)}{bcolors.ENDC} (Archivos xlsx)")
    ii = 0
    xiTotal = 0
    for fileImport in ListaArchivo:
        ii = ii+1
        print(f"\t\t\t{ii:03}", end=" ")
        DataFromExcel = pd.read_excel(xPath1+fileImport, sheet_name=NombreHoja,  header=0, engine='xlrd',dtype=xdtype)
        xDataFrameImport = xDataFrameImport.append(DataFromExcel, ignore_index=True)
        xTotal = len(DataFromExcel)
        xiTotal = xiTotal + xTotal
        print(f"\t{fileImport:<30}\t({xTotal:8,.0f})", end=" ")
        Listo()

    print(f"\n\t\t\tTotal Registros Importados: {str(xiTotal)} de {len(xDataFrameImport)}")
    return xDataFrameImport

def wait_key():
    """ Espera que se presione una Tecla en la Consola y retorna la tecla presionada """
    result = None
    Banner("Pulse cualquier Tecla para continuar.....",Pad="C")
    if os.name == 'nt':
        import msvcrt
        result = msvcrt.getch()
    return result

def Listo(QueTipo=True):
    print(bcolors.BLUE+"\t\u2611" +
          bcolors.ENDC if QueTipo else bcolors.FAIL+"\u2612"+bcolors.ENDC)

def isNaN(num):
    return num != num

def isstr(xValor):
    return type(xValor) == str

def parse_datejson2(Fecha):
    if Fecha!=None:
        EPOCH = datetime.utcfromtimestamp(0)
        if len(Fecha) < 18:  ## Verifica que la cadena tenga la longitud minima, si no complet con los Ceros
            Fecha = Fecha+"00000"
        milliseconds = int(Fecha[:-5])  ## Lleva la cadena a su equivalente en Milisegundos
        hours = int(Fecha[-5:]) / 100   ## Transforma los
        if hours == 0:
            hours = -4.0
        adjustedseconds = milliseconds / 1000 + hours * 3600
        xReturn = EPOCH + timedelta(seconds=adjustedseconds)
    else:
        xReturn=Fecha
    return xReturn

def parse_date(DateString="Debe proporcionar una fecha en formato JSON del Tipo /Date(1503889200000)/"):
    """
    parse_date             : Convierte las Fechas JSON a fecha regulares\n
    Parameters DateString  : Cadena de Texto con fecha en formato JSON del tipo /Date(1503889200000)/
    """
    if DateString == None:
        xReturn = None
    else:
        EPOCH = datetime.utcfromtimestamp(0)
        if not isNaN(DateString):
            timepart = DateString.split('(')[1].split(')')[0]  ## Extrae solo la parte que esta entre los patentices ()
        else:
            return 0

        if len(timepart) < 18:  ## Verifica que la cadena tenga la longitud minima, si no complet con los Ceros
            timepart = timepart+"00000"
        milliseconds = int(timepart[:-5])  ## Lleva la cadena a su equivalente en Milisegundos
        hours = int(timepart[-5:]) / 100   ## Transforma los
        if hours == 0:
            hours = -4.0
        adjustedseconds = milliseconds / 1000 + hours * 3600
        xReturn = EPOCH + timedelta(seconds=adjustedseconds)
    return xReturn

#from datetime import datetime
def validate(date_text):
    try:
        xR=datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


def Json2MySQL(timepart):
    if not isNaN(timepart):
        EPOCH = datetime.utcfromtimestamp(0)
        try:
            return timepart.strftime('%Y-%m-%d %H:%M:%S')
            #datetime.datetime.strptime(timepart, '%Y-%m-%d')
            #return timepart
        except :
            if not type(timepart) == str:
                timepart=str(timepart)
        timepart=timepart+"00" if timepart[-1]==":" else timepart # si tiene los : al final se pitio los segundos, se corrige
        if not (timepart.find("-") or timepart.find(":")):   # si contiene los : se asume que es texto con fecha y hora
            if len(timepart) < 18:  ## Verifica que la cadena tenga la longitud minima, si no complet con los Ceros
                    timepart = timepart+"00000"
            if len(timepart)>18:
                timepart=timepart[0:17]
            milliseconds = int(timepart[:-5])  ## Lleva la cadena a su equivalente en Milisegundos
            hours = int(timepart[-5:]) / 100   ## Transforma los
            if hours == 0:
                hours = -4.0
            adjustedseconds = milliseconds / 1000 + hours * 3600
            xReturn = EPOCH + timedelta(seconds=adjustedseconds)
            return xReturn
        else:
            return timepart
    else:
        return None

def TerminarPrograma(Menssage="#### Termino Normal Por Usuario ####"):
    Menssage = "#### Termino Normal Por Usuario ####" if len(
        Menssage) == 0 else Menssage
    print(Menssage)
    sys.exit(0)

def xTipoCtaCtbl(x):
    xTipo = "N/D"
    if x[0] == "5":
        xTipo = "Inversión"
    if x[0] == "6":
        xTipo = "Costo"
    if x[0] == "7":
        xTipo = "Gasto"
    return xTipo

def QueGenero(xCadena="Debe ingresar una Cadena Valida",html=True):
    """
    QueGenero : Esta función devuelve el tratamiento 'Sr o Srta' dependiendo del primer nombre de la cadena proporcionada.
    xCadena   : String que representa el nombre completo, del cual se separa por los espacios, y devuelve el primer sub string,
                el cual se asocia a su respectivo tratamiento 'Sr o Srta' dependiendo del caso
    Retorna   : String
    """
    Propio=xCadena.split()
    Nombre=Propio[0].title()
    htmlin="<strong>" if html else ""
    htmlout="</strong>" if html else ""
    if Nombre[-1:] in ["a","e"] : ### Terminaciones en 'a' y 'e' Normalmente de Mujeres
        return ("Estimada "+htmlin+Nombre+htmlout)
    else:
        return ("Estimado "+htmlin+Nombre+htmlout)

def ExisteTablaMariaDB(xcursor="Debe indicar un Cursor", Tabla="Debe indicar la tabla a verificar"):
    xcursor.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(Tabla.replace('\'', '\'\'')))
    if xcursor.fetchone()[0] == 1:
       return True
    return False

def ExisteTablaSQLite3(xcursor="Debe indicar un Cursor", Tabla="Debe indicar la tabla a verificar"):
    """
    ExisteTabla: Permite averiguar si en una Base de Datos de Access (talvez otras) existe una tabla en particular
        Parametros:
            xcursor -> Cursor de conexión a la base de datos
            Nombre  -> Nombre de Tabla que se quiere Verificar si existe
    La función usa PypyODBC opyODBC, para saber si la tabla existe ya que en TurboODBC no hay soporte aun.
    """
    xcursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='"+Tabla+"'")
    if xcursor.fetchone()[0]==1:
        return True
    else:
        return False

def ExisteTabla(xcursor="Debe indicar un Curosor", Tabla="Debe indicar la tabla a verificar"):
    """
    ExisteTabla: Permite averiguar si en una Base de Datos de Access (talvez otras) existe una tabla en particular
        Parametros:
            xcursor -> Cursor de conexión a la base de datos
            Nombre  -> Nombre de Tabla que se quiere Verificar si existe
    La función usa PypyODBC opyODBC, para saber si la tabla existe ya que en TurboODBC no hay soporte aun.
    """
    #Existe = xcursor.tables(table=Tabla, tableType='TABLE').fetchone()

    for xx in xcursor.tables().fetchall():
        xTabla=xx[2].upper()

        if xTabla==Tabla.upper():
            return True
    return False

# def ExisteTabla2(StrConexion="Debe Indicar Cadena de Conexión", Tabla="Debe indicar la tabla a verificar"):
#     """
#     ExisteTabla: Permite averiguar si en una Base de Datos de Access (talvez otras) existe una tabla en particular
#         Parametros:
#             xcursor -> Cursor de conexión a la base de datos
#             Nombre  -> Nombre de Tabla que se quiere Verificar si existe
#     La función usa PypyODBC opyODBC, para saber si la tabla existe ya que en TurboODBC no hay soporte aun.
#     """

#     Conexion_db_Access = ConnODBC.connect(StrConexion, autocommit=True)
#     xcursor = Conexion_db_Access.cursor()
#     Existe = xcursor.tables(table=Tabla, tableType='TABLE').fetchone()
#     Conexion_db_Access.close()
#     return Existe

def ImportSAP_SF(xArchivo="", xsep="|", xHeadLine=4, AnchoFijo=False,PrintError=False):
    """
    ImportSAP_SF : Permite realizar la importación de reportes sin formato creados en SAP.
                   El Procedimiento devuelve como resultado el DataFrame con los datos importados.
                   Nota: Evaluar si este procedimiento es eficiente y si no colapsa con muchos datos.
    Parametros:
        xArchivo    : Nombre del Archivo TXT de formato tabular o salida sin formato de SAP
        xsep        : El separador de campos a utiliza, por defecto es el carácter barra o Pipe.
        xHeadLine   : es el indicador de donde esta la líneas de encabezado, por defecto es 4
        AnchoFijo   : Permite indicarle si debe dividir las columnas solo por los separadores o determinar
                      según el encabezado la lectura posterior de datos
        PrintError  : Permite mostrar errores de caracteres o formato, que se repara automáticamente.

    """
    xProceso = (os.path.basename(xArchivo)).upper().split('.')[0]
    print(f"\tProcesamiento \x1B[31m{xProceso}\x1B[0m----> Lectura y Transformación")
    with open(xArchivo, 'r') as f:
        xFila = 0
        xMisDatos = []
        nErrores=0

        for xlineas in f: #tqdm(f):
            xFila = xFila+1
            xdex = -1

            ### xLineas tiene la linea completa sin separar
            ## Corrige errores en las descripciones con caracateres raros o exepciones..
            if u"\x1a" in xlineas:
                if PrintError:
                    print("\t\t\t"+bcolors.WARNING +r"opps carácter raro \x1a en Linea:",xFila,bcolors.ENDC+bcolors.GREEN+"- Fixing..."+bcolors.ENDC)
                xlineas = xlineas.replace(u"\x1a", " ")

            if '  "|' in xlineas:
               if PrintError:
                    print("\t\t\t"+bcolors.WARNING + r'opps carácter raro <  " |> en Linea: ',xFila, bcolors.ENDC+" - Fixing...")
               xlineas = xlineas.replace('  "|', "|")

            if ("Salida dinámica de lista" in xlineas or xlineas.replace("-","")=="\n"):
                if PrintError:
                    print(f"Lineas de separación? {xFila}\n{xlineas}")
                continue


            lineas = xlineas.split(xsep)  # obtiene las columnas
            #lineas = [linea.split(xsep) for linea in f] ### esto recupera todo y lleva a una matriz
            if xFila >= xHeadLine:
                if xHeadLine == xFila:  # Esta es la Linea de Encabezados
                    ### Recorre el encabezado y elimina columnas no deseadas
                    NombreColumnas = []
                    if AnchoFijo:
                        ## Crear Matriz encabezados
                        nSep = xlineas.count(xsep)  # Cuenta los separadores
                        xColumna = []

                        for i in range(nSep):
                            xdex = xlineas.find(xsep, xdex+1)
                            xColumna.append(xdex)
                            #NombreColumnas.append(lineas)

                        #### Elimina las columnas innecesarias
                        NombreColumnas = lineas
                        for i in range(len(NombreColumnas)-1, -1, -1):
                            #NombreColumnas[i]=NombreColumnas[i].strip()
                            if NombreColumnas[i] == "":
                                del NombreColumnas[i]
                            if NombreColumnas[i] == "\n":
                                del NombreColumnas[i]

                        xMisDatos.append(NombreColumnas)
                    else:
                       NombreColumnas = lineas
                       xMisDatos.append(NombreColumnas)

                else:
                    ### Procesa las lineas de datos
                    if len(lineas)>1 and NombreColumnas[0]==lineas[1] and NombreColumnas[1]==lineas[2]:
                        if PrintError:
                            print("Posible encabezado repetido, saltando linea\n",lineas)
                        continue

                    if len(lineas) > 2 and AnchoFijo:
                        #print(lineas)
                        i = -1
                        xRecord = []
                        for n in range(len(xColumna)-1):
                            i = i+1
                            #print(n,xlineas[xColumna[i]+1:xColumna[i+1]])
                            xRecord.append(
                                xlineas[xColumna[n]+1:xColumna[n+1]])
                        xMisDatos.append(xRecord)
                    else:
                        nLineas = len(lineas)
                        nColumnas = len(NombreColumnas)
                        if nLineas == nColumnas:
                            xMisDatos.append(lineas)
                        else:
                            if nLineas > 2:  # Muestra errores solo de las Filas que no son separadores
                                nErrores=nErrores+1
                                if PrintError:
                                    print(f"Error Fila \x1B[31m{xFila}\x1B[0m: Se encontraron \x1B[31m{nColumnas}\x1B[0m columnas, que datos los {nLineas}")

    print(f"\t\tSe importaron \x1B[31m{xFila-xHeadLine-2-nErrores}\x1B[0m \t Registros (No considera encabezados)")
    print(f"\t\tProcesamiento \x1B[31m{xProceso}\x1B[0m \t----> Creando DataFrame")
    ### Saca fila de Encabezados
    xFinal = xMisDatos[0]
    ### Revisar si hay Columnas Repetidas, si encuentra repetidas agregar al final _n, donde n es el numero indice de cada repetición
    #   si repetidos, poner el indice de columna como _n , donde n es el numero de columna +1
    iCol = 0
    for xCol in xFinal:
        xCadena = xFinal[iCol].strip()
        xFinal[iCol] = xCadena
        # si es mayor a uno significa que hay mas de una columna con el mismo Nombre
        if xFinal.count(xCol) > 1:
            xFinal[iCol] = xCol+"_"+str(iCol+1)
        iCol = iCol+1
    ########
    del xMisDatos[0]
    ### Crea el Dataframe y
    xDF = pd.DataFrame(data=xMisDatos, columns=xFinal)
    try: ### Trata de Borrar columnas en blanco
        if "" in xDF[:0]:
            xDF.drop(columns="", inplace=True)
    except :
        print("no Tiene Columnas en blanco")

    #Banner(xTipo=0)
    return xDF

def ClearCrt():
    """
    cls : Limpia la pantalla de Consola símil a cls o Clear en otros idiomas.
    """
    if os.name == ("ce", "nt", "dos"):
        os.system ("cls")
    else:
        os.system ("cls")

def Banner(xTitulo="",xAncho=120,xTipo=1,TextMode=True,Pad="L"):
    """
    Permite tener textos en pantalla formateados y encuadrados:\n
    xAncho  -> Es el ancho que tendrá el Banner (default 120)\n
    xTipo 0 -> Banner Titulo (default Nada, creando líneas vacía)\n
    xTipo 1 -> Líneas Intermedias sin líneas superior e inferior\n
    xTipo 2 -> Agrega texto y Líneas Final\n
    xTipo 3 -> Sin Líneas \n
    TextMode-> Si es Verdadero, solo dibuja caracteres\n
               '+', '-' y '|', si es Falso se dibujaran\n
               caracteres
               Ascii Extendidos\n
    Pad     -> Indica la Alineación del Texto\n
               L -> Left o Izquierda (Default L)\n
               C -> Centro\n
               R -> Right o Derecha\n
    """
    Pad="C" if xTipo==0 else Pad
    xTitulo = xTitulo.replace("\t","    ")  ### Remplaza las Tabulaciones por espacios...
    xTitulo = xTitulo.replace("\x1b","        \x1b")
    xTitulo = xTitulo.replace("[0m", "[0m       ")
    xTitulo = xTitulo.replace("[31m", "[31m        ")
    yy1 = 0
    yy2 = 0
    xx = (xAncho-2)
    if xTipo==0:
        xSup = "+"+"-"*xx+"+" if TextMode else "\xB0"+"\xC4"*xx+"\xBF"
        print(xSup)


    if Pad=="C":
        yy1 = int(((xAncho-len(xTitulo))/2)-1)
        yy2 = yy1

    if Pad=="L":
        yy1=0
        yy2=int(xAncho-len(xTitulo)-2)

    if Pad=="R":
         yy1 = int(xAncho-len(xTitulo)-2)
         yy2=0

    xDeltaLinea = int(xAncho-(yy1+yy2+len(xTitulo)+2))
    xTitulo=xTitulo+" "*xDeltaLinea
    Linea2 = "|"+" "*yy1+xTitulo+" "*(yy2)+"|" if TextMode else "\xB3" + "\xFF"*yy1+xTitulo+"\xFF"*yy2+"\xB3"
    if len(xTitulo)>0 and not xTipo==3:
        print(Linea2)
    if xTipo == 0  or  xTipo == 2:
        xInf = "+"+"-"*xx+"+" if TextMode else "\xC0"+"\xC4"*xx+"\xD9"
        print(xInf)
    if xTipo == 1 and len(xTitulo)==0:
        xInf = "+"+"-"*xx+"+" if TextMode else "\xC0"+"\xC4"*xx+"\xD9"
        print(xInf)

    if xTipo == 3 and len(xTitulo) > 0:
        xInf = " "+" "*yy1+xTitulo+" "*yy2+" "
        print(xInf)

def Delta_Fecha(xFecha="Debe Proporcionar una Fecha Valida", xAhora=datetime.now(), EsNulo=False):
    """
        Delta_Fecha : Permite calcula la diferencia entre una fecha y la fecha Actual u otra fecha
                        que se pase como parametro en xAhora
            Parametros :
                xFecha : DataFrame o Valor que contiene una Fecha a la cual se restara la Fecha Actual o la que se pase en xAhora
                xAhora : Si no se pasa nada se usara la Fecha Actual.
                EsNulo : Si se es Verdadero o True, se pasa nulo"""
    try:
        Valor = str((xAhora-xFecha).days) if (type(xFecha) is pd.Timestamp) else "-999"
    except:
        print("Error :", xFecha)

    return Valor

def ConvertFechaMySQL(Valor, sep="/"):
    """
    ConvertFecha: Normaliza los separadores de fecha a Slash, para mejorar compatibilidad, cambia los '-' y '.' a '/'
        Valor   -> Lista, Tupla o DataFrame en columna
        sep     -> Separadore Requerido, por defecto es '/'
    """
    if Valor.strip()=="":
        return None

    if "." or "-" in Valor:
        Valor = Valor.replace(".", sep)
        #return Valor
    Valor1=Valor.split(sep)
    Valor=Valor1[2]+sep+Valor1[1]+sep+Valor1[0]
    return Valor

def ConvertFecha(Valor, sep="/"):
    """
    ConvertFecha: Normaliza los separadores de fecha a Slash, para mejorar compatibilidad, cambia los '-' y '.' a '/'
        Valor   -> Lista, Tupla o DataFrame en columna
        sep     -> Separadore Requerido, por defecto es '/'
    """
    if "." or "-" in Valor:
        return Valor.replace(".",sep)
    return Valor

def ConvertSAPVal(valor, decimal='.'):
    """
    Convert the string number value to a float
     - Remove $
     - Remove comas
     - Convert to float type
    """
    try:
        n_val=valor

        if isinstance(n_val, float):
            return(n_val)

        elif isinstance(n_val, int):
            return (n_val)

        if '$' in n_val:
            n_val = n_val.replace('$', '')

        if ' ' in n_val:
            n_val=n_val.replace(' ','')  ### Quita los espacios dentro de la cadena si los tiene

        if '-' in n_val:
                n_val = n_val.replace('-', '')
                n_val = '-'+n_val

        if decimal == '.' and ',' in n_val:
            n_val = n_val.replace(',', '')

        if decimal == ',' and '.' in n_val:
                n_val = n_val.replace('.', '')

        if ',' in n_val:
                n_val = n_val.replace(',', '.')
        ## transformar al final el resultado a que sea decimal siempre el .

        n_val = 0 if n_val == '' else float(n_val)
        return ((n_val))
    except:
        print(f"Error en dato :{valor} (posible encabezado no detectado)")

def ConvertInt(valor):
    """
    Convert the string number value to a float
     - Remove $
     - Remove comas
     - Convert to float type
    """
    if isinstance(valor, float):
        return(valor)
    elif isinstance(valor, int):
        return (valor)
    else:
        if '-' in valor:
            new_val='-'+valor.replace('-','')
        new_val = valor.replace(',', '.').replace('$', '')
        new_val = 0 if new_val == '' else float(new_val)
        return (round(new_val, 1))

def ToExcel(NombreArchivo="SalidaSinNombre.xlsx", DataFrames=[], NombreHoja="Hoja1",AutoOpen=False,xCord=0,yCord=0,Titulo=None,xListaDatos=[],xListaHojas=[]):
    """
    ToExcel : Permite crear archivos excel\n
    NombreArchivo   -> Nombre del Archivo de Salida\n
    DataFrame       -> un dataframe o array que se grabaran en Excel\n
    NombreHoja      -> Indica el Nombre de la Hoja (Default Hoja1) cambiando a lista\n
    """
    ### Como mejora :
    #                xCord       : Indicar coordenada de Inserción fila
    #                yCord       : Indica la columna donde iniciara la inserción
    #                Titulo      : Texto que se usara como Titulo, Ojo que si existe adecuar xCord e yCord para que se pueda agregar
    #                xListaDatos : pasar lista con los dataframe que se pondrán en las respectivas hojas
    #                xListaHojas : pasar lista de hojas, revisar que la misma cantidad de dataframe tengan su respectivo nombre de Hoja
    #if not Titulo is None:
    xCord = 3 if (xCord < 3 and not Titulo is None) else xCord
    yCord = 0 if (yCord < 0 ) else yCord
    ### Revisar si NombreHoja existe y si es una list o String

    try:

        writer = ExcelWriter(NombreArchivo, engine='xlsxwriter')
        DataFrames.to_excel(writer, index=False,
                            sheet_name=NombreHoja, startrow=xCord,startcol=yCord)
        writer.save()

    except:
        print("Error Inesperado: ", sys.exc_info()[0])
        print(EnvironmentError)

    try:
        if AutoOpen:
            os.system("start EXCEL.EXE "+NombreArchivo)
    except:
        print("ERROR OPEN FILE ....\n \
               Cierre su copia Abierta.")

def ToExcel2019(xArchivo="SalidaSinNombre.xlsx",DataFrames=[], NombreHojas=["Hoja1"], ColumnasHojas=[], \
                AutoOpen=False, xCord=1, yCord=1, Titulo=[],AgruparCeldas=False,xIndex=True):
    """
    ToExcel2019 : Permite crear archivos excel con una o Varias Hojas, incluido Títulos\n
    xArchivo        -> Nombre del Archivo de Salida XLSX\n
    DataFrames      -> un dataframe o array que se grabaran en Excel, Puede ser Anidado \n
    NombreHoja      -> un dataframe o Lista con los Nombres de las Hojas,(Default Hojas) cambiando a lista\n
    ColumnasHojas   -> Si el Dataframe o Lista no trae los encabezados, se puede agregar en este, pasar "" si no se requiere en alguna Hoja
    AutoOpen        -> True, si quiere abrir el archivo al finalizar, por defecto False\n
    xCord           -> Fila en la que se insertara el Primer Registro, default es 0\n
    yCord           -> Columna en la que se insertara, default es 0\n
        Nota:\n
            xCord / yCord : Se ajustaran Automáticamente si existe un Titulo asignado \n
    Titulo          -> Lista de Títulos que se Aplicaran a Cada Hoja, lo que Afectara a xCord si este es menor a 3\n
    AgruparCeldas   -> Permite que se agrupen las celdas repetidas subyacentes.\n
    xIndex          -> Agrega o no la Columna de Indice del DataFrame default es True
    """
    xCord = 1 if (xCord < 1 and not Titulo is None) else xCord
    yCord = 2 if (yCord < 1) else yCord
    ### Revisar si NombreHoja existe y si es una list o String
    try:
        with pd.ExcelWriter(xArchivo, engine='xlsxwriter', date_format='dd.mm.yyyy',datetime_format='dd.mm.yyyy') as writer:
            i=0
            for xNombreHoja in NombreHojas:
                if xNombreHoja == '':
                    xNombreHoja = "Hoja1"
                i=i+1
                if i-1 == 0 and not type(DataFrames) is list:
                    xDataFrame=pd.DataFrame.from_records(DataFrames)

                else:
                    xDataFrame=DataFrames[i-1]
                if type(xDataFrame) is list:
                    xColumnas = ColumnasHojas[i-1]
                    if len(xColumnas)>0:
                        xDataFrame = pd.DataFrame.from_records(xDataFrame,columns=xColumnas)
                    else:
                        xDataFrame = pd.DataFrame.from_records( xDataFrame)

                xDataFrame.to_excel(writer, index=xIndex,sheet_name=xNombreHoja, startrow=xCord, startcol=yCord-1,merge_cells=AgruparCeldas)
            writer.save()
            #writer.close()
            #### Probar Abrir y Agregar los Títulos si es que los Tiene
            # client.Dispatch("Excel.Application")
            # client.Dispatch("Excel.Application")
            # client.gencache.EnsureDispatch('Excel.Application')
            # win32.Dispatch('Excel.Application')
            # win32.gencache.EnsureDispatch('Excel.Application')
            xExcel = client.dynamic.Dispatch("Excel.Application")

            #xExcel=client.Dispatch("Excel.Application")
            wb = xExcel.Workbooks.open(xArchivo)
            i=0
            for xNombreHoja in NombreHojas:
                if xNombreHoja=='' :
                    xNombreHoja="Hoja1"
                i=i+1
                ws = wb.Worksheets(xNombreHoja)
                ws.Columns.AutoFit()
                if Titulo!=[]:
                    if len(Titulo[i-1])>0:
                        #xCelda=chr(64+yCord)+str(xCord)
                        ws.Cells(yCord, xCord).Value = Titulo[i-1]
                        #ws.Range(xCelda).Value = Titulo[i-1]
                        ws.Cells(yCord, xCord).Font.Size = 14
            wb.Save()
            #wb.close()
            try:
                if AutoOpen:
                    xExcel.visible = True
                    #os.system("start EXCEL.EXE "+xArchivo)
                else:
                    xExcel.Application.Quit()
            except:
                print("ERROR OPEN FILE ....\n \
                    Cierre su copia Abierta.")
                xExcel.Application.Quit()

    except Exception as e:
        print("Error Inesperado: ", sys.exc_info()[0])
        print(e)
        print(EnvironmentError)
        xExcel.Application.Quit()  ## Trata de cerrar si esta abierto

    finally:
        ws=None
        wb=None
        xExcel=None
        writer=None

def AjusteAños(dfx="Error : Debe especificar un Dataframe"):
    """
    AjusteAños : Revisa que el calculo de Años en una columna no sean negativos o decimales.
        Parametro :
            dfx : Dataframe (columna dentro de ) con un valor entero o decimal que representa un calculo de años
    """
    if dfx['xYear'] < 1:
        return 1
    else:
        return dfx['xYear']

def EstadoVencimientoContratosSGCP(xdf="Error : Debe especificar un Dataframe"):
    """
    EstadoVencimientoContratosSGCP : Determina para efectos de SGCP (Sub Gerencia Control Proyecto) un estado tipo texto según el,
                                     rango de días que tiene la columna que se pasa en el dataframe
    """
    if xdf['Vencimiento Contrato'] <= 30 and xdf['Vencimiento Contrato'] > 15:
        return "a menos de 30 días"
    elif xdf['Vencimiento Contrato'] <= 15 and xdf['Vencimiento Contrato'] >10:
        return "a menos de 15 días"
    elif xdf['Vencimiento Contrato'] <= 10 and xdf['Vencimiento Contrato'] > 0:
        return "a menos de 10 días"
    elif xdf['Vencimiento Contrato'] > 30:
        return "En Plazo"
    elif xdf['Vencimiento Contrato'] <=-60:
        return "Cerrado / Eliminado"
    else:
        return "Vencido"

def EstadoVencimientoContratos(xdf="Error : Debe especificar un Dataframe"):
    if xdf['Vencimiento Contrato'] > 00 and xdf['Vencimiento Contrato'] <= 30*6:
        return "<= 6 Meses"
    else: # xdf['Vencimiento Contrato'] > 30*6
        return "> a 6 Meses"

def EstadoHDT(xpd="Error: Debe Proporcionar un DataFrame"):
    if xpd['nDias']> 10:
        return "Sin Ingreso por mas de "+str(xpd['nDias'])+" días"
    else:
        return ""

def EstadoVencimiento(xdf="Error : Debe especificar un Dataframe"):
    #if  xdf['Fecha Fin']>0:
        if xdf['Vencimiento Garantias'] < -100 :
            return "¿Devuelta?"
        elif xdf['Vencimiento Garantias'] > 00 and xdf['Vencimiento Garantias'] <= 15:
            return "> a 0 días"
        elif xdf['Vencimiento Garantias'] > 15 and xdf['Vencimiento Garantias'] <= 30:
            return "> a 15 días"
        elif xdf['Vencimiento Garantias'] > 30 and xdf['Vencimiento Garantias'] <= 60:
            return "> a 30 días"
        elif xdf['Vencimiento Garantias'] > 60 and xdf['Vencimiento Garantias'] <= 90:
            return "> a 60 días"
        elif xdf['Vencimiento Garantias'] > 90 and xdf['Vencimiento Garantias'] <= 120:
            return "> a 90 días"
        elif xdf['Vencimiento Garantias'] >120:
            return "> a 120 días"
        else:
            return "¿Vencida?"

def color_negative_red(valor):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = 'red' if valor < 0 else 'black'
    return 'color: %s' % color

def a15Dias(s):
    color='red' if s <=15 else ''
    return 'background-color: ' % color

def EnviarCorreoAdjunto(destinatario='lcorales', Titulo="@Python - Correos Automaticos", copy=None, mensaje=None, adjunto=None, html=False):
    #### NOTA:
    ####      Recordar que tanto los destinatarios como los en copia se separan con ;
    ####      Este proceso funciona sin problemas para enviar desde Outlook sin pasar credenciales (talvez solo si esta uno logeado)
    ol = client.Dispatch("Outlook.Application")
    mail = ol.CreateItem(0)
    mail.To = destinatario
    mail.Subject = Titulo
    mail.Importance= 2

    if not copy is None:
        mail.CC = copy

    if html:
        if not mensaje is None:
            mail.HTMLBody = mensaje
    else:
        if not mensaje is None:
            mail.Body = mensaje

    if not adjunto is None:
        mail.Attachments.Add(adjunto)

    mail.Send()


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders


def emailSender(xTo ,Asunto="TEST", xBody="Hola Mundo",xServer="Outlook",adjunto=""):
    """
    emailSender : Permite enviar correos con adjuntos si se requiere.
    @parameters :
        xTo     : Destinatario(s), si es mas de uno se debe separar con ';'
        Asunto  : Texto del Asunto o referencia del mensaje.
        xBody   : Texto del cuerpo principal del Mensaje, texto plano o HTML
        xServer : Servicio de correo que se utilizara, ya sea "Outlook" o "gmail"
        adjunto : Archivo en cualquier formato que se enviara como adjunto.

    """
    # Define email addresses to use
    xTo=xTo.split(";")
    for addr_to in xTo:
        # User_email esta definido al inicio del archivo....
        if True:
            User_email="lcorales@colbun.cl"
            PassWord="LvIj202105"
        else:
            User_email="notificador@colbun.cl"
            PassWord="notificador"

        addr_from = 'dexsys@gmail.com' if xServer=="gmail" else User_email

        smtp_server='smtp.gmail.com'     if xServer=="gmail" else 'smtp.office365.com'
        smtp_port   = 587

        smtp_user   = 'dexsys@gmail.com' if xServer=="gmail" else User_email
        smtp_pass   = 'ffsgunnbyrqdsfgk' if xServer=="gmail" else PassWord

        # Construct email
        msg = MIMEMultipart('alternative')
        msg['To'] = addr_to
        msg['From'] = addr_from
        msg['Subject'] = Asunto

        # Create the body of the message (a plain-text and an HTML version).
        #text = "This is a test message.\nText and html."

        # Record the MIME types of both parts - text/plain and text/html.
        #part1 = MIMEText(text, 'plain')
        part2 = MIMEText(xBody, 'html')
        if not adjunto=="":
            xFile1 = MIMEBase('application', "octet-stream")
    #       I have a CSV file named `attachthisfile.csv` in the same directory that I'd like to attach and email
            xFile1.set_payload(open(adjunto, "rb").read())
            encoders.encode_base64(xFile1)
            xFile=os.path.basename(adjunto)
            xFile1.add_header('Content-Disposition', f"attachment; filename={xFile}")
            msg.attach(xFile1)

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.

        msg.attach(part2)

        # Send the message via an SMTP server
        try:
            s = smtplib.SMTP(smtp_server, smtp_port)
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(smtp_user,smtp_pass)
            s.sendmail(addr_from, addr_to, msg.as_string())
            s.quit()
        except:
            print("ERROR ----> Se produjo un Error al tratar de enviar el correo, cheque, la configuracion smtp.")
            ErroresCorreos=1
