**Accès au README anglais : <a>https://github.com/kevintsi/projetCC/blob/main/README.md</a>** 

# Mini Projet en Cloud Computing

## Objectif

Le but de ce projet était de créer un modèle en utilisant un algorithme (Régression Lineaire, Classification) et créer une API utilisant ce modèle.

Pour ce mini projet, j'ai utilisé 2 datasets : 

<a>https://storage.googleapis.com/h3-data/listings_final.csv</a><br/>
<a>https://storage.googleapis.com/h3-data/price_availability.csv</a>

Et l'algorithme Régression Lineaire dans le but de prédire le prix local en fonction de :

- Latitude
- Longitude
- Le facteur de prix hebdomadaire
- Le facteur de prix mensuel
- Capacité de personnes
- Nombre de lits
- Nombre de chambres
- Nombre de salle de bains

Vous pouvez accéder au projet à travers ce lien : <a>https://kt-cc-mini-project.herokuapp.com</a> 

## Pipeline

### Data Handler

```python
    class DataHandler:
    """
        Classe permettant de récupérer et initialiser les données
    """

    def __init__(self):
        """
            Initialise les données
        """

    def get_data(self):
        """
            Récupère les données à partir d'un serveur distant
        """

    def group_data(self):
        """
            Fusionne les deux datasets
        """

    def get_process_data(self):
        """
            Appel toutes les fonctions
        """
```

### Feature Recipe

```python
class FeatureRecipe:
    """
        Classe qui sépare par type de données et supprime les colonnes inutiles
    """
    
    def __init__(self, data: pds.DataFrame):
        """
            Initialise les données

        Args:
            data (pds.DataFrame): Dataset qui va être utilisé
        """
    
    def separate_variable_types(self) -> None:
        """
            Sépare par types de variable
        """
        
    def drop_uselessf(self):
        """
            Supprime les données inutiles
        """ 
        
    def deal_duplicate(self):
        """
            Récupère tous les duplicatas et les suppriment s'il y en a
        """

    def drop_nanp(self, threshold: float):
        """
            Supprime les colonnes avec un pourcentage @threshold % de NAN

        Args:
            threshold (float): Pourcentage
        """
    
    def get_duplicates(self):
        """
            Récupère tous les duplicatas

        Returns:
            list : Liste des colonnes à supprimer 
        """

    def prepare_data(self, threshold: float):
        """
            Appel toutes les fonctions

        Args:
            threshold (float): Pourcentage
        """
```

### Feature Extractor

```python
class FeatureExtractor:
    """
        Classe Feature Extractor extrait et sépare les données qui vont être utilisé pour l'entrainement.
    """
    
    def __init__(self, data : pds.DataFrame, flist: list):
        """
            Initialise les données

        Args:
            data (pds.DataFrame): Dataset à être utilisé
            flist (list): Liste des colonnes
        """
    
    def extract(self):
        """
            Extrait les données
        """

    def split(self, size_test:float, rnge:int, target:str):
        """
            Sépare les données et récupère X_train, X_test, y_train, y_test 
        Args:
            size_test (float): Proportion de données à être utilisé lors de la séparation de test 
            rnge (int): Controle le mélange appliqué au données avant séparation
            target (str): La cible
        Returns:
            tuple: X_train, X_test, y_train, y_test 
        """
```

### Model Builder

```python
class ModelBuilder: 
    """
        CLasse pour entrainer et afficher les résultats du modèle ML
    """
    def __init__(self, model_path: str = None, save: bool = None):
        """
            Instancie la classe LinearRegression et le chemin pour sauvegarder le modèle
        Args:
            model_path (str, optional): Chemin où sauvegarder le modèle. Par défaut None.
            save (bool, optional): Déjà sauvegardé ou pas. Par défaut None.
        """
        
    def __repr__(self):
    
    def train(self, X, Y):
        """
            Entrainement
        Args:
            X (matrix): Données d'entrainées
            Y (matrix): Valeur cible
        """
    
    def predict_test(self, X) -> np.ndarray:
        """
            Prédire valeur
        Args:
            X (matrix): Echantillons

        Returns:
            np.ndarray: Valeur prédite
        """
        
    def predict_from_dump(self, X) -> np.ndarray:
    
    def save_model(self):
        """
            Sauvegarde le modèle
        """
    
    def print_accuracy(self, X_test, y_test):
        """
            Affiche la précision de l'algorithme

        Args:
            X_test (matrix): Les colonnes de test entrainé Trained test features
            y_test (matrix): La cible de test entrainé
        """

    def load_model(self):
        """
            Charge le modèle

        Returns:
            model : Le modèle
        """
```

## API

### Routes disponibles

predict("/predict") :

**Methode** : POST

**Corps** : Item (latitude : float, longitude : float, pricing_weekly_factor : float, pricing_monthly_factor : float, person_capacity : int, beds : int, bedrooms : int, bathrooms : int)

**Retourne** : Local_price prédit
