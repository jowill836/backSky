from fastapi import FastAPI, HTTPException
import pandas as pd
import json
import numpy as np

# Charger le fichier CSV
df = pd.read_csv("data/hygdata_v37.csv")
df.replace([np.inf, -np.inf, np.nan], 0, inplace=True)

# Créer une instance FastAPI
app = FastAPI()

# Route pour obtenir toutes les données
@app.get("/stars")
def get_donnees():
    json_data = json.loads(df.to_json(orient="records"))
    return json_data

# Route pour obtenir les données par id
@app.get("/stars/{element_id}")
def get_element_par_id(element_id: int):
    try:
        # Filtrer le DataFrame pour obtenir l'élément avec l'id spécifié
        element = df[df['id'] == element_id].to_dict(orient="records")[0]
        return element
    except IndexError:
        raise HTTPException(status_code=404, detail="Element non trouvé")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
