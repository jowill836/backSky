from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import pandas as pd

# Charger les données
file_path = 'data/hygdata_v37.csv'
star_data = pd.read_csv(file_path)
star_data = star_data.fillna('null')

# Créer l'application Flask
app = Flask(__name__)

# Activer CORS pour votre application Flask
CORS(app)


# Configuration JWT
app.config["JWT_SECRET_KEY"] = "votre_secret_jwt"  # Changez ceci pour votre clé secrètels
jwt = JWTManager(app)

# Route pour se connecter et obtenir un token JWT
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    # Ici, validez l'authenticité de l'utilisateur (exemple simplifié)
    if username != "admin" or password != "password":
        return jsonify({"msg": "Mauvais nom d'utilisateur ou mot de passe"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

# Route pour obtenir toutes les étoiles
@app.route('/stars', methods=['GET'])
@jwt_required()
def get_stars():
    return jsonify(star_data.head(1000).to_dict(orient='records'))

# Fonction pour estimer la température à partir de la classe spectrale
def estimate_temperature(spect):
    if pd.isna(spect) or len(spect) == 0:
        return float('inf')  # Aucune donnée spectrale disponible
    # Ajoutez ici la logique pour estimer la température
    # Exemple très simplifié :
    temp_order = 'OBAFGKM'
    return temp_order.find(spect[0])  # Utilise le premier caractère pour l'estimation

# Route pour obtenir les 50 étoiles les plus chaudes
@app.route('/stars/hottest', methods=['GET'])
@jwt_required()
def get_hottest_stars():
    star_data['estimated_temp'] = star_data['spect'].apply(estimate_temperature)
    hottest_stars = star_data.nsmallest(50, 'estimated_temp')
    return jsonify(hottest_stars.to_dict(orient='records'))

# Route pour obtenir les 50 étoiles les plus proches
@app.route('/stars/closest', methods=['GET'])
@jwt_required()
def get_closest_stars():
    closest_stars = star_data.nsmallest(50, 'dist')
    return jsonify(closest_stars.to_dict(orient='records'))

# Route pour obtenir les 50 étoiles les plus brillantes
@app.route('/stars/brightest', methods=['GET'])
@jwt_required()
def get_brightest_stars():
    brightest_stars = star_data.nlargest(50, 'mag')
    return jsonify(brightest_stars.to_dict(orient='records'))

# Route pour obtenir les 50 étoiles les plus grosses
@app.route('/stars/biggest', methods=['GET'])
@jwt_required()
def get_biggest_stars():
    biggest_stars = star_data.nlargest(50, 'lum')
    return jsonify(biggest_stars.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
