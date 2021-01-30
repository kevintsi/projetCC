**Access to french readme : <a>https://github.com/kevintsi/projetCC/blob/main/README_FR.md</a>** 

# Small Project in Cloud Computing

## Objectif

The goal of this project was to create a model using an algorithm (Linear Regression, Classification) and create an API using this model.

For this small project I used two dataset : 

<a>https://storage.googleapis.com/h3-data/listings_final.csv</a><br/>
<a>https://storage.googleapis.com/h3-data/price_availability.csv</a>

And the Linear Regression algorithm in order to predict the local_price depending on :

- Latitude
- Longitude
- Pricing_weekly_factor
- Pricing_monthly_factor
- Person_capacity
- Beds
- Bedrooms
- Bathrooms

You can access the project through this link : <a>https://kt-cc-mini-project.herokuapp.com</a>

## Pipeline

### Data Handler

```python
    class DataHandler:
    """
        Class which retrieves and initializes data
    """

    def __init__(self):
        """
            Initialize data
        """

    def get_data(self):
        """
            Get data from bucket
        """

    def group_data(self):
        """
            Merge both datasets
        """

    def get_process_data(self):
        """
            Call all the functions
        """
```

### Feature Recipe

```python
class FeatureRecipe:
    """
        Class which split by type of data and delete useless features
    """
    
    def __init__(self, data: pds.DataFrame):
        """
            Initialize data

        Args:
            data (pds.DataFrame): Dataset to be used
        """
    
    def separate_variable_types(self) -> None:
        """
            Separate types of variable
        """
        
    def drop_uselessf(self):
        """
            Delete all useless features
        """ 
        
    def deal_duplicate(self):
        """
            Retrieve all duplicates and delete them if there are
        """

    def drop_nanp(self, threshold: float):
        """
            Delete columns with @threshold % of NAN

        Args:
            threshold (float): Pourcentage
        """
    
    def get_duplicates(self):
        """
            Get all duplicates

        Returns:
            list : List of columns to drop 
        """

    def prepare_data(self, threshold: float):
        """
            Call all the methods

        Args:
            threshold (float): Pourcentage
        """
```

### Feature Extractor

```python
class FeatureExtractor:
    """
        Feature Extractor class which will extract all and split the data that will be used to train  
    """
    
    def __init__(self, data : pds.DataFrame, flist: list):
        """
            Initalize data

        Args:
            data (pds.DataFrame): Dataset to be used
            flist (list): list of features
        """
    
    def extract(self):
        """
            Extract data
        """

    def split(self, size_test:float, rnge:int, target:str):
        """
            Split data and get X_train, X_test, y_train, y_test 
        Args:
            size_test (float): Proportion of data to be used when test split 
            rnge (int): Controls the shuffling applied to the data before applying the split
            target (str): The target
        Returns:
            tuple: X_train, X_test, y_train, y_test 
        """
```

### Model Builder

```python
class ModelBuilder: 
    """
        Class for train and print results of ml model 
    """
    def __init__(self, model_path: str = None, save: bool = None):
        """
            Instanciate the LinearRegression class and path to save model
        Args:
            model_path (str, optional): Path where to save model. Defaults to None.
            save (bool, optional): Already save or not. Defaults to None.
        """
        
    def __repr__(self):
    
    def train(self, X, Y):
        """
            Train
        Args:
            X (matrix): Training data
            Y (matrix): Target values
        """
    
    def predict_test(self, X) -> np.ndarray:
        """
            Predict value
        Args:
            X (matrix): Samples

        Returns:
            np.ndarray: Predict values
        """
        
    def predict_from_dump(self, X) -> np.ndarray:
    
    def save_model(self):
        """
            Save model
        """
    
    def print_accuracy(self, X_test, y_test):
        """
            Print accuracy of algorithm

        Args:
            X_test (matrix): Trained test features
            y_test (matrix): Trained test target
        """

    def load_model(self):
        """
            Load model

        Returns:
            model : Model
        """
```

## API

### Available routes

predict("/predict") :

**Method** : POST

**Body** : Item (latitude : float, longitude : float, pricing_weekly_factor : float, pricing_monthly_factor : float, person_capacity : int, beds : int, bedrooms : int, bathrooms : int)

**Return** : Predicted local_price
