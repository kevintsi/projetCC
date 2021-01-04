from .utils.utils import DataHandler, FeatureExtractor, FeatureRecipe, ModelBuilder

def DataManager(bucket: str = None, d: DataHandler=None, fr: FeatureRecipe=None, fe: FeatureExtractor=None):
    """
        Fonction qui lie les 3 premières classes de la pipeline et qui retourne FeatureExtractor.split(0.1)
    
    Args:
        d (DataHandler, optional): [description]. Defaults to None.
        fr (FeatureRecipe, optional): [description]. Defaults to None.
        fe (FeatureExtractor, optional): [description]. Defaults to None.
    """
    ## Instanciate DataHandler to retrieve data
    d = DataHandler()
    print("Loading data...")
    d.get_process_data()
    print("Data loaded")
    ## Instanciate FeatureRecipe with the data in parameter to filter the merge
    fr = FeatureRecipe(d.df_merge)
    print("Filtering features...")
    fr.prepare_data(0.3)
    print("Filtering done")

    fe = FeatureExtractor(d.df_merge, list(['listing_id','name','type','city','neighborhood','latitude','longitude','is_rebookable','is_new_listing','is_fully_refundable','is_host_highly_rated']))
    fe.extract()

    return fe.split(0.3,42,'local_price')

X_train, X_test, y_train, y_test = DataManager()
mb = ModelBuilder(".")
mb.train(X_train, y_train)
mb.save_model()

    