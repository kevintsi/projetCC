import pandas as pds
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import LinearRegression
from joblib import dump, load
import datetime

class DataHandler:
    """
        Class which retrieve data and initialization of data
    """

    def __init__(self):
        print("Initialization")
        self.df_listings_final = None
        self.df_price_availability = None
        self.df_merge = None

    def get_data(self):
        print("Get data from bucket")
        self.df_listings_final = pds.read_csv("https://storage.googleapis.com/h3-data/listings_final.csv", sep=";")

    def group_data(self):
        # merge
        print("Data merged") 
        self.df_merge = pds.merge(self.df_price_availability.groupby('listing_id')['local_price'].mean(), self.df_listings_final, on='listing_id')

    def get_process_data(self):
        self.get_data()
        self.group_data()
        
class FeatureRecipe:
    """
        Class which split by type of data
    """
    
    def __init__(self, data: pds.DataFrame):
        print("FeatureRecipe starts...")
        self.df = data
        self.cate = []
        self.floa = []
        self.intt = []
        print("End of FeatureRecipe initialisation\n")
    
    def separate_variable_types(self) -> None:
        print("Separate variable types starts...")
        for col in self.df.columns:
            if self.df[col].dtypes == int:
                self.intt.append(self.df[col])
            elif self.df[col].dtypes == float:
                self.floa.append(self.df[col])
            else:
                self.cate.append(self.df[col])
        print("Separate variable types end...")
        print ("Dataset number of columns : {} \nnumber of discreet values : {} \nnumber of continuous values : {} \nnumber of others : {} \ntotal size : {}\n".format(len(self.df.columns),
        len(self.intt),len(self.floa),len(self.cate),len(self.intt)+len(self.floa)+len(self.cate) ))
        
    def drop_uselessf(self):
        print("Drop useless feature start...")
        
        if "Unnamed: 0" in self.df.columns:
            self.df.drop("Unnamed: 0", axis=1, inplace=True)
            
        for col in self.df.columns:
            if self.df[col].isna().sum() == len(self.df[col]):
                self.df.drop([col], axis=1, inplace=True)
                
        print("Drop useless feature end...")
        print("Number columns remaining {}\n".format(len(self.df.columns)))
        
    def deal_duplicate(self):
        print("Deal duplicate start...")
        duplicates = self.get_duplicates()
        if len(duplicates) != 0:
            for dplc in duplicates:
                dropped_duplicates = self.df.drop(dplc, axis=1, inplace=True)
                print("Dropped duplicates : {}".format(dropped_duplicates))
        print("Deal duplicate end...")
    
    def drop_nanp(self, threshold: float):
        dropped = 0
        print("Drop columns with {} percentage of NAN".format(threshold))
        self.get_duplicates()
              
        for col in self.df.columns:
            if self.df[col].isna().sum() / self.df.shape[0] >= threshold:
                self.df.drop([col], axis=1, inplace=True)
                dropped+=1
              
        print("Number of columns dropped : {}\n".format(dropped))
    
    def get_duplicates(self):
        print("Get duplicates")
        drop_col = []
        for col_index in range(self.df.shape[1]):
            for second_col_index in range(col_index+1,self.df.shape[1]):
                if self.df.iloc[:,col_index].equals(self.df.iloc[:,second_col_index]):
                    drop_col.append(self.df.iloc[:,second_col_index].name)
        print("Drop col : {}".format(drop_col))
        return drop_col
              
    #def deal_dtime(self):
    #    pass
    
    def prepare_data(self, threshold: float):
        self.drop_uselessf()
        self.separate_variable_types()
        self.deal_duplicate()
        self.drop_nanp(threshold)
        #self.deal_dtime()

class FeatureExtractor:
    """
        Feature Extractor class
    """
    
    def __init__(self, data : pds.DataFrame, flist: list):
        """
            Input : pandas.DataFrame, feature list to drop
            Output : X_train, X_test, y_train, y_test according to sklearn.model_selection.train_test_split
        """
        self.x_train, self.x_test, self.y_train, self.y_test = None, None, None, None
        self.df = data
        self.flist = flist
    
    def extract(self):
        print("Extraction start...")
        for col in self.df.columns:
            if col in self.flist:
                self.df.drop(col, axis=1, inplace=True)
        print("Extraction end...\n")
        
    def split(self, size_test:float, rnge:int, target:str):
        print("Splitting start...")
        print(self.df.loc[:,self.df.columns != target])
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.df.loc[:,self.df.columns != target], self.df[target], test_size=size_test, random_state=rnge)
        print("Splitting end\n ")
        return self.X_train, self.X_test, self.y_train, self.y_test
    
class ModelBuilder:
    """
        Class for train and print results of ml model 
    """
    def __init__(self, model_path: str = None, save: bool = None):
        print("Start constructing ModelBuilder instance...")
        self.path = model_path
        self.save = save
        self.reg = LinearRegression()
        print("End constructing ModelBuilder instance...")
        
    def __repr__(self):
        pass
    
    def train(self, X, Y):
        self.reg.fit(X, Y)
    
    def predict_test(self, X) -> np.ndarray:
        return self.reg.predict(X)
        
    def predict_from_dump(self, X) -> np.ndarray:
        pass
    
    def save_model(self):
        #with the format : 'model_{}_{}'.format(date)
        res = pickle.dumps(self.reg)
        dump(res, "{}/model_{}.joblib".format(self.path, datetime.now()))
    
    def print_accuracy(self, X_test, y_test):
        print("Coef accurancy : {} %".format(self.reg.score(X_test, y_test)*100))

    def load_model(self):
        try:
            #load model
            clt = load("{}/model_{}.joblib".format(self.path, datetime.now()))
        except:
            print("File doesn't exist. You must save the model first")