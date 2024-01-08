Pour tester l'API que vous venez de créer, vous pouvez utiliser un outil comme Postman, qui est un client API populaire. Voici les étapes générales pour tester votre API avec Postman :

1. **Installation de Postman** : Si vous ne l'avez pas déjà fait, téléchargez et installez Postman depuis [leur site web](https://www.postman.com/downloads/).

2. **Démarrer votre API Flask** : Exécutez votre application Flask en exécutant le script Python (`app.py` ou le nom que vous avez donné à votre fichier). Assurez-vous que Flask s'exécute sans erreurs.

3. **Ouvrir Postman** : Lancez Postman sur votre ordinateur.

4. **Se Connecter pour obtenir un Token JWT** :
   - Dans Postman, créez une nouvelle requête en cliquant sur le bouton `+ New`.
   - Sélectionnez `POST` comme méthode de requête.
   - Entrez l'URL de votre API pour la route de connexion, généralement quelque chose comme `http://127.0.0.1:5000/login`.
   - Dans l'onglet `Body`, sélectionnez `raw` et choisissez `JSON` comme format.
   - Entrez les informations d'identification, par exemple : `{"username": "admin", "password": "password"}`.
   - Cliquez sur `Send`. Vous devriez recevoir un token JWT en réponse.

5. **Utiliser le Token pour Accéder aux Autres Routes** :
   - Créez une nouvelle requête pour une des routes de votre API, par exemple `GET http://127.0.0.1:5000/stars`.
   - Dans l'onglet `Authorization`, sélectionnez `Bearer Token` et collez le token JWT que vous avez reçu précédemment.
   - Cliquez sur `Send` pour exécuter la requête. Vous devriez voir la réponse de votre API dans Postman.

6. **Tester les Différentes Routes** : Répétez la procédure pour les différentes routes (`/stars/hottest`, `/stars/closest`, etc.), en changeant l'URL et la méthode (GET ou POST) selon les besoins de chaque route.



Tester votre API de cette manière vous aidera à comprendre comment elle se comporte en pratique et à identifier les éventuels problèmes à corriger.