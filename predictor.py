
import numpy as np
import pickle

#loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))   #rb = read binary file

#we will use the prediction system now on trained model

input_data = (13.28,20.28,87.32,545.2,0.1041,0.1436,0.09847,0.06158,0.1974,0.06782,0.3704,0.8249,2.427,31.33,0.005072,0.02147,0.02185,0.00956,0.01719,0.003317,17.38,28,113.1,907.2,0.153,0.3724,0.3664,0.1492,0.3739,0.1027)

#change the input data to numpy array
feed_data = np.asarray(input_data)

#reshape the numpy array as we are predictiong for only one data point
feed_data_reshape = feed_data.reshape(1,-1)

prediction = loaded_model.predict(feed_data_reshape)

if(prediction[0]==0):
    print("The cancer is Malignant, High risk detected")
else:
    print("The cancer is Benign, Low risk detected")