#importing the libraries
import streamlit as st
from tensorflow import keras
from PIL import Image
from skimage.transform import resize
import numpy as np
import time

#loading the image classifier model
img_clf = keras.models.load_model('...file_path/img_cls_cnn')


#functions to predict image

def predict(X):
     
    # Compute the probability of a elephant present in the picture
    Y_prediction = img_clf.predict(X)
         
    return Y_prediction

# Designing the interface
st.title("Asian-African Image Classification App")
# For newline
st.write('\n')

image = Image.open("...file_path/cover.jpg")
show = st.image(image, use_column_width=True)

st.sidebar.title("Upload Image")

#Disabling warning
st.set_option('deprecation.showfileUploaderEncoding', False)
#Choose your own image
uploaded_file = st.sidebar.file_uploader(" Choose an Elephant Image ",type=['png', 'jpg', 'jpeg'] )

if uploaded_file is not None:
    
    u_img = Image.open(uploaded_file)
    show.image(u_img, 'Uploaded Image', use_column_width=True)
    # We preprocess the image to fit in algorithm.
    image = np.asarray(u_img)/255
    
    my_image= resize(image, (180,180)).reshape((1, 180,180,3))

# For newline
st.sidebar.write('\n')
    
if st.sidebar.button("Click Here to Classify"):
    
    if uploaded_file is None:
        
        st.sidebar.write("Please upload an Image to Classify")
    
    else:
        
        with st.spinner('Classifying ...'):
            
            prediction = predict(my_image)
            time.sleep(2)
            st.success('Done!')
            
        st.sidebar.header("Algorithm Predicts: ")
        
        #Formatted probability value to 3 decimal places
        probability = "{:.3f}".format(float(prediction*100))
        
        # Classify elephant present in the picture if prediction > 0.5
        
        if prediction > 0.5:
            
            st.sidebar.write(" It is an 'Asian' Elephant. ", '\n' )
              
                             
        else:
            st.sidebar.write(" It is an 'African' Elephant. ",'\n')
            

