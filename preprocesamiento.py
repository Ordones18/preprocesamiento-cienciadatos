import pandas as pd
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

def cargar_datos():
# Carga el dataset del Titanic csv 
    return sns.load_dataset('titanic')
    
def preprocesar_datos(df):
# Eliminar columnas irrelevantes
    columnas_a_eliminar = ['deck', 'embark_town', 'alive', 'class', 'who', 'adult_male']
    df.drop(columns=columnas_a_eliminar, inplace=True)
    print(f"Paso 1 Columnas eliminadas {columnas_a_eliminar}")

# Gestionar valores nulos
    mediana_edad = df['age'].median()
    df['age'] = df['age'].fillna(mediana_edad)
    moda_embarked = df['embarked'].mode()[0]
    df['embarked'] = df['embarked'].fillna(moda_embarked)
    print("Paso 2 Valores nulos en 'age' y 'embarked' rellenados con mediana y moda respectivamente")

# Eliminar duplicados
    df.drop_duplicates(inplace=True)
    print("Paso 3 Duplicados eliminados")

# Codificar variables categóricas One-Hot Encoding
    df = pd.get_dummies(df, columns=['sex', 'embarked'], drop_first=True)
    print("Paso 4 Variables 'sex' y 'embarked' codificadas")   

# Normalizar variables numéricas
    scaler = MinMaxScaler()
    columnas_a_normalizar = ['age', 'fare']
    df[columnas_a_normalizar] = scaler.fit_transform(df[columnas_a_normalizar])
    print("Paso 5 Columnas 'age' y 'fare' normalizadas")
        
    print("\n--- PREPROCESAMIENTO COMPLETADO ---")
    return df

def guardar_datos(df, nombre_archivo):
# Guarda el dataframe procesado en un archivo CSV
    df.to_csv(nombre_archivo, index=False)
    print(f"\nDataset limpio guardado exitosamente como '{nombre_archivo}'")

# --- Flujo Principal de Ejecución ---
if __name__ == "__main__":
# Cargar los datos
    datos_originales = cargar_datos()
        
# Preprocesar los datos
    datos_procesados = preprocesar_datos(datos_originales)
        
# Mostrar una vista previa del resultado
    print("\nPrimeras 5 filas del dataset final:")
    print(datos_procesados.head())
        
# Guardar el resultado
    guardar_datos(datos_procesados, 'titanic_procesado.csv')   