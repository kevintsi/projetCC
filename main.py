from joblib import load
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    latitude : float
    longitude : float
    pricing_weekly_factor : float
    pricing_monthly_factor : float
    person_capacity : int
    beds : int
    bedrooms : int
    bathrooms : int

app = FastAPI()

@app.post("/predict/")
async def predict(item: Item):
    """
        Route used to predict a local price with a given Item (latitude, longitude, pricing_weekly_factor, pricing_monthly_factor, person_capacity, beds, bedrooms, bathrooms)
    Args:
        item (Item): an Item 

    Returns:
        float : predicted local price
    """
    model = load("./ml/model.joblib")
    #print("Data : {}".format(item))
    data = [item.latitude, item.longitude, item.person_capacity, item.beds, item.bedrooms, item.bathrooms, item.pricing_weekly_factor, item.pricing_monthly_factor]
    #print("Data to string : {}".format(data))
    predict_value = model.predict([data])
    return predict_value[0]