import joblib
 

regr_from_joblib = joblib.load('random_forest_crop_yield_model.pkl')
 

import numpy as np

def yield_fn(features_list):

      int_features2 = np.array(features_list)

      int_features1 = int_features2.reshape(1, -1)


      tested1=regr_from_joblib.predict(int_features1)



      print(tested1)

      return  tested1

