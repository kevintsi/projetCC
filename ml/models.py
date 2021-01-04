from .utils.utils import DataHandler, FeatureExtractor, FeatureRecipe

def DataManager(d: DataHandler=None, fr: FeatureRecipe=None, fe: FeatureExtractor=None):
    """
    
        Fonction qui lie les 3 premières classes de la pipeline et qui retourne FeatureExtractor.split(0.1)
    
    Args:
        d (DataHandler, optional): [description]. Defaults to None.
        fr (FeatureRecipe, optional): [description]. Defaults to None.
        fe (FeatureExtractor, optional): [description]. Defaults to None.
    """
    pass