import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
#import SessionState

import numpy as np
model = load_model('Model',compile=False)
model.compile()

st.title('Cat & Dog Image Classifier')
input_image = st.file_uploader('Upload image')

if st.session_state.get('CHECK') != True:

    st.session_state['CHECK'] = button1 # Saved the state





if st.session_state['CHECK'] == True:
    predict = load_img(input_image, target_size=(64, 64))
    predict_modified = img_to_array(predict)
    predict_modified = predict_modified / 255
    predict_modified = np.expand_dims(predict_modified, axis=0)
    result = model.predict(predict_modified)
    if result < 0.5:
        probability = 1 - result[0][0]
        if probability<0.60:
            st.write('We are little confused here as we are only ', probability*100, '% sure that its a Cat')
            st.header('CAT')
            
        else:
            st.write('We are ', probability*100, '% sure that its a Cat')
            st.header('CAT')
            
    else:
        probability = result[0][0]
        if probability<0.60:
            st.write('We are little confused here as we are only ', probability*100, '% sure that its a Dog')
            st.header('DOG')
            
        else:
            st.write('We are ', probability*100, '% sure that its a Dog')
            st.header('DOG')
            
    image1 = load_img(input_image)
    image1 = img_to_array(image1)
    image1 = np.array(image1)
    image1 = image1/255.0

    st.image(image1, width=500)
    if st.button('Check 2'):

        st.write("Do your logic here")
   


