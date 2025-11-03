# IMPORTACION DE LIBRERÍAS
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split

# CARGA DE DATOS
df = sns.load_dataset('titanic') # Usamos la librería seaborn para cargar el dataset del Titanic 

#VISTA DE LOS DATOS SIN PROCESAR
print("Vista previa de los datos sin procesar:")
print(df.head())
print("\nInformación general de los datos sin procesar:")
print(df.info())