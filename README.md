# Small Project in Cloud Computing

## Objectif

The goal of this project was to create a model using an algorithm (Linear Regression, Classification) and create an API using this model.

For this small project I used two dataset : 

<a>https://storage.googleapis.com/h3-data/listings_final.csv</a>
<a>https://storage.googleapis.com/h3-data/price_availability.csv</a>

And the Linear Regression algorithm in order to predict the local_price depending on :

- Local_price 
- Latitude
- Longitude
- Pricing_weekly_factor
- Pricing_monthly_factor
- Person_capacity
- Beds
- Bedrooms
- Bathrooms

## API

### Available routes

predict("/predict") :

**Method** : POST

**Body** : Item (latitude : float, longitude : float, pricing_weekly_factor : float, pricing_monthly_factor : float, person_capacity : int, beds : int, bedrooms : int, bathrooms : int)

**Return** : Predicted local_price
