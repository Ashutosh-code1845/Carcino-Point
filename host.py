import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


def cancer_predict(input_data):

    # change the input data to numpy array
    feed_data = np.asarray(input_data)

    # reshape the numpy array as we are predictiong for only one data point
    feed_data_reshape = feed_data.reshape(1, -1)

    prediction = loaded_model.predict(feed_data_reshape)

    if (prediction[0] == 0):
        return "The cancer is Malignant, High risk detected"
    else:
        return "The cancer is Benign, Low risk detected"


def main():
    # giving title
    st.title('ChemoWave')
    st.write('Hosted for Educational Purpose  [Github](https://github.com/Ashutosh-code1845/Qardio-Point)')
    # getting data from user
    radius_mean = st.text_input("Enter the value of Mean Radius: ")
    texture_mean = st.text_input("Enter the value of Mean Texture: ")
    perimeter_mean = st.text_input("Enter the value of Mean Perimeter: ")
    area_mean = st.text_input("Enter the value of Mean Area: ")
    smoothness_mean = st.text_input("Enter the value of Mean Smoothness: ")
    compactness_mean = st.text_input("Enter the value of Mean Compactness: ")
    concavity_mean = st.text_input("Enter the value of Mean Concavity: ")
    concave_points_mean = st.text_input("Enter the value of Mean Concave Points: ")
    symmetry_mean = st.text_input("Enter the value of Mean Symmetry: ")
    fractal_dimension_mean = st.text_input("Enter the value of Mean Fractional Dimension: ")
    radius_se = st.text_input("Enter the value of Radius: ")
    texture_se = st.text_input("Enter the value of Texture: ")
    perimeter_se = st.text_input("Enter the value of Perimeter: ")
    area_se = st.text_input("Enter the value of Area: ")
    smoothness_se = st.text_input("Enter the value of Smoothness: ")
    compactness_se = st.text_input("Enter the value of Compactness: ")
    concavity_se = st.text_input("Enter the value of Concavity: ")
    concave_points_se = st.text_input("Enter the value of Concave Points: ")
    symmetry_se = st.text_input("Enter the value of Symmetry: ")
    fractal_dimension_se = st.text_input("Enter the value of Fractional Dimension: ")
    radius_worst = st.text_input("Enter the value of Worst Radius: ")
    texture_worst = st.text_input("Enter the value of Worst Texture: ")
    perimeter_worst = st.text_input("Enter the value of Worst Perimeter: ")
    area_worst = st.text_input("Enter the value of Worst Area: ")
    smoothness_worst = st.text_input("Enter the value of Worst Smoothness: ")
    compactness_worst = st.text_input("Enter the value of Worst Compactness: ")
    concavity_worst = st.text_input("Enter the value of Worst Concavity: ")
    concave_points_worst = st.text_input("Enter the value of Worst Concave Points: ")
    symmetry_worst = st.text_input("Enter the value of Worst Symmetry: ")
    fractal_dimension_worst = st.text_input("Enter the value of Worst Fractional Dimension: ")

    #code for prediction
    diagnosis = ""

    #button
    if st.button("Test Result"):
        diagnosis = cancer_predict([radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst])

    if diagnosis == "The cancer is Malignant, High risk detected":
        st.error(diagnosis)
    else:
        st.success(diagnosis)

#to make the run code run through command prompt taking main as the first function
if __name__ == '__main__':
    main()