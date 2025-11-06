# SQL

## Créer une application PySide6 de type CRUD utilisant SQLite3  
1) Créer une interface qui permettra de gérer des étudiants
> Nom  
> Prenom  
> Age  
> NumeroDA
2) L'interface devra comporter un formulaire permettant
   1) Afficher ou Modifier un étudiant
   2) Des boutons permettant
      1) D'insérer dans la BD
      2) De sauvegarder une modification (voir https://www.w3schools.com/sql/sql_update.asp)
      3) De supprimer un enregistrement
      4) aller à l'enregistrement précédent
      5) aller à l'enregistrement suivant
      6) De recharger tous les enregistrements de la BD (SELECT)
   
## Utiliser un QTableView pour afficher les résultats d'une requête SELECT
1) Vous pouvez vous inspirer du tutoriel: https://www.pythonguis.com/tutorials/pyside6-qtableview-modelviews-numpy-pandas/
2) Ajouter une interface permettant d'ajouter des conditions à la requête et exécuter la requête


## Utilisation des clés
1) Développez une application va modéliser 3 entités dans une BD "films.db".
2) La première table représentera un Film
- filmId (clé primaire)
- nom
- realisateur
- annee
- genreId (clé étrangère vers Genre.genreId)
3) La deuxième table représentera un Genre de film
- genreId (clé primaire)
- nom (clé unique)
4) La troisième table représentera un Acteur
- acteurId (clé)
- nom
- prénom
- (clé unique avec nom + prénom)
5) Ajouter du data à vos tables (si vous êtes en manque d'inspiration, visitez imdb.com)
6) Faites une requête pour aller chercher tous les films appartenant à un genre en utlisant le nom du genre
   1) Vous pouvez dans un premier temps le faire en deux requêtes
   2) Essayer de le faire en une requête en utilisant un INNER JOIN (https://www.tutorialspoint.com/sqlite/sqlite_using_joins.htm)
7) Essayez de représenter la relation plusieurs à plusieurs entre les films et les acteurs
   1) Petit indice: Vous allez avoir besoin d'une nouvelle table (XREF tables ou cross-reference tables)
   2) Faites une requêtes pour sortir la liste des acteurs pour un film