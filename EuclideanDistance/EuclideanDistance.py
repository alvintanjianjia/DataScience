import sklearn
import pandas as pd
import numpy as np
from sklearn import preprocessing

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances

restaurants = pd.read_csv('List of restaurants.csv')

res_nutrition_min = restaurants['Food Nutrition Score'].min()
res_nutrition_max = restaurants['Food Nutrition Score'].max()
res_dist_min = restaurants['Distance (km)'].min()
res_dist_max = restaurants['Distance (km)'].max()
res_price_min = restaurants['Price for one meal (per pax/per set)'].min()
res_price_max = restaurants['Price for one meal (per pax/per set)'].max()

restaurants['Food Nutrition Score']=(restaurants['Food Nutrition Score']-restaurants['Food Nutrition Score'].min())/(restaurants['Food Nutrition Score'].max()-restaurants['Food Nutrition Score'].min())
restaurants['Distance (km)']=(restaurants['Distance (km)']-restaurants['Distance (km)'].min())/(restaurants['Distance (km)'].max()-restaurants['Distance (km)'].min())
restaurants['Price for one meal (per pax/per set)']=(restaurants['Price for one meal (per pax/per set)']-restaurants['Price for one meal (per pax/per set)'].min())/(restaurants['Price for one meal (per pax/per set)'].max()-restaurants['Price for one meal (per pax/per set)'].min())
restaurant_num = restaurants[['Distance (km)', 'Food Nutrition Score' , 'Price for one meal (per pax/per set)']]




user_continue = True
while user_continue is True:
    user_reply = input('Do you want to continue? 0 or 1')
    if int(user_reply) == 0:
        break
    distance = float(input("Preferred distance (km)?"))
    nutrition = float(input("How healthy (0-1)? 1 being most unhealthy"))
    price = float(input("Preferred price (RM)?"))



    distance = (distance-res_dist_min)/(res_dist_max-res_dist_min)
    price = (price - res_price_min) / (res_price_max - res_price_min)
    nutrition = (nutrition - res_nutrition_min) / (res_nutrition_max - res_nutrition_min)


    print(distance, nutrition, price)

    euclidean_array = euclidean_distances(restaurant_num, [[distance, nutrition, price]])

    smallest_euclidean = np.min(euclidean_array)
    smallest_euclidean_index = np.argmin(euclidean_array)
    print(restaurants.iloc[smallest_euclidean_index, :])
print('Thank you')


