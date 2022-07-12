import numpy as np;
import pandas as pd;
import matplotlib.pyplot  as plt;
from sklearn.model_selection  import train_test_split
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle


from yield_code import yield_fn


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


dist_dict = {'LATUR': 0, 'PALGHAR': 1, 'OSMANABAD': 2, 'WARDHA': 3, 'SOLAPUR': 4, 'YAVATMAL': 5, 'SANGLI': 6, 'NANDED': 7,
 'AHMEDNAGAR': 8, 'MUMBAI': 9, 'RATNAGIRI': 10, 'GADCHIROLI': 11, 'THANE': 12, 'HINGOLI': 13, 'PARBHANI': 14, 'BHANDARA': 15,
 'GONDIA': 16, 'AKOLA': 17, 'JALNA': 18, 'DHULE': 19, 'CHANDRAPUR': 20, 'BEED': 21, 'WASHIM': 22, 'KOLHAPUR': 23,
 'NAGPUR': 24, 'NASHIK': 25, 'RAIGAD': 26, 'PUNE': 27, 'AMRAVATI': 28, 'SATARA': 29, 'JALGAON': 30, 'NANDURBAR': 31,
 'SINDHUDURG': 32, 'BULDHANA': 33, 'AURANGABAD': 34}

dict_state = {'Maharashtra': 0}

dict_season = {'Kharif': 0,
 'Autumn': 1,
 'Whole Year': 2,
 'Summer': 3,
 'Rabi': 4}

dict_crop = {'Gram': 0, 'Other  Rabi pulses': 1, 'Tomato': 2, 'Linseed': 3, 'Rapeseed &Mustard': 4, 'Wheat': 5, 'Other Cereals & Millets': 6,
 'Small millets': 7, 'Safflower': 8, 'Sugarcane': 9, 'Cotton(lint)': 10, 'Urad': 11, 'Sunflower': 12, 'Grapes': 13, 'Arhar/Tur': 14,
 'other oilseeds': 15, 'Ragi': 16, 'Bajra': 17, 'Niger seed': 18, 'Total foodgrain': 19, 'Maize': 20, 'Jowar': 21, 'Rice': 22,
 'Banana': 23, 'Castor seed': 24, 'Mango': 25, 'Onion': 26, 'Sesamum': 27, 'Pulses total': 28, 'Moong(Green Gram)': 29, 'Groundnut': 30,
 'Other Kharif pulses': 31, 'Tobacco': 32, 'Soyabean': 33}

dict_soil = {'sandy': 0,
 'loamy': 1,
 'clay': 2,
 'peaty': 3,
 'silty': 4,
 'chalky': 5,
 'silt': 6}

feature_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


from recamandation_code import recondation_fn


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html') 

    
@app.route('/production')
def production(): 
    return render_template('index.html')


@app.route('/production/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    int_features = [str(x) for x in request.form.values()]

    print("output from web page  ",int_features)

    state_ind = dict_state[int_features[0]]
    feature_list[0] = state_ind
    print(state_ind)

    dist_ind = dist_dict[int_features[1]]
    feature_list[1] = dist_ind
    print(dist_ind)

    feature_list[2] = float(int_features[2])
    print(feature_list[2])

    season_ind = dict_season[int_features[3]]
    feature_list[3] = season_ind
    print(season_ind)   

    crop_ind = dict_crop[int_features[4]]
    feature_list[4] = crop_ind
    print(crop_ind)

    feature_list[5] = float(int_features[5])
    print(feature_list[5])

    feature_list[6] = float(int_features[6])
    print(feature_list[6])

    feature_list[7] = float(int_features[7])
    print(feature_list[7])

    feature_list[8] = float(int_features[8])
    print(feature_list[8])

    feature_list[9] = float(int_features[9])
    print(feature_list[9])

    soil_ind = dict_soil[int_features[10]]
    feature_list[10] = soil_ind
    print(soil_ind)

    feature_list[11] = float(int_features[11])
    print(feature_list[11])

    feature_list[12] = float(int_features[12])
    print(feature_list[12])

    feature_list[13] = float(int_features[13])
    print(feature_list[13])

    a=feature_list


    print(a)

    output_yield=yield_fn(feature_list)


    return render_template('index.html', prediction_text='Yield  will be    {} kg for Hectare '.format(output_yield[0]*1000))

@app.route('/crop')
def crop():
     return render_template('crop.html')



@app.route('/crop/predict1',methods=['POST'])
def predict1():
    '''
    For rendering results on HTML GUI
    '''
    int_features1 = [str(x) for x in request.form.values()]
    int_features2=['1','2','3','4','5','6']
    a1=int_features1[0]
    a2=int_features1[1]
    a3=int_features1[2]
    a4=int_features1[3]

    
    a5=int_features1[4]
    a6=int_features1[5]
    a7=int_features1[6]
    
    
    
   # int_features21 = np.array(int_features2)




  #  int_features11 = int_features21.reshape(1, -1)
   # prediction1 = model1.predict(int_features11)

    output1 = recondation_fn(a1,a2,a3,a4,a5,a6,a7)
   # resultcrop = {value:key for key, value in croplist.items()}
    print(output1)
    
    
 
    

    

    return render_template('crop.html', prediction1_text='You will get best Yield if you cultivate  {} '.format(output1[0]))



if __name__ == "__main__":
    app.run(debug=True)
