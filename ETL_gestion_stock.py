import pandas as pd
import requests



def extract_1(url):#format CSV
    try:
        data=pd.read_csv(url) # "skip" ignore les lignes mal formatées ,on_bad_lines='skip'
        return data
    except Exception as e :
        print( "statut",e)
        return None


"""def extract(url):# format json
    file=requests.get(url)
    if file.ok:
        data =file.json()
        df= pd.dataframe(data)
        return df
    else:
        print("reponse sur le fichier",file.status_code)
        return None
    return df
"""
#format bd



def tranform(df,TVA):
# Ajouter une nouvelle colonne 'Montant' en multipliant Quantité et PrixUnitaire(€)
    df['Montant'] = df['Quantité'] * df['Prix Unitaire (€)']
    df['TVA'] = df['Montant'] * TVA
    return df


"""
def load(data, path):
    try:
        data.to_excel(path,index=False,)
        print("suces")
    except Exception as e:
        print("echec")

"""

def load(data, path):
    try:
        # Sauvegarde des données dans un fichier Excel
        data.to_excel(path, index=False, engine='openpyxl') #df.to_csv("foo.csv")
        print("Succès ! Les données ont été chargées dans le fichier Excel.")
    except Exception as e:
        print(f"Échec lors du chargement des données dans le fichier Excel. Erreur : {e}")

#exécution
print(" Extaction*****")
url ="https://raw.githubusercontent.com/J-Y-KPANGBAN/PROJET_etl_v1/refs/heads/main/stock_grande_surface.csv"
df =extract_1(url)
print(df.head())

print("transformation*****")
df_transf=tranform(df,0.20)
print(df.head())

print("chargement*****")
chemin ="C:/Users/Jean-YvesDG/Downloads/projet_gestion_ETL_python/mon_file.xlsx"
load(df,chemin)

print("les statistiques",df.describe())
print("les statistiques",df.shape())

