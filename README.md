# Image-Classification-Using-Convolutional-Neural-Network-

The project involved building a ML Model for Image classification of Asian and African Elephants using CNN and web-app deployment using Streamlit.

## Dataset
The Dataset mainly comprises of the following details
- Number of classes: 2 (Asian elephant and African elephant)
- Number of images: 1028
- Image shape range: (100, 100) to (4992, 3328)
- To increase complexity the train set contains less than 5% mislabelled images, while all images in the test set have the correct label.

Link to Dataset: https://www.kaggle.com/datasets/vivmankar/asian-vs-african-elephant-image-classification

## ML Model Building
The pre-processing part only involved reshaping the dataset to suitable array as input to the Model. The model was trained on Convolutional Neural Network, which is basically a subtype of Neural Networks that is mainly used for applications in image and speech recognition. Its built-in convolutional layer reduces the high dimensionality of images without losing its information. Convolutional neural networks divide the image into smaller areas in order to view them separately for the first time. That is why CNNs are especially suited for this use case. The training accuracy achieved was 93%.

The model was validated against the test set images from dataset, with average accuracy of 80%. It can be further improved with variety of data and arrangement of the convolutional and max-pooling layers to each different use case.

## Demo Web-App Deployment
The trained model was saved and deployed over web using Streamlit. Streamlit, is an open-source Python library that makes it easy to create and share web apps for machine learning and data science. It doesn’t replace a proper deployment to production that requires monitoring, logging etc. However, it enables you to create “something that works” in a few hours.
A few internet images were used to validate the deployed model and it gave the correct prediction almost every time. Screenshots of the same are available in this repo.
